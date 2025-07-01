# Contributing to MCP KQL Server

> **Welcome Contributors!** 🎉

Thank you for your interest in contributing to the MCP KQL Server project. This guide will help you get started with contributing to our AI-powered KQL query execution system.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Guidelines](#contributing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)
- [Code Style](#code-style)
- [Documentation](#documentation)
- [Community](#community)

## 🤝 Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Azure CLI installed and authenticated (`az login`)
- Git for version control
- Access to Azure Data Explorer cluster(s) for testing

### Quick Start

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/mcp-kql-server.git
   cd mcp-kql-server
   ```

3. **Set up development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements-dev.txt
   ```

4. **Verify installation**:
   ```bash
   python -c "from mcp_kql_server import __version__; print(f'MCP KQL Server v{__version__} ready for development!')"
   ```

## 🛠️ Development Setup

### Environment Configuration

1. **Create a `.env` file** (optional):
   ```bash
   # Optional: Enable debug mode
   KQL_DEBUG=true
   
   # Optional: Custom memory path for testing
   KQL_MEMORY_PATH=/path/to/test/memory
   ```

2. **Authenticate with Azure**:
   ```bash
   az login
   ```

3. **Install pre-commit hooks** (recommended):
   ```bash
   pre-commit install
   ```

### Project Structure

```
mcp-kql-server/
├── mcp_kql_server/          # Main package
│   ├── __init__.py          # Package initialization with author info
│   ├── mcp_server.py        # FastMCP server implementation
│   ├── execute_kql.py       # KQL query execution logic
│   ├── schema_memory.py     # Schema caching and discovery
│   ├── unified_memory.py    # Advanced memory management
│   ├── kql_auth.py          # Azure authentication
│   ├── utils.py             # Utility functions
│   └── constants.py         # Configuration constants
├── docs/                    # Documentation
├── tests/                   # Test suite (create if contributing tests)
├── .github/workflows/       # CI/CD pipelines
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
└── pyproject.toml          # Project configuration
```

## 📝 Contributing Guidelines

### Types of Contributions

We welcome the following types of contributions:

- 🐛 **Bug Reports**: Help us identify and fix issues
- 💡 **Feature Requests**: Suggest new functionality
- 🔧 **Bug Fixes**: Submit fixes for identified issues
- ✨ **New Features**: Implement new capabilities
- 📚 **Documentation**: Improve or add documentation
- 🧪 **Tests**: Add or improve test coverage
- 🎨 **Code Quality**: Refactoring and optimization

### Before You Start

1. **Check existing issues** to see if your contribution is already being discussed
2. **Open an issue** to discuss major changes before implementation
3. **Follow the coding standards** outlined below
4. **Ensure all tests pass** before submitting

### Author Attribution

All new files should include the following header:

```python
"""
[File Description]

[Detailed description of the file's purpose and functionality]

Author: Arjun Trivedi
Email: arjuntrivedi42@yahoo.com
"""
```

## 🔄 Pull Request Process

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-number-description
```

### 2. Make Your Changes

- Follow the coding standards
- Add tests for new functionality
- Update documentation as needed
- Ensure your changes don't break existing functionality

### 3. Test Your Changes

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=mcp_kql_server --cov-report=html

# Run linting
flake8 mcp_kql_server/
black --check mcp_kql_server/
isort --check-only mcp_kql_server/

# Run security scan
bandit -r mcp_kql_server/
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "feat: add new feature description"
# or
git commit -m "fix: resolve issue with specific component"
```

Use conventional commit messages:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for adding tests
- `refactor:` for code refactoring
- `style:` for formatting changes
- `ci:` for CI/CD changes

### 5. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:
- Clear title and description
- Reference to related issues
- Screenshots/examples if applicable
- Checklist of changes made

### 6. Code Review Process

- All PRs require review from maintainers
- Address feedback promptly
- Keep PRs focused and reasonably sized
- Ensure CI/CD pipeline passes

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_execute_kql.py

# Run with coverage
pytest --cov=mcp_kql_server --cov-report=term-missing

# Run integration tests (requires Azure access)
pytest -m integration
```

### Writing Tests

- Write tests for all new functionality
- Use descriptive test names
- Include both positive and negative test cases
- Mock external dependencies when possible

Example test structure:
```python
"""
Test module for [component name].

Author: Arjun Trivedi
Email: arjuntrivedi42@yahoo.com
"""

import pytest
from mcp_kql_server.component import function_to_test

def test_function_success_case():
    """Test successful execution of function."""
    # Arrange
    input_data = "test_input"
    
    # Act
    result = function_to_test(input_data)
    
    # Assert
    assert result == expected_output

def test_function_error_case():
    """Test error handling in function."""
    with pytest.raises(ValueError):
        function_to_test(invalid_input)
```

## 🎨 Code Style

### Python Code Standards

- **Formatting**: Use `black` for code formatting
- **Import sorting**: Use `isort` for import organization
- **Linting**: Follow `flake8` guidelines
- **Type hints**: Use type annotations where appropriate
- **Docstrings**: Follow Google-style docstrings

### Code Quality Checks

```bash
# Format code
black mcp_kql_server/
isort mcp_kql_server/

# Check formatting
black --check mcp_kql_server/
isort --check-only mcp_kql_server/

# Lint code
flake8 mcp_kql_server/

# Type checking
mypy mcp_kql_server/

# Security scanning
bandit -r mcp_kql_server/
```

### Documentation Standards

- Clear and concise descriptions
- Include examples where helpful
- Update README.md for significant changes
- Document new configuration options
- Include type information in docstrings

## 📚 Documentation

### Building Documentation

```bash
# Install documentation dependencies
pip install -r requirements-dev.txt

# Build documentation (if Sphinx is set up)
cd docs
make html
```

### Documentation Guidelines

- Use clear, descriptive language
- Include code examples
- Keep documentation up-to-date with code changes
- Use proper markdown formatting
- Include screenshots for UI changes

## 🌟 Community

### Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and community discussions
- **Email**: Contact [arjuntrivedi42@yahoo.com](mailto:arjuntrivedi42@yahoo.com) for direct communication

### Recognition

Contributors will be:
- Listed in the project's contributor section
- Credited in release notes for significant contributions
- Invited to join the maintainer team for exceptional ongoing contributions

## 📄 License

By contributing to MCP KQL Server, you agree that your contributions will be licensed under the same [MIT License](LICENSE) that covers the project.

## 🙏 Thank You

Thank you for contributing to MCP KQL Server! Your efforts help make this project better for everyone in the data analytics and AI community.

---

**Happy Coding! 🚀**

*For questions about contributing, please open an issue or contact the maintainers.*