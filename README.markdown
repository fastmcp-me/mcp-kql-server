# 🚀 MCP KQL Server

A Model Context Protocol (MCP) server for executing Kusto Query Language (KQL) queries against Azure Data Explorer clusters. Seamlessly integrates with Claude Desktop and Visual Studio Code (VS Code). Supports Azure CLI authentication and provides a convenient `kql_execute` tool for running queries directly within your AI prompts, complete with optional visualizations.

<<<<<<< HEAD
## ✨ Features
=======
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
>>>>>>> 528f279b22dd0d4e0df0b31cfa1a71ed0e54e6c7

- **🔍 Execute KQL Queries**: Run KQL queries directly within your AI prompts using the `kql_execute` MCP tool.
- **⚡ Plug-and-Play Simplicity**: No manual tenant ID configuration or complex credential management. Simply authenticate via Azure CLI (`az login`) and start querying immediately.
- **🤖 Seamless Claude Integration**: Execute KQL queries within Claude Desktop without switching interfaces or dashboards.
- **🔒 Secure and Efficient**: Leverages Azure CLI’s robust authentication, ensuring secure credential handling and optimized query performance.
- **📊 Visualization Ready**: Optional Markdown table outputs make data analysis intuitive and engaging.
- **🔑 Azure CLI Authentication**: Built-in Azure CLI authentication with retry and caching logic.
- **📡 Protocol Compatibility**: Fully compatible with MCP protocol version `2024-11-05`.
- **🛠️ Reliable Implementation**: Uses `fastmcp` for a robust and reliable MCP server implementation.

<<<<<<< HEAD
### 📌 Comparison with Other Tools
=======
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/4R9UN/mcp-kql-server.git
   ```
>>>>>>> 528f279b22dd0d4e0df0b31cfa1a71ed0e54e6c7

| Feature                      | MCP KQL Server | Azure Data Explorer MCP | Standalone Scripts |
|------------------------------|----------------|-------------------------|--------------------|
| Claude Integration           | ✅             | ❌                      | ❌                 |
| Plug-and-Play Authentication | ✅ (Azure CLI) | ❌ (Manual setup)       | ❌ (Custom code)   |
| No Tenant ID Required        | ✅             | ❌                      | ❌                 |
| Data Visualization           | ✅             | ✅                      | ❌                 |
| Open-Source                  | ✅             | ✅                      | Varies             |

## 📋 Requirements

- Python 3.10 or higher
- Azure Data Explorer cluster access
- Azure CLI installed and authenticated (`az login`)
- Node.js (optional, for Claude Desktop filesystem server)
- VS Code with Claude extension or MCP client (for VS Code integration)

## 📂 Project Structure

```
mcp-kql-server/
├── mcp_kql_server/
│   ├── __init__.py
│   ├── mcp_server.py
│   ├── kql_auth.py
│   └── execute_kql.py
├── claude_desktop_config.json
├── LICENSE
├── pyproject.toml
├── README.md
└── requirements.txt
```

## 🏗️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/4R9UN/mcp-kql-server.git
cd mcp-kql-server
```

### 2️⃣ Install Python 3.10+

- **Windows**:
  ```bash
  winget install Python.Python.3.10
  ```
- **macOS**:
  ```bash
  brew install python@3.10
  ```
- **Linux**:
  ```bash
  sudo apt-get install python3.10
  ```

Verify installation:
```bash
python --version
```

### 3️⃣ Install Azure CLI

- Follow official instructions: [Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- Log in to Azure:
  ```bash
  az config set core.login_experience_v2=off
  az login
  ```

### 4️⃣ Create and Activate Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### 5️⃣ Install Dependencies

```bash
pip install .
```

## 🖥️ Setup for Claude Desktop

- Copy `claude_desktop_config.json` to Claude's configuration directory:
  - **Windows**: `C:\Users\YourUser\AppData\Roaming\Claude\`
  - **macOS**: `/Users/YourUser/Library/Application Support/Claude/`
  - **Linux**: Currently not supported by Claude Desktop.

- Update the configuration file with your Python path and project directory:

```json
{
  "mcpServers": {
    "mcp-kql-server": {
      "command": "C:\\Users\\YourPath\\mcp-kql-server\\.venv\\Scripts\\python.exe",
      "args": [
        "-m",
        "mcp_kql_server.mcp_server"
      ]
    }
  }
}
```

- Optional: Install Node.js for filesystem server support ([Node.js](https://nodejs.org/)).
- Restart Claude Desktop.

## 🖱️ Setup for VS Code

- Install [VS Code](https://code.visualstudio.com/).
- Install the `Copilot MCP` client extension.
- Modify the MCP `settings.json` with the following configuration:

```json
{
  "mcpServers": {
    "mcp-kql-server": {
      "command": "C:\\Users\\YourPath\\mcp-kql-server\\.venv\\Scripts\\python.exe",
      "args": [
        "-m",
        "mcp_kql_server.mcp_server"
      ],
      "env": {
        "PYTHONPATH": "C:\\Users\\YourPath\\mcp-kql-server",
        "PYTHONUNBUFFERED": "1",
        "AZURE_CORE_ONLY_SHOW_ERRORS": "true"
      }
    }
  }
}
```

- Run the `MCP: List Servers` command in VS Code’s Command Palette to verify setup.
- Enable autodiscovery if using Claude Desktop’s configuration.

## ✅ Test the Server

- **Claude Desktop**:
  - Open Claude Desktop and provide the following prompt:
    ```
    Use a tool to execute the attached KQL query, visualize the results, and provide high-level insights from the query output.

    KQL query: "cluster('mycluster').database('mydb').MyTable | take 10"
    ```

## 🤝 Contributing

<<<<<<< HEAD
- Fork the repository.
- Create a feature branch:
  ```bash
  git checkout -b feature/YourFeature
  ```
- Commit your changes:
  ```bash
  git commit -m "Add YourFeature"
  ```
- Push to your branch:
  ```bash
  git push origin feature/YourFeature
  ```
- Open a Pull Request.

## 📬 Contact

For issues or questions, please open a ticket on GitHub or contact the maintainer at [arjuntrivedi42@yahoo.com](mailto:arjuntrivedi42@yahoo.com).

🎉 **Happy Querying!**
=======
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Please open an issue to discuss new features or report bugs.

## 📬 Contact

For questions or support, open an issue on GitHub or contact arjuntrivedi42@yahoo.com.
>>>>>>> 528f279b22dd0d4e0df0b31cfa1a71ed0e54e6c7
