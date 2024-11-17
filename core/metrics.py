import os

def calculate_metrics(project_path):
    metrics = {
        "total_files": 0,
        "total_lines": 0,
        "comment_lines": 0,
        "code_lines": 0
    }
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith(".py"):
                metrics["total_files"] += 1
                with open(os.path.join(root, file), "r") as f:
                    lines = f.readlines()
                    metrics["total_lines"] += len(lines)
                    metrics["comment_lines"] += sum(1 for line in lines if line.strip().startswith("#"))
                    metrics["code_lines"] += sum(1 for line in lines if line.strip() and not line.strip().startswith("#"))
    return metrics
