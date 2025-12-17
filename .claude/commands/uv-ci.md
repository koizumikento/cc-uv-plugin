---
description: "Run all CI checks (ruff, mypy, pytest)"
---

# Run All CI Checks

Execute the complete CI pipeline: linting, type checking, and tests.

## Instructions

Run all checks in sequence and provide a comprehensive report:

### 1. Ruff Linting
```bash
uv run ruff check .
```

### 2. Ruff Format Check
```bash
uv run ruff format --check .
```

### 3. Mypy Type Checking
```bash
uv run mypy .
```

### 4. Pytest Tests
```bash
uv run pytest
```

## Report Format

After running all checks, provide a summary:

```
CI Results Summary
==================
Ruff Lint:    PASS/FAIL (X issues)
Ruff Format:  PASS/FAIL (X files need formatting)
Mypy:         PASS/FAIL (X type errors)
Pytest:       PASS/FAIL (X passed, Y failed, Z skipped)

Overall: PASS/FAIL
```

## Missing Dependencies

If any tool is not installed, report which ones are missing and suggest:
```bash
uv add --dev ruff mypy pytest
```

## Options

- `/uv-ci --fix` - Attempt to auto-fix issues (ruff fix + format)
- `/uv-ci --fast` - Skip slow checks (only ruff + pytest, no mypy)

User arguments: $ARGUMENTS
