from agents.orchestrator_agent import generate_subtasks
from agents.research_agent import research_subtasks
from agents.analyst_agent import analyze_research
from agents.writer_agent import write_report

topic = "Impact of AI in Healthcare"

print("🧠 Generating subtasks...")
subtasks = generate_subtasks(topic)

print("\n🔍 Researching...")
research = research_subtasks(subtasks)

print("\n📊 Analyzing...")
analysis = analyze_research(research)

print("\n✍ Writing final report...")
report = write_report(topic, analysis)

print("\n" + "=" * 70)
print("FINAL REPORT")
print("=" * 70)

print(report)