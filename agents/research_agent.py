import os
from dotenv import load_dotenv
from tavily import TavilyClient

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