from dataclasses import dataclass, field

@dataclass
class AppState:
    topic: str = ""
    subtasks: list = field(default_factory=list)
    report: str = ""
    approved: bool = False


state = AppState(
    topic="Impact of AI in Healthcare"
)

print("Initial State:")
print(state)

state.subtasks.append("Benefits of AI")
state.report = "AI improves diagnosis."
state.approved = True

print("\nUpdated State:")
print(state)