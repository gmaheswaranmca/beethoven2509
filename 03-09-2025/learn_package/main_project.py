# Outside 'project', e.g., in main.py
from project.module_a import func_a
from project.utils.helper import helper_func
from project.data.loader import load_data

print(func_a())         # Output: Function A from module_a
print(helper_func())    # Output: Helper function from utils.helper
print(load_data())      # Output: Parsed: raw data