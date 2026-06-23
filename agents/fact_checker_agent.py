from utils.llm import llm

def fact_check_report(report):
    prompt = f"""
You are an expert fact-checking agent.

Review the following report.

Check for:
1. Unsupported claims
2. Contradictions
3. Exaggerated statements
4. Misleading statistics
5. Areas needing clarification

For each issue:
- Quote the statement
- Explain the concern
- Suggest a correction

If no major issues are found, say:
"No major factual concerns detected."

REPORT:
{report}
"""

    response = llm.invoke(prompt)

    return response.content