import os
import re

def find_dead_code(project_path):
    all_functions = set()
    all_references = set()

    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    code = f.read()
                all_functions.update(_find_functions(code))
                all_references.update(_find_references(code))

    dead_code = all_functions - all_references
    return list(dead_code)

def _find_functions(code):
    return set(re.findall(r'def (\w+)\(', code))

def _find_references(code):
    return set(re.findall(r'(\w+)\(', code))
