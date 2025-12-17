# cc-uv-plugin

Claude Code plugin optimized for Python development with uv.

## Overview

This plugin provides seamless integration between Claude Code and uv (the fast Python package manager). It includes:

- **Custom slash commands** for common uv operations
- **Session hooks** for automatic environment setup
- **MCP server** for advanced uv tool integration

## Available Commands

| Command | Description |
|---------|-------------|
| `/uv-init` | Initialize a new uv project with pyproject.toml |
| `/uv-add` | Add dependencies to the project |
| `/uv-test` | Run tests using pytest via uv |
| `/uv-run` | Execute any command in the uv environment |
| `/uv-check` | Check project dependencies and environment |

## Project Structure

```
.claude/
├── CLAUDE.md           # This file
├── commands/           # Slash command definitions
│   ├── uv-init.md
│   ├── uv-add.md
│   ├── uv-test.md
│   ├── uv-run.md
│   └── uv-check.md
├── hooks/              # Hook scripts
│   └── session-init.sh
└── settings.json       # Hook configuration
mcp/
├── server.py           # MCP server implementation
└── tools/              # Tool implementations
    └── uv_tools.py
```

## uv Best Practices

When working with uv in this project:

1. **Always use `uv run`** to execute Python scripts and commands
2. **Use `uv add`** instead of `pip install` for dependencies
3. **Check `uv.lock`** for reproducible builds
4. **Use `uv sync`** to synchronize the environment with pyproject.toml

## Common Workflows

### Starting a new project
```bash
uv init
uv add <dependencies>
uv run python main.py
```

### Adding development dependencies
```bash
uv add --dev pytest ruff mypy
```

### Running tests
```bash
uv run pytest
uv run pytest --cov
```

### Type checking and linting
```bash
uv run mypy .
uv run ruff check .
uv run ruff format .
```
