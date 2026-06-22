from dataclasses import dataclass, field

@dataclass
class AppState:
    topic: str = ""
    research_results: list = field(default_factory=list)
    report: str = ""