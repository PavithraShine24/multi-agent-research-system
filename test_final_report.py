from agents.orchestrator_agent import generate_subtasks
from agents.research_agent import research_subtasks
from agents.analyst_agent import analyze_research
from agents.writer_agent import write_report
from agents.fact_checker_agent import fact_check_report
from agents.human_loop_agent import human_review
from agents.revision_agent import revise_report

topic = "Impact of AI in Healthcare"

print("🧠 Generating subtasks...")
subtasks = generate_subtasks(topic)

print("\n🔍 Researching...")
research = research_subtasks(subtasks)


print("\n📊 Analyzing...")
analysis = analyze_research(research)

print("\nANALYSIS OUTPUT:")
print(analysis)

print("\n✍ Writing final report...")
report = write_report(topic, analysis)

print("\n✅ Fact Checking...")
fact_check = fact_check_report(report)

print("\n" + "="*60)
print("FINAL REPORT")
print("="*60)

print(report)

print("\n" + "="*60)
print("FACT CHECK RESULTS")
print("="*60)

print(fact_check)

while True:
    print("\n👤 Human Review...")
    decision = human_review(report)

    if decision == "yes":
        final_report = report
        break

    print("\n📝 Revising report based on fact-check feedback...")
    report = revise_report(report, fact_check)

    print("\n🔍 Fact Checking revised report...")
    fact_check = fact_check_report(report)