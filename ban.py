from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins

# Your API ID and Hash
api_id = '7980140'
api_hash = 'db84e318c6894f560a4087c20c33ce0a'

# Initialize the client
client = TelegramClient('userbot_session', api_id, api_hash)

@client.on(events.NewMessage(pattern=r"\.b", outgoing=True))
async def silent_ban_all(event):
    if event.is_channel:
        # Silently ban all users in the channel
        async for user in client.iter_participants(event.chat_id):
            try:
                # Ban user by revoking the permission to view messages
                await client.edit_permissions(event.chat_id, user.id, view_messages=False)
            except Exception as e:
                print(f"Failed to ban {user.id}: {e}")

# Start the client
client.start()
client.run_until_disconnected()
