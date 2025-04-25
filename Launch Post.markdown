## 🚀 Launching MCP KQL Server: Seamless KQL Queries in Claude

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

### Get Started Today

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/mcp-kql-server.git
   ```

2. **Install Dependencies**:
   ```bash
   cd mcp-kql-server
   pip install -e .
   ```

3. **Authenticate with Azure**:
   ```bash
   az login
   ```

4. **Configure Claude**:
   - Add `claude_desktop_config.json` to your Claude configuration directory.

5. **Execute Queries**:
   - Use the `kql_execute` tool in Claude to run queries like `cluster('mycluster').database('mydb').MyTable | take 10`.

### Join the Community

🌟 **Try MCP KQL Server today** and experience data analytics like never before, right within Claude!

[GitHub Repository](https://github.com/yourusername/mcp-kql-server)
