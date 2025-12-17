# cc-uv-plugin

Claude Code plugin optimized for Python development with [uv](https://github.com/astral-sh/uv).

## Features

- **Slash Commands**: Quick access to common uv operations
- **Session Hooks**: Automatic environment initialization
- **MCP Server**: Full uv tool integration for Claude Code

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/your-username/cc-uv-plugin.git
cd cc-uv-plugin
```

### 2. Set up the plugin

Copy the `.claude` directory to your project:

```bash
cp -r .claude /path/to/your/project/
```

Or symlink it for global use:

```bash
ln -s $(pwd)/.claude ~/.claude
```

### 3. (Optional) Install the MCP Server

For advanced uv tool integration:

```bash
cd mcp
uv sync
```

Then add to your Claude Code settings (`~/.config/claude/settings.json`):

```json
{
  "mcpServers": {
    "uv-tools": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/cc-uv-plugin/mcp", "python", "server.py"]
    }
  }
}
```

## Available Slash Commands

| Command | Description |
|---------|-------------|
| `/uv-init [name]` | Initialize a new uv Python project |
| `/uv-add <packages>` | Add dependencies (use `--dev` for dev deps) |
| `/uv-test [args]` | Run pytest tests via uv |
| `/uv-run <command>` | Execute any command in the uv environment |
| `/uv-check` | Check project dependencies and environment |

### Examples

```
/uv-init my-project
/uv-add requests httpx
/uv-add --dev pytest ruff mypy
/uv-test -v
/uv-run python main.py
/uv-check
```

## MCP Server Tools

When the MCP server is enabled, Claude Code gains access to these tools:

| Tool | Description |
|------|-------------|
| `uv_init` | Initialize a new Python project |
| `uv_add` | Add dependencies |
| `uv_remove` | Remove dependencies |
| `uv_sync` | Sync environment with pyproject.toml |
| `uv_run` | Run commands in the environment |
| `uv_pip_list` | List installed packages |
| `uv_lock` | Manage lock file |
| `uv_python_install` | Install Python versions |
| `uv_python_list` | List available Python versions |
| `uv_version` | Get uv version |

## Session Hook

The plugin includes a session initialization hook that:

1. Checks if uv is installed
2. Detects if the current directory is a uv project
3. Automatically syncs dependencies if needed
4. Reports environment status at session start

## Project Structure

```
cc-uv-plugin/
├── README.md
├── .claude/
│   ├── CLAUDE.md           # Project context for Claude
│   ├── commands/           # Slash command definitions
│   │   ├── uv-init.md
│   │   ├── uv-add.md
│   │   ├── uv-test.md
│   │   ├── uv-run.md
│   │   └── uv-check.md
│   ├── hooks/              # Hook scripts
│   │   └── session-init.sh
│   └── settings.json       # Hook configuration
└── mcp/
    ├── server.py           # MCP server implementation
    └── pyproject.toml      # MCP server dependencies
```

## Requirements

- [uv](https://github.com/astral-sh/uv) installed on your system
- [Claude Code](https://claude.ai/code) CLI

### Installing uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## License

MIT
