from dataclasses import dataclass
from typing import List, Optional

@dataclass
class EntryFilter:
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    mood: Optional[str] = None
    weather: Optional[str] = None
    tags: Optional[List[str]] = None
    search: Optional[str] = None
