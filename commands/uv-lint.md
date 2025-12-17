---
description: "Run ruff linting and formatting checks"
---

# Run Ruff Linting and Formatting

Execute ruff for code quality checks.

## Instructions

1. Check if ruff is installed in the project (look in pyproject.toml)
2. If not installed, suggest: `uv add --dev ruff`
3. Based on arguments ($ARGUMENTS), run the appropriate command:

### Default (no arguments): Run both check and format check
```bash
uv run ruff check .
uv run ruff format --check .
```

### With arguments:
- `/uv-lint check` - Run linting only
- `/uv-lint format` - Run formatting only (check mode)
- `/uv-lint fix` - Auto-fix linting issues
- `/uv-lint format-fix` - Auto-format code

4. Analyze the output:
   - Report number of issues found
   - Categorize by type (import sorting, unused imports, style, etc.)
   - Suggest fixes for common issues

User arguments: $ARGUMENTS
