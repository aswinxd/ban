from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins

# Your API ID and Hash
api_id = '7980140'
api_hash = 'db84e318c6894f560a4087c20c33ce0a'

# Initialize the client
client = TelegramClient('userbot_session', api_id, api_hash)

@client.on(events.NewMessage(pattern=r"\.b", outgoing=True))
async def ban_all(event):
    if event.is_channel:
        # Check if user has admin rights in the channel
        admins = await client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        if event.sender_id not in [admin.id for admin in admins]:
            await event.reply("You need to be an admin to ban members.")
            return

        # Ban all users except admins
        async for user in client.iter_participants(event.chat_id):
            if user.id not in [admin.id for admin in admins]:
                try:
                    await client.edit_permissions(event.chat_id, user.id, view_messages=False)
                    await event.reply(f"Banned {user.id}")
                except Exception as e:
                    print(f"Failed to ban {user.id}: {e}")

        await event.reply("All non-admin members have been banned.")
    else:
        await event.reply("This command only works in channels.")

# Start the client
client.start()
client.run_until_disconnected()
