-- Table to store source and target channel configurations
CREATE TABLE IF NOT EXISTS channel_config (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_channel_id TEXT NOT NULL,
    target_channel_id TEXT NOT NULL,
    UNIQUE(source_channel_id, target_channel_id)
);

-- Table to store the forwarded message data for resuming
CREATE TABLE IF NOT EXISTS forwarded_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_id INTEGER NOT NULL,
    source_channel_id TEXT NOT NULL,
    target_channel_id TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending', -- 'pending', 'forwarded', 'failed'
    UNIQUE(message_id, source_channel_id, target_channel_id)
);