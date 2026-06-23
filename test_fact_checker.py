from agents.fact_checker_agent import fact_check_report

sample_report = """
AI reduces healthcare costs by 90%.
AI completely replaces doctors.
"""

result = fact_check_report(sample_report)

print("\nFACT CHECK RESULTS\n")
print(result)