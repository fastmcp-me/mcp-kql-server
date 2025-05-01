from fastmcp import FastMCP
from pydantic import BaseModel
from typing import List, Any, Union
from .kql_auth import authenticate
from .execute_kql import execute_kql_query
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pydantic models for input and output schemas
class KQLInput(BaseModel):
    query: str
    visualize: bool = False

class KQLResult(BaseModel):
    columns: List[str]
    rows: List[List[Any]]
    row_count: int
    visualization: Union[str, None] = None

class KQLOutput(BaseModel):
    status: str
    result: Union[KQLResult, None] = None
    error: Union[str, None] = None

# Check authentication at startup
print("Initializing mcp_kql_server.mcp_server module", file=sys.stderr)
sys.stderr.flush()
auth_status = authenticate()
if not auth_status.get("authenticated"):
    logger.error("Authentication failed: %s", auth_status.get("message"))
    print("Authentication failed. Please run 'az login' and try again.", file=sys.stderr)
    sys.stderr.flush()
    sys.exit(1)

# Define the MCP server
server = FastMCP(
    name="mcp-kql-server",
    version="1.0.0",
    description="MCP server for executing KQL queries with Azure authentication",
)

# Define the KQL execution tool
@server.tool()
async def kql_execute(input: KQLInput) -> KQLOutput:
    """
    Execute a KQL query against an Azure Data Explorer cluster.

    Args:
        input: Input model containing the query and visualization flag.
            - query: The KQL query to execute (e.g., cluster('mycluster').database('mydb').MyTable | take 10)
            - visualize: If true, include a Markdown table visualization.

    Returns:
        KQLOutput: Output model with execution status and result.
    """
    logger.info("Received input: %s", input.dict())
    query = input.query
    if not query:
        return KQLOutput(status="error", error="Missing 'query' field in input")

    try:
        result = execute_kql_query(query, visualize=input.visualize)
        table_response = KQLResult(
            columns=list(result[0].keys()) if result else [],
            rows=[list(row.values()) for row in result if "visualization" not in row],
            row_count=len([row for row in result if "visualization" not in row]),
            visualization=result[-1].get("visualization") if input.visualize and result else None
        )
        logger.info("Query executed successfully. Rows returned: %d", table_response.row_count)
        return KQLOutput(status="success", result=table_response)
    except Exception as e:
        logger.error("Error executing query: %s", str(e))
        return KQLOutput(status="error", error=str(e))

# Run the server
if __name__ == "__main__":
    print("Starting MCP server", file=sys.stderr)
    sys.stderr.flush()
    server.run()