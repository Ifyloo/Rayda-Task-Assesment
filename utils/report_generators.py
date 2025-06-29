# utils/report_generators.py

def generate_test_report(results):
    with open("test_report.txt", "w") as f:
        f.write("Test Results:\n")
        for result in results:
            f.write(f"{result}\\n")

