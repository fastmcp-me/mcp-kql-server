# MCP KQL Server

A Microsoft Cloud Platform (MCP) server for executing KQL queries against Azure Data Explorer with Azure CLI authentication.

## Installation

1. Ensure you have `uv` installed:
   ```bash
   pip install uv
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   uvx venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uvx pip install .
   ```

## Running the Server

Start the server using:
```bash
uvx run start
```

The server will be available at `http://0.0.0.0:5000`.

## Usage

- **Authenticate**:
  ```bash
  curl -X POST http://localhost:5000/auth
  ```

- **Execute a KQL Query**:
  ```bash
  curl -X POST http://localhost:5000/execute \
       -H "Content-Type: application/json" \
       -d '{"query": "cluster('\''mycluster'\'').database('\''mydb'\'').MyTable | take 10"}'
  ```

## Integration with Claude Desktop

Configure the server in `claude_desktop_config.json` to enable the `kql_execute` tool in Claude Desktop. See `mcp_config.yaml` for tool details.

## Requirements

- Python 3.9
- Azure CLI (`az`) for authentication
- Dependencies: Flask, waitress, azure-kusto-data, tenacity

## Troubleshooting

- Ensure Azure CLI is authenticated: `az login`
- Check server logs for errors.
- Verify port 5000 is open and accessible.