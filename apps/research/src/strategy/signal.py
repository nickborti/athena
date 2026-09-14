from dataclasses import dataclass
from datetime import datetime


@dataclass
class Signal:
    action: str
    timestamp: datetime