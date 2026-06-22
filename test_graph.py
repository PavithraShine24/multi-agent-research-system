from models.state import AppState
from graph.workflow import build_graph

graph = build_graph()

initial_state = AppState(
    topic="Impact of AI in Healthcare"
)

final_state = graph.invoke(initial_state)

print("\n" + "=" * 60)
print("FINAL REPORT")
print("=" * 60)

print(final_state["report"])