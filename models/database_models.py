from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Entry:
    id: Optional[int]
    date: str
    title: str
    content: str
    mood: Optional[str]
    weather: Optional[str]
    tags: Optional[List[str]]
    word_count: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class AIAnalysis:
    id: Optional[int]
    entry_id: int
    analysis_type: str
    result: str
    created_at: Optional[str] = None
