import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "radar.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id TEXT PRIMARY KEY,
            title TEXT,
            snippet TEXT,
            category TEXT,
            intent_score INTEGER,
            freshness_text TEXT,
            source TEXT,
            url TEXT,
            status TEXT DEFAULT 'جديد',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_leads(leads):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    new_count = 0
    for lead in leads:
        cursor.execute('''
            INSERT OR IGNORE INTO leads (id, title, snippet, category, intent_score, freshness_text, source, url, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            lead['id'],
            lead['title'],
            lead['snippet'],
            lead['category'],
            lead['intent_score'],
            lead['freshness_text'],
            lead['source'],
            lead['url'],
            lead.get('status', 'جديد')
        ))
        if cursor.rowcount > 0:
            new_count += 1
    conn.commit()
    conn.close()
    return new_count

def get_all_leads():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM leads ORDER BY created_at DESC')
    rows = cursor.fetchall()
    leads = [dict(row) for row in rows]
    conn.close()
    return leads
  
