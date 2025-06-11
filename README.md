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
> "You're buying carpet for a rectangular room that's 14 feet by 11 feet. The carpet costs $4.25 per square foot. How much will the carpet cost, and if there's a 7.5% sales tax, what's your total cost?"

**How the LLM solves it with MCP tools:**
1. Calls the `multiply` tool to compute the area: 14 × 11 = 154
2. Calls the `multiply` tool to get the carpet cost: 154 × 4.25 = 654.50
3. Calls the `percentage` tool to get the sales tax: 7.5% of 654.50 = 49.09
4. Calls the `add` tool to get the total: 654.50 + 49.09 = 703.59

**Final answer:**
```
Carpet cost (before tax): $654.50
Sales tax: $49.09
Total cost: $703.59
```

**Benefit:**
> By leveraging the MCP server's calculation tools, LLMs can solve real-world math and reasoning problems accurately, even for decimal and multi-step questions.

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

---

**Author:** Dr. Wai Yan Nyein Naing 