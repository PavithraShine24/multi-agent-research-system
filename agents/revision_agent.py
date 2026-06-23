from utils.llm import llm

def revise_report(report, fact_check):
    prompt = f"""
You are an expert editor.

Original Report:
{report}

Fact Checker Feedback:
{fact_check}

Revise the report by:
- Fixing unsupported claims.
- Softening exaggerated statements.
- Adding necessary clarifications.
- Keeping the same structure.
- Do NOT invent citations.

Return only the revised report.
"""

    response = llm.invoke(prompt)

    return response.content