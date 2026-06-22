from agents.orchestrator_agent import generate_subtasks
from agents.research_agent import research_subtasks

topic = "Impact of AI in Healthcare"

subtasks = generate_subtasks(topic)

results = research_subtasks(subtasks)

for section in results:
    print("\n" + "="*60)

    print("\nSUBTASK:")
    print(section["subtask"])

    print("\nSOURCES FOUND:")
    print(len(section["sources"]))