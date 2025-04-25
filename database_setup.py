import sqlite3

# Database connection
DB_FILE = 'bot_data.db'
conn = sqlite3.connect(DB_FILE)

def initialize_database():
    with conn:
        # Create table for channel configurations
        conn.execute("""
            CREATE TABLE IF NOT EXISTS channel_config (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_channel_id TEXT NOT NULL,
                target_channel_id TEXT NOT NULL,
                UNIQUE(source_channel_id, target_channel_id)
            )
        """)
        # Create table for tracking forwarded messages
        conn.execute("""
            CREATE TABLE IF NOT EXISTS forwarded_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message_id INTEGER NOT NULL,
                source_channel_id TEXT NOT NULL,
                target_channel_id TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending', -- 'pending', 'forwarded', 'failed'
                UNIQUE(message_id, source_channel_id, target_channel_id)
            )
        """)

# Initialize the database on import
initialize_database()