from agents.research_agent import research_topic
from agents.writer_agent import write_report

topic = "Impact of AI in Healthcare"

print("Researching...\n")

research_results = research_topic(topic)

print("Writing report...\n")

report = write_report(topic, research_results)

print(report)