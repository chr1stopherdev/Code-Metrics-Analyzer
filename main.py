from core.metrics import calculate_metrics
from core.complexity import calculate_complexity
from core.dead_code import find_dead_code
from core.report_generator import generate_report

def main():
    project_path = input("Enter the path to your project: ")
    print("Analyzing project...")

    metrics = calculate_metrics(project_path)
    complexity = calculate_complexity(project_path)
    dead_code = find_dead_code(project_path)

    generate_report(metrics, complexity, dead_code)
    print("Analysis complete! Report generated.")

if __name__ == "__main__":
    main()
