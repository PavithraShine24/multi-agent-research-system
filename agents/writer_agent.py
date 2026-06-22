import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)


def write_report(topic, research_results):
    """
    Generate a structured report from research findings.
    """

    research_text = ""

    for result in research_results:
        research_text += f"""
Title: {result['title']}
Content: {result['content']}

"""

    prompt = f"""
You are a professional research report writer.

Topic:
{topic}

Research Findings:
{research_text}

Write a well-structured report with the following sections:

1. Executive Summary
2. Introduction
3. Key Findings
4. Challenges and Limitations
5. Future Outlook
6. Conclusion

Use clear language and bullet points where appropriate.
Do not make up information not present in the findings.
"""

    response = llm.invoke(prompt)

    return response.content