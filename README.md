# Simple MCP Server

**Author:** Dr. Wai Yan Nyein Naing

A simple example of an MCP server for beginners.

## Quick Start

### 1. Install

```bash
# Clone the repository
git clone https://github.com/WaiYanNyeinNaing/mcp-dummy-server.git
cd mcp-dummy-server

# Create virtual environment
python3.10 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Test

**Option 1: Start server first (recommended for learning)**
```bash
# Terminal 1: Start the server
python server.py

# Terminal 2: Run the client
python client.py
```

**Option 2: Auto-start (client starts server automatically)**
```bash
# Client automatically starts the server
python client.py
```

#### Example: Reasoning Calculation with LLM + MCP Tool

Suppose you ask an LLM:
> "A watch costs $212,320 and is on sale for 23% off. How much do I need to pay?"

**How the LLM solves it with MCP tools:**
1. Calls the `multiply` tool to compute the discount: 212320 × 0.23 = 48833.6
2. Calls the `add` tool to subtract the discount: 212320 - 48833.6 = 163486.4

**Final answer:**
```
You need to pay $163,486.40 after the 23% discount.
```

**Benefit:**
> By leveraging the MCP server's calculation tools, LLMs can solve real-world math and reasoning problems accurately, even for complex or multi-step questions.

## Integration

### Cursor

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "dummy": {
      "command": "/path/to/.venv/bin/python",
      "args": ["/path/to/server.py"],
      "cwd": "/path/to/mcp-dummy-server"
    }
  }
}
```

### VS Code

Create `.vscode/mcp.json`:

```json
{
  "servers": {
    "dummy": {
      "command": "/path/to/.venv/bin/python",
      "args": ["/path/to/server.py"],
      "cwd": "/path/to/mcp-dummy-server"
    }
  }
}
```

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "dummy": {
      "command": "/path/to/.venv/bin/python",
      "args": ["/path/to/server.py"],
      "cwd": "/path/to/mcp-dummy-server"
    }
  }
}
```

## Files

- `server.py` - The MCP server
- `client.py` - Test client  
- `requirements.txt` - Dependencies

## Tools

- `add(a, b)` - Add two numbers
- `multiply(a, b)` - Multiply two numbers

---

**Author:** Dr. Wai Yan Nyein Naing 