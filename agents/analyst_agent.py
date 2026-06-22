from utils.llm import llm

def analyze_research(research_results):
    analyses = []

    for item in research_results:
        subtask = item["subtask"]
        sources = item["sources"]

        # Combine source contents
        content = "\n".join(
            source.get("content", "")
            for source in sources
        )

        prompt = f"""
You are an expert research analyst.

Subtask:
{subtask}

Research Content:
{content}

Extract the most important insights.

Return:
- 4 to 6 concise bullet points
- Focus only on important findings
- Avoid repetition
"""

        response = llm.invoke(prompt)

        analyses.append({
            "subtask": subtask,
            "analysis": response.content
        })

    return analyses