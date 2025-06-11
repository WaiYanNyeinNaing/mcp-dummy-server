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
# Clone or navigate to this directory
cd mcp_dummy

# Create virtual environment with Python 3.10+
python3.10 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
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

### With Cursor

Add to your `/Users/[username]/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "dummy": {
      "command": "python",
      "args": ["/path/to/mcp_dummy/server.py"],
      "cwd": "/path/to/mcp_dummy"
    }
  }
}
```

Or for HTTP mode:
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

1. **Local Script Method**: Point Claude Desktop to your `server.py` file
2. **HTTP Method**: Start the server with `--transport http` and use the URL

### With uv (Recommended)

If you prefer using `uv` for dependency management:
```json
{
  "mcpServers": {
    "dummy": {
      "command": "uv",
      "args": [
        "run",
        "--with", "git+https://github.com/jlowin/fastmcp.git",
        "python",
        "server.py"
      ],
      "cwd": "/path/to/mcp_dummy"
    }
  }
}
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
mcp_dummy/
├── server.py           # Main FastMCP server (supports both transports)
├── client.py           # Test client (supports both connection modes)
├── requirements.txt    # Dependencies (FastMCP from GitHub)
├── README.md          # This file
├── Learning.md        # Educational background on MCP concepts
└── .venv/             # Virtual environment (created during setup)
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