---
description: "Run pytest tests using uv"
---

# Run Tests with uv

Execute the test suite using pytest through uv.

## Instructions

1. Check if pytest is installed (look in pyproject.toml dependencies)
2. If pytest is not installed, ask if the user wants to add it with `uv add --dev pytest`
3. Run the tests with `uv run pytest $ARGUMENTS`
4. If no arguments provided, run with verbose output: `uv run pytest -v`
5. Analyze test results and provide a summary:
   - Number of passed/failed/skipped tests
   - If failures occurred, explain what went wrong
   - Suggest fixes for failing tests

## Additional options the user might specify

- Specific test file: `/uv-test tests/test_main.py`
- Specific test function: `/uv-test tests/test_main.py::test_function`
- With coverage: `/uv-test --cov`
- Stop on first failure: `/uv-test -x`

User arguments: $ARGUMENTS
