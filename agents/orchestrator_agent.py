import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.llm import llm

load_dotenv()




def generate_subtasks(topic):
    """
    Break a broad topic into 4–6 research subtasks.
    """

    prompt = f"""
You are a research planner.

Topic:
{topic}

Generate 4 to 6 research subtasks.

Rules:
- Each subtask should focus on one aspect.
- Keep them concise.
- Return ONLY the subtasks.
- One subtask per line.
"""

    response = llm.invoke(prompt)

    subtasks = [
        line.strip("-•123456789. ").strip()
        for line in response.content.split("\n")
        if line.strip()
    ]

    return subtasks