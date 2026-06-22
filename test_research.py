from agents.research_agent import research_topic

topic = "Impact of AI in Healthcare"

results = research_topic(topic)

for i, result in enumerate(results, start=1):
    print(f"\nSource {i}")
    print("Title:", result["title"])
    print("URL:", result["url"])
    print("Content:", result["content"][:300])