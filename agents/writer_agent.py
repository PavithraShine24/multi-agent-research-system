from utils.llm import llm

def write_report(topic, analyses):

    prompt = f"""
You are a professional report writer.

Write a comprehensive report on:

TOPIC:
{topic}

Use the following analyzed insights:

{analyses}

The report should contain:

1. Executive Summary
2. Introduction
3. Main Findings
4. Challenges and Limitations
5. Future Outlook
6. Conclusion

Write in a professional and well-structured manner.
"""

    response = llm.invoke(prompt)

    return response.content