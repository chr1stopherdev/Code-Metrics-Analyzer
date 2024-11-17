import matplotlib.pyplot as plt

def create_charts(metrics, complexity):
    labels = ['Code Lines', 'Comment Lines']
    sizes = [metrics['code_lines'], metrics['comment_lines']]

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Code vs Comments')
    plt.savefig('code_comments_pie.png')
    print("Saved pie chart: code_comments_pie.png")

    complexities = [c['complexity'] for c in complexity['high_complexity']]
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(complexities)), complexities)
    plt.title('High Complexity Functions')
    plt.xlabel('Function Index')
    plt.ylabel('Cyclomatic Complexity')
    plt.savefig('complexity_histogram.png')
    print("Saved histogram: complexity_histogram.png")
