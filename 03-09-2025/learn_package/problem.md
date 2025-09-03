## Problem: Organizing and Importing Modules in a Multi-Level Python Package

### Scenario

You are developing a Python package named `analytics` with the following directory structure:

```
analytics/
    __init__.py
    core/
        __init__.py
        processor.py
        validator.py
    io/
        __init__.py
        reader.py
        writer.py
    tools/
        __init__.py
        formatter.py
```

### Requirements

1. **Module Implementation:**
    - In `core/processor.py`, implement a function `process_data(data)` that returns `"Processed: <data>"`.
    - In `core/validator.py`, implement a function `validate_data(data)` that returns `True` if `data` is not empty, else `False`.
    - In `io/reader.py`, implement a function `read_data()` that returns `"sample data"`.
    - In `io/writer.py`, implement a function `write_data(data)` that returns `"Written: <data>"`.
    - In `tools/formatter.py`, implement a function `format_data(data)` that returns `"**<data>**"`.

2. **Module Imports:**
    - In `core/processor.py`, import and use `validate_data` from its sibling module.
    - In `io/writer.py`, import and use `format_data` from the `tools` subpackage.

3. **Package Initialization:**
    - In each `__init__.py`, expose the relevant modules using `__all__`.

4. **Usage Example:**
    - Show how to use `read_data`, `process_data`, `write_data`, and `format_data` from outside the package (e.g., in `main.py`).

### Notes

- Use relative imports for sibling and parent modules within the package.
- Use absolute imports when accessing modules from outside the package.
- Ensure each module is independently testable and reusable.
- Properly structure `__init__.py` files to facilitate clean imports.