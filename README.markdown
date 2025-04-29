# 🚀 MCP KQL Server

💡 **Purpose**: The MCP KQL Server enables seamless execution of KQL (Kusto Query Language) queries against Azure Data Explorer directly within Claude Desktop. It leverages Azure CLI for secure authentication and returns results in a structured table format, making data analytics accessible without leaving your Claude workflow.

Are you a data analyst or developer looking to streamline your Azure Data Explorer workflows without leaving Claude? We’re thrilled to announce the release of **MCP KQL Server**, a groundbreaking tool that brings KQL (Kusto Query Language) query execution directly into your Claude Desktop environment.

### Why MCP KQL Server Stands Out

In a world of complex data analytics tools, MCP KQL Server offers a refreshing, user-centric approach. Here’s what sets it apart:

- **Plug-and-Play Simplicity**: Unlike other tools that require manual configuration of tenant IDs or complex credential management, MCP KQL Server uses Azure CLI authentication. Just run `az login`, and you’re ready to query—no fuss, no hassle.
- **Seamless Claude Integration**: Execute KQL queries within Claude, keeping your workflow uninterrupted. No need to switch to separate interfaces or dashboards.
- **Secure and Efficient**: Built with security in mind, it leverages Azure CLI’s robust authentication, ensuring your credentials remain safe. Optimized for performance, it delivers query results quickly in a structured table format.
- **Visualization Ready**: With optional Markdown table output, results are presented clearly, making data analysis intuitive and engaging.

### Key Features

- **Effortless Query Execution**: Run KQL queries against Azure Data Explorer with a single command in Claude.
- **Secure Authentication**: Uses Azure CLI, eliminating the need to expose sensitive information.
- **Structured Results**: Returns query results in a table format (columns, rows, row_count) for easy analysis.
- **Data Visualization**: Enable Markdown tables for beautifully formatted output in Claude.

### How It Compares to Other Tools

Compared to traditional KQL query tools like Azure Data Explorer’s web UI or standalone Python scripts, MCP KQL Server offers unmatched integration and ease of use:

| Feature                     | MCP KQL Server | Azure Data Explorer UI | Standalone Scripts |
|-----------------------------|----------------|------------------------|--------------------|
| Claude Integration          | ✅             | ❌                     | ❌                 |
| Plug-and-Play Authentication| ✅ (Azure CLI) | ❌ (Manual setup)      | ❌ (Custom code)   |
| No Tenant ID Required       | ✅             | ❌                     | ❌                 |
| Data Visualization          | ✅ (Markdown)  | ✅ (Web-based)         | ❌                 |
| Open-Source                 | ✅             | ❌                     | Varies            |

MCP KQL Server eliminates the need for context-switching, making it ideal for users who live in Claude and need quick access to Azure Data Explorer insights.


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

## 📬 Contact

For questions or support, open an issue on GitHub or contact [your email or preferred contact method].
