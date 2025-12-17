---
description: "Run mypy type checking"
---

# Run Mypy Type Checking

Execute mypy for static type analysis.

## Instructions

1. Check if mypy is installed in the project (look in pyproject.toml)
2. If not installed, suggest: `uv add --dev mypy`
3. Run mypy with the provided arguments:

### Default (no arguments):
```bash
uv run mypy .
```

### With path argument:
```bash
uv run mypy $ARGUMENTS
```

4. Common options the user might specify:
   - `/uv-typecheck src/` - Check specific directory
   - `/uv-typecheck --strict` - Run in strict mode
   - `/uv-typecheck --ignore-missing-imports` - Ignore missing stubs

5. Analyze the output:
   - Report total number of type errors
   - Group errors by file
   - Explain common type errors and how to fix them
   - Suggest adding type stubs if missing (e.g., `uv add --dev types-requests`)

User arguments: $ARGUMENTS
