import os
from dotenv import load_dotenv
from tavily import TavilyClient
from concurrent.futures import ThreadPoolExecutor

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def research_topic(topic: str):
    """
    Search the web and return relevant results.
    """

    results = tavily.search(
        query=topic,
        search_depth="advanced",
        max_results=5
    )

    return results["results"]

def research_subtasks(subtasks):
    all_results = []

    def process_task(task):
        print(f"\n🔍 Researching: {task}")

        results = research_topic(task)

        return {
            "subtask": task,
            "sources": results
        }

    with ThreadPoolExecutor(max_workers=5) as executor:
        all_results = list(executor.map(process_task, subtasks))

    return all_results