from utils.visualizer import create_charts

def generate_report(metrics, complexity, dead_code):
    print("Generating report...")
    report = f"""
    === Project Metrics ===
    Total Files: {metrics['total_files']}
    Total Lines: {metrics['total_lines']}
    Code Lines: {metrics['code_lines']}
    Comment Lines: {metrics['comment_lines']}
    
    === Complexity Analysis ===
    Average Complexity: {complexity['avg_complexity']}
    High Complexity Functions: {complexity['high_complexity']}
    
    === Dead Code ===
    Dead Functions Found: {len(dead_code)}
    """

    with open("report.txt", "w") as f:
        f.write(report)
    create_charts(metrics, complexity)
    print("Report saved as report.txt")
