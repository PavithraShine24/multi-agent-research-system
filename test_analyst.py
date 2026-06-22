from agents.orchestrator_agent import generate_subtasks
from agents.research_agent import research_subtasks
from agents.analyst_agent import analyze_research

topic = "Impact of AI in Healthcare"

print("🧠 Generating subtasks...")
subtasks = generate_subtasks(topic)

print("\n🔍 Researching subtasks...")
research = research_subtasks(subtasks)

print("\n📊 Analyzing research...")
analysis = analyze_research(research)

for section in analysis:
    print("\n" + "=" * 60)

    print("\nSUBTASK:")
    print(section["subtask"])

    print("\nKEY INSIGHTS:")
    print(section["analysis"])