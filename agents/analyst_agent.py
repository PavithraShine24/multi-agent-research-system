from utils.llm import llm

def analyze_research(research_results):
    combined_content = ""

    for item in research_results:
        subtask = item["subtask"]
        sources = item["sources"]

        content = "\n".join(
            source.get("content", "")
            for source in sources
        )

        combined_content += f"""
Subtask: {subtask}

Research Content:
{content}

----------------------------------------
"""

    prompt = f"""
You are an expert research analyst.

Below are findings collected for multiple subtasks.

{combined_content}

For EACH subtask:

- Identify 4 to 6 key insights.
- Focus only on important findings.
- Avoid repetition.
- Clearly separate insights by subtask.

Format:

SUBTASK: <subtask name>

KEY INSIGHTS:
• Insight 1
• Insight 2
• Insight 3
"""

    response = llm.invoke(prompt)

    return response.content