import re
import logging
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from azure.kusto.data.exceptions import KustoServiceError
from tabulate import tabulate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_query(query: str) -> tuple[str, str]:
    """
    Validate and extract cluster and database from KQL query.
    
    Returns:
        tuple: (cluster_uri, database)
    """
    logger.info("Validating KQL query...")
    cluster_match = re.search(r"cluster\('([^']+)'\)", query)
    if not cluster_match:
        raise ValueError("Could not extract cluster name. Ensure query includes cluster('<name>').")
    database_match = re.search(r"database\('([^']+)'\)", query)
    if not database_match:
        raise ValueError("Could not extract database name. Ensure query includes database('<name>').")

    raw_cluster = cluster_match.group(1)
    if raw_cluster.startswith("https://"):
        cluster_uri = raw_cluster
    elif "." in raw_cluster:
        cluster_uri = f"https://{raw_cluster}"
    else:
        cluster_uri = f"https://{raw_cluster}.kusto.windows.net"

    database = database_match.group(1)
    logger.info(f"Validated: cluster_uri={cluster_uri}, database={database}")
    return cluster_uri, database

def execute_kql_query(query: str, visualize: bool = False) -> list[dict]:
    """
    Execute a KQL query and return results in a structured format.
    
    Args:
        query (str): The KQL query to execute.
        visualize (bool): If True, include a Markdown table visualization in the result.
        
    Returns:
        list[dict]: Query results as a list of dictionaries.
    """
    logger.info("Preparing to execute KQL query: %s", query)
    
    try:
        cluster_uri, database = validate_query(query)
        
        # Clean the query by removing cluster and database prefixes
        cleaned_query = re.sub(
            r"cluster\('([^']+)'\)\.database\('([^']+)'\)\.",
            "",
            query,
            count=1
        )
        logger.debug(f"Cleaned KQL query:\n{cleaned_query}")
        
        # Authenticate and execute query
        kcsb = KustoConnectionStringBuilder.with_az_cli_authentication(cluster_uri)
        client = KustoClient(kcsb)
        try:
            response = client.execute(database, cleaned_query)
            
            # Extract results
            table = response.primary_results[0]
            columns = [col.column_name for col in table.columns]
            results = [dict(zip(columns, row)) for row in table]
            
            logger.info(f"Query executed successfully. Returned {len(results)} rows.")
            
            # Add visualization if requested
            if visualize and results:
                markdown_table = tabulate(
                    [list(row.values()) for row in results],
                    headers=columns,
                    tablefmt="pipe"
                )
                results.append({"visualization": markdown_table})
            
            return results
            
        finally:
            client.close()  # Ensure client is closed to release resources
            
    except KustoServiceError as ke:
        logger.error("Kusto service error: %s", str(ke))
        raise
    except Exception as e:
        logger.error("Error executing query: %s", str(e))
        raise

if __name__ == "__main__":
    # Example usage
    sample_query = "cluster('mycluster').database('mydb').MyTable | take 10"
    try:
        results = execute_kql_query(sample_query, visualize=True)
        print("Query Results:")
        for row in results:
            if "visualization" in row:
                print(row["visualization"])
            else:
                print(row)
    except Exception as e:
        print(f"Error: {str(e)}")