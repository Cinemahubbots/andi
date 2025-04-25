from telethon import events
from database_setup import conn

cursor = conn.cursor()

@client.on(events.NewMessage(pattern='/setsource'))
async def set_source(event):
    if event.is_private:
        try:
            source_channel_id = event.message.text.split(' ')[1]
            cursor.execute("SELECT * FROM channel_config WHERE source_channel_id = ?", (source_channel_id,))
            if cursor.fetchone():
                await event.reply(f"Source channel {source_channel_id} is already set.")
            else:
                cursor.execute("INSERT INTO channel_config (source_channel_id, target_channel_id) VALUES (?, ?)",
                               (source_channel_id, ""))
                conn.commit()
                await event.reply(f"Source channel {source_channel_id} has been set.")
        except IndexError:
            await event.reply("Invalid command format. Use `/setsource <channel_id>`.")
        except Exception as e:
            await event.reply(f"An error occurred: {str(e)}")

@client.on(events.NewMessage(pattern='/settarget'))
async def set_target(event):
    if event.is_private:
        try:
            target_channel_id = event.message.text.split(' ')[1]
            cursor.execute("SELECT source_channel_id FROM channel_config WHERE target_channel_id = ?", ("",))
            row = cursor.fetchone()
            if row:
                source_channel_id = row[0]
                cursor.execute("UPDATE channel_config SET target_channel_id = ? WHERE source_channel_id = ?",
                               (target_channel_id, source_channel_id))
                conn.commit()
                await event.reply(f"Target channel {target_channel_id} has been set for source channel {source_channel_id}.")
            else:
                await event.reply("Please set a source channel first using `/setsource`.")
        except IndexError:
            await event.reply("Invalid command format. Use `/settarget <channel_id>`.")
        except Exception as e:
            await event.reply(f"An error occurred: {str(e)}")
