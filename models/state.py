from dataclasses import dataclass, field

@dataclass
class AppState:
    topic: str = ""

    subtasks: list = field(default_factory=list)

    research_results: list = field(default_factory=list)

    report: str = ""