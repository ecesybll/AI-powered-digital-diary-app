from config.database import get_connection
from typing import Dict
import json

def get_entry_stats() -> Dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*), AVG(word_count) FROM entries')
    count, avg_word_count = cursor.fetchone()
    cursor.execute('SELECT mood, COUNT(*) FROM entries GROUP BY mood')
    mood_stats = {row[0]: row[1] for row in cursor.fetchall()}
    cursor.execute('SELECT weather, COUNT(*) FROM entries GROUP BY weather')
    weather_stats = {row[0]: row[1] for row in cursor.fetchall()}
    conn.close()
    return {
        'total_entries': count,
        'avg_word_count': avg_word_count,
        'mood_stats': mood_stats,
        'weather_stats': weather_stats
    }

def get_tag_trends() -> Dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT tags FROM entries')
    tag_counts = {}
    for (tags_json,) in cursor.fetchall():
        tags = json.loads(tags_json) if tags_json else []
        for tag in tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    conn.close()
    return tag_counts
