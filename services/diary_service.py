from config.database import get_connection
from models.database_models import Entry
from typing import List, Optional
import json

def add_entry(entry: Entry) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO entries (date, title, content, mood, weather, tags, word_count)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        entry.date, entry.title, entry.content, entry.mood, entry.weather, json.dumps(entry.tags), entry.word_count
    ))
    conn.commit()
    entry_id = cursor.lastrowid
    conn.close()
    return entry_id

def get_entries() -> List[Entry]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries ORDER BY date DESC')
    rows = cursor.fetchall()
    conn.close()
    entries = []
    for row in rows:
        entries.append(Entry(
            id=row[0],
            date=row[1],
            title=row[2],
            content=row[3],
            mood=row[4],
            weather=row[5],
            tags=json.loads(row[6]) if row[6] else [],
            word_count=row[7],
            created_at=row[8],
            updated_at=row[9]
        ))
    return entries

def get_entry(entry_id: int) -> Optional[Entry]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries WHERE id = ?', (entry_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Entry(
            id=row[0],
            date=row[1],
            title=row[2],
            content=row[3],
            mood=row[4],
            weather=row[5],
            tags=json.loads(row[6]) if row[6] else [],
            word_count=row[7],
            created_at=row[8],
            updated_at=row[9]
        )
    return None
