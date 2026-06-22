from agents.research_agent import research_topic
from agents.writer_agent import write_report


def research_node(state):
    print("\n🔍 Research Agent Running...")

    results = research_topic(state.topic)

    state.research_results = results

    return state


def writer_node(state):
    print("\n✍ Writer Agent Running...")

    report = write_report(
        state.topic,
        state.research_results
    )

    state.report = report

    return state