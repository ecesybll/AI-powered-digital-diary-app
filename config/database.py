import sqlite3
from config.settings import DB_PATH

ENTRIES_SCHEMA = '''
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    mood TEXT,
    weather TEXT,
    tags TEXT,
    word_count INTEGER,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);
'''

AI_ANALYSES_SCHEMA = '''
CREATE TABLE IF NOT EXISTS ai_analyses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entry_id INTEGER NOT NULL,
    analysis_type TEXT NOT NULL,
    result TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(entry_id) REFERENCES entries(id)
);
'''

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(ENTRIES_SCHEMA)
    cursor.execute(AI_ANALYSES_SCHEMA)
    conn.commit()
    conn.close()
