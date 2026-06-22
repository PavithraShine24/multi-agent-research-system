from agents.orchestrator_agent import generate_subtasks

topic = "Impact of AI in Healthcare"

subtasks = generate_subtasks(topic)

print("\nGenerated Subtasks:\n")

for i, task in enumerate(subtasks, start=1):
    print(f"{i}. {task}")