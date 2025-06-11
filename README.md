# FastMCP Dummy Server

A professional, minimal example of a [FastMCP](https://github.com/jlowin/fastmcp) server for learning and experimentation.

**Author:** Dr. Wai Yan Nyein Naing

## ✨ Features

- **Dual Transport Support**: Both STDIO and HTTP transports via command-line arguments
- **Multiple Tools**: `add` and `multiply` operations with comprehensive logging
- **Professional Code**: Type hints, error handling, logging, and documentation
- **Interactive Client**: Test tools manually or run automated tests
- **Easy Integration**: Ready for Cursor, Claude Desktop, and other MCP clients

---

## 🚀 Quick Start

### 1. Prerequisites

- **Python 3.10+** (FastMCP requires Python 3.10 or higher)
- **Git** (for installing FastMCP from GitHub)

### 2. Setup

```bash
# Clone the repository
git clone https://github.com/WaiYanNyeinNaing/mcp-dummy-server.git
cd mcp-dummy-server

# Create virtual environment with Python 3.10+
python3.10 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Optional: Create environment file for configuration
cp env.example .env
# Edit .env with your specific paths
```

### 3. Run the Server

```bash
# STDIO mode (default - for local development and MCP clients)
python server.py

# HTTP mode (for web-based integrations)
python server.py --transport http

# Custom HTTP configuration
python server.py --transport http --port 9000 --host 0.0.0.0
```

### 4. Test with Client

```bash
# Test with STDIO server
python client.py

# Test with HTTP server
python client.py --mode http

# Interactive mode
python client.py --interactive

# Custom test values
python client.py --add-a 10 --add-b 20
```

---

## 📖 Usage Examples

### Server Options

```bash
# Show all options
python server.py --help

# Examples:
python server.py                           # STDIO transport (default)
python server.py -t http                   # HTTP transport
python server.py -t http -p 9000           # HTTP on port 9000
python server.py --verbose                 # Enable debug logging
```

### Client Options

```bash
# Show all options
python client.py --help

# Examples:
python client.py                           # Connect via STDIO
python client.py -m http                   # Connect via HTTP
python client.py -i                       # Interactive mode
python client.py --add-a 15 --add-b 25    # Custom test values
```

### Available Tools

- **`add(a: int, b: int) -> int`**: Add two integers
- **`multiply(a: float, b: float) -> float`**: Multiply two numbers

---

## 🔌 Integration Guide

### With Cursor (Recommended Setup)

Add to your `~/.cursor/mcp.json` or `%APPDATA%\Cursor\User\mcp.json` (Windows):

#### **Method 1: Virtual Environment (Recommended)**
```json
{
  "mcpServers": {
    "dummy": {
      "command": "/absolute/path/to/mcp-dummy-server/.venv/bin/python",
      "args": ["/absolute/path/to/mcp-dummy-server/server.py"],
      "cwd": "/absolute/path/to/mcp-dummy-server"
    }
  }
}
```

#### **Method 2: With Environment Variables**
Create a `.env` file in your project directory:
```bash
# .env
MCP_DUMMY_PATH=/absolute/path/to/mcp-dummy-server
PYTHON_PATH=/absolute/path/to/mcp-dummy-server/.venv/bin/python
```

Then in your `mcp.json`:
```json
{
  "mcpServers": {
    "dummy": {
      "command": "${PYTHON_PATH}",
      "args": ["${MCP_DUMMY_PATH}/server.py"],
      "cwd": "${MCP_DUMMY_PATH}",
      "env": {
        "PYTHONPATH": "${MCP_DUMMY_PATH}"
      }
    }
  }
}
```

#### **Method 3: HTTP Mode**
Start the server first:
```bash
cd /path/to/mcp-dummy-server
source .venv/bin/activate
python server.py --transport http --port 8000
```

Then in `mcp.json`:
```json
{
  "mcpServers": {
    "dummy": {
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

### With Claude Desktop

#### **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
#### **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "dummy": {
      "command": "/absolute/path/to/mcp-dummy-server/.venv/bin/python",
      "args": ["/absolute/path/to/mcp-dummy-server/server.py"],
      "cwd": "/absolute/path/to/mcp-dummy-server"
    }
  }
}
```

### With uv (Modern Python Package Manager)

```json
{
  "mcpServers": {
    "dummy": {
      "command": "uv",
      "args": [
        "run",
        "--python", "3.10",
        "--with", "git+https://github.com/jlowin/fastmcp.git",
        "python",
        "server.py"
      ],
      "cwd": "/absolute/path/to/mcp-dummy-server"
    }
  }
}
```

### Environment Setup Tips

#### **Finding Absolute Paths**
```bash
# Get current directory path
pwd

# Get Python interpreter path
which python

# Or for virtual environment
which .venv/bin/python
```

#### **Windows Paths**
Use forward slashes or escaped backslashes:
```json
{
  "command": "C:/path/to/mcp-dummy-server/.venv/Scripts/python.exe",
  "args": ["C:/path/to/mcp-dummy-server/server.py"],
  "cwd": "C:/path/to/mcp-dummy-server"
}
```

#### **Troubleshooting Path Issues**
```bash
# Test your configuration
cd /your/project/path
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Verify Python version
python --version

# Test server manually
python server.py --verbose
```

---

## 🔧 Troubleshooting

### Common Issues

#### "0 tools enabled" in Cursor
1. **Check Python Version**: Ensure you're using Python 3.10+
   ```bash
   python --version  # Should be 3.10.x or higher
   ```

2. **Verify Installation**: Test the server manually
   ```bash
   python server.py --verbose
   ```

3. **Check Working Directory**: Ensure `cwd` is set correctly in `mcp.json`

4. **Test HTTP Mode**: Try HTTP transport as an alternative
   ```bash
   python server.py --transport http
   # Then update mcp.json to use the HTTP URL
   ```

#### Import Errors
- **FastMCP not found**: Install from GitHub (see requirements.txt)
- **Python version**: FastMCP requires Python 3.10+

#### Connection Issues
- **HTTP mode**: Ensure the server is running before connecting the client
- **Port conflicts**: Use `--port` to specify a different port
- **Firewall**: Check that your firewall allows the specified port

### Debug Mode

Enable verbose logging for detailed information:
```bash
python server.py --verbose
python client.py --verbose
```

### Testing Installation

```bash
# Test server can start
python server.py --help

# Test client can connect (with server running)
python client.py --add-a 1 --add-b 1
```

---

## 📁 File Structure

```
mcp-dummy-server/
├── server.py           # Main FastMCP server (supports both transports)
├── client.py           # Test client (supports both connection modes)
├── requirements.txt    # Dependencies (FastMCP from GitHub)
├── README.md          # This documentation
├── Learning.md        # Educational background on MCP concepts
├── .gitignore         # Git ignore patterns
├── env.example        # Environment variables template (copy to .env)
└── .venv/             # Virtual environment (created during setup)
```

### Environment Configuration

Create a `.env` file for local configuration (copy from `.env.example`):

```bash
# MCP Dummy Server Environment Configuration
# Project paths (use absolute paths)
MCP_DUMMY_PATH=/absolute/path/to/mcp-dummy-server
PYTHON_PATH=/absolute/path/to/mcp-dummy-server/.venv/bin/python

# Server configuration
MCP_HOST=127.0.0.1
MCP_PORT=8000
MCP_LOG_LEVEL=INFO

# Windows example:
# MCP_DUMMY_PATH=C:/path/to/mcp-dummy-server
# PYTHON_PATH=C:/path/to/mcp-dummy-server/.venv/Scripts/python.exe
```

---

## 🎓 Learning Resources

- **[Learning.md](Learning.md)**: Beginner-friendly explanation of MCP concepts
- **[FastMCP Documentation](https://github.com/jlowin/fastmcp)**: Official FastMCP documentation
- **[MCP Specification](https://spec.modelcontextprotocol.io/)**: Model Context Protocol specification

---

## 💡 Next Steps

Once you have this working:

1. **Add more tools**: Extend `server.py` with additional `@mcp.tool` functions
2. **Add resources**: Use `@mcp.resource` for providing static or dynamic data
3. **Add authentication**: Implement bearer token authentication for production use
4. **Deploy to production**: Use the HTTP mode for web-based integrations

---

## 👨‍⚕️ Author

**Dr. Wai Yan Nyein Naing**  
*Learning and experimenting with the Model Context Protocol ecosystem*

---

**Happy coding with FastMCP! 🚀** 