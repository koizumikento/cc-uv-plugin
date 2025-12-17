---
description: "Execute a command in the uv environment"
---

# Run Command with uv

Execute any command within the uv-managed Python environment.

## Instructions

1. Run the command using `uv run $ARGUMENTS`
2. If no arguments provided, show helpful usage examples
3. Capture and display the output
4. If the command fails:
   - Check if required dependencies are missing
   - Suggest installing missing packages with `uv add`
   - Explain any error messages

## Common usage examples

- Run a Python script: `/uv-run python main.py`
- Run a module: `/uv-run python -m http.server`
- Run linting: `/uv-run ruff check .`
- Run type checking: `/uv-run mypy .`
- Run formatting: `/uv-run ruff format .`
- Interactive Python: `/uv-run python`

User arguments: $ARGUMENTS
