---
description: "Check project dependencies and environment status"
---

# Check uv Project Status

Perform a comprehensive check of the uv project environment.

## Instructions

Execute the following checks and report results:

1. **Environment Check**
   - Verify uv is installed: `uv --version`
   - Check Python version: `uv run python --version`

2. **Project Configuration**
   - Read and display pyproject.toml summary
   - List installed dependencies: `uv pip list`

3. **Lock File Status**
   - Check if uv.lock exists
   - Run `uv lock --check` to verify lock file is up to date

4. **Dependency Health**
   - Run `uv sync --dry-run` to check for sync issues
   - Report any outdated packages if possible

5. **Development Tools**
   - Check if common dev tools are installed (pytest, ruff, mypy)
   - Suggest installing missing recommended tools

## Report Format

Provide a clear summary with:
- Overall status (healthy / needs attention / issues found)
- List of any issues or warnings
- Recommended actions if problems are detected
