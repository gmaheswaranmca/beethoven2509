from .module_a import func_a  # Sibling import

def func_b():
    return f"Function B and {func_a()}"