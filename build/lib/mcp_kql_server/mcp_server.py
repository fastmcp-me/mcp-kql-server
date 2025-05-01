from mcp.server.fastmcp import FastMCP
from typing import Dict, List, Any
from .kql_auth import authenticate
from .execute_kql import execute_kql_query
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
async def kql_execute(input: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute a KQL query against an Azure Data Explorer cluster.

    Args:
        input (dict): A dictionary containing the query.
            - query (str): The KQL query to execute (e.g., cluster('mycluster').database('mydb').MyTable | take 10)
            - visualize (bool, optional): If true, includes a Markdown table visualization.

    Returns:
        dict: A dictionary with the execution status and result.
            - status (str): "success" or "error"
            - result (dict): Contains columns, rows, row_count, and visualization (if requested)
            - error (str): Error message if failed
    """
    query = input.get("query")
    visualize = input.get("visualize", False)
    if not query:
        return {"status": "error", "error": "Missing 'query' field in input"}

    try:
        logger.info("Executing query: %s", query)
        result = execute_kql_query(query, visualize=visualize)
        table_response = {
            "columns": list(result[0].keys()) if result and "visualization" not in result[0] else [],
            "rows": [list(row.values()) for row in result if "visualization" not in row],
            "row_count": len([row for row in result if "visualization" not in row]),
        }
        if visualize and result and "visualization" in result[-1]:
            table_response["visualization"] = result[-1]["visualization"]
        logger.info("Query executed successfully. Rows returned: %d", table_response["row_count"])
        return {"status": "success", "result": table_response}
    except Exception as e:
        logger.error("Error executing query: %s", str(e))
        return {"status": "error", "error": str(e)}

# Run the server
if __name__ == "__main__":
    print("Starting MCP server", file=sys.stderr)
    sys.stderr.flush()
    server.run()