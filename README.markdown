# 🚀 MCP KQL Server

💡 **Purpose**: The MCP KQL Server enables seamless execution of KQL (Kusto Query Language) queries against Azure Data Explorer directly within Claude Desktop. It leverages Azure CLI for secure authentication and returns results in a structured table format, making data analytics accessible without leaving your Claude workflow.

🔧 **Features**:
- **Seamless Claude Integration**: Execute KQL queries within Claude, enhancing productivity.
- **Secure Authentication**: Uses Azure CLI for authentication, eliminating the need to manage sensitive credentials like tenant IDs.
- **Structured Output**: Returns query results in a table format (columns, rows, row_count) for easy analysis.
- **Data Visualization**: Optional Markdown table output for better readability in Claude.
- **Efficient and Lightweight**: Optimized for performance with robust error handling.

## 🏗️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/mcp-kql-server.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd mcp-kql-server
   ```

3. **Create a Virtual Environment** (recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Linux/Mac
   ```

4. **Install Dependencies**:
   ```bash
   pip install -e .
   ```

## ⚙️ Setup

1. **Install Azure CLI**:
   - Download and install Azure CLI from [Azure CLI Installation](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
   - Authenticate with Azure:
     ```bash
     az login
     ```

2. **Configure Claude Desktop**:
   - Copy `claude_desktop_config.json` to your Claude configuration directory (consult Claude Desktop documentation for the exact path, e.g., `%APPDATA%\Claude`).
   - The configuration should look like:
     ```json
     {
       "mcpServers": {
         "mcp-kql-server": {
           "command": "C:\\Users\\YourUsername\\mcp-kql-server\\.venv\\Scripts\\python.exe",
           "args": [
             "-m",
             "mcp_kql_server.mcp_server"
           ]
         }
       }
     }
     ```
   - Update the `command` path to match your virtual environment’s Python executable.

3. **Test the Server**:
   - Run the server manually:
     ```bash
     python -m mcp_kql_server.mcp_server
     ```
   - In Claude Desktop, use the `kql_execute` tool to run a query, e.g., `cluster('mycluster').database('mydb').MyTable | take 10`.

## 📋 Requirements

| Requirement         | Version/Description                     |
|---------------------|-----------------------------------------|
| Python              | 3.10 or higher                         |
| Azure CLI           | Latest version                         |
| Dependencies        | Listed in `pyproject.toml`             |

## 🔍 Tools

### kql_execute
- **Description**: Executes a KQL query against an Azure Data Explorer cluster.
- **Input**:
  - `query` (str): The KQL query to execute (e.g., `cluster('mycluster').database('mydb').MyTable | take 10`).
  - `visualize` (bool, optional): If true, includes a Markdown table visualization.
- **Output**:
  - `status` (str): "success" or "error".
  - `result` (dict): If successful, contains:
    - `columns` (list): Column names.
    - `rows` (list): Query result rows.
    - `row_count` (int): Number of rows.
    - `visualization` (str, optional): Markdown table if `visualize` is true.
  - `error` (str): Error message if failed.

**Example**:
```json
{
  "query": "cluster('mycluster').database('mydb').MyTable | take 10",
  "visualize": true
}
```

## 🌟 Additional Features

- **Data Visualization**: Query results can be formatted as Markdown tables for better readability in Claude, enabled by setting `visualize: true` in the input.
- **Future Enhancements**:
  - **Query Caching**: Implement caching for frequently executed queries using `functools.lru_cache` to improve performance.
  - **Query Validation**: Add client-side validation to catch syntax errors before execution.
  - **Advanced Visualization**: Integrate libraries like `plotly` for graphical outputs (e.g., charts) in Claude.

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Please open an issue to discuss new features or report bugs.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions or support, open an issue on GitHub or contact [your email or preferred contact method].