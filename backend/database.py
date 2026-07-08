import sqlite3

# ----------------------------
# SQLite Connection
# ----------------------------

conn = sqlite3.connect(
    "networking.db",
    check_same_thread=False
)

conn.row_factory = sqlite3.Row

cursor = conn.cursor()

# ----------------------------
# Conversation History
# ----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bio TEXT,
    event TEXT,
    interests TEXT,
    response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# ----------------------------
# Feedback
# ----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    response TEXT,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()