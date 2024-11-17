import ast
import os

def calculate_complexity(project_path):
    complexities = []
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    code = f.read()
                complexities.extend(_analyze_complexity(file_path, code))
    avg_complexity = sum(c['complexity'] for c in complexities) / len(complexities) if complexities else 0
    high_complexity = [c for c in complexities if c['complexity'] > 10]

    return {
        "avg_complexity": round(avg_complexity, 2),
        "high_complexity": high_complexity,
    }

def _analyze_complexity(file_path, code):
    results = []
    try:
        tree = ast.parse(code, filename=file_path)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                complexity = _calculate_function_complexity(node)
                results.append({"function": node.name, "complexity": complexity, "file": file_path})
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
    return results

def _calculate_function_complexity(node):
    complexity = 1
    for child in ast.walk(node):
        if isinstance(child, (ast.If, ast.For, ast.While, ast.And, ast.Or, ast.Try)):
            complexity += 1
    return complexity
