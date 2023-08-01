from pyrogram import types, Client
import os

MESSENGER_PUBLIC_CHANNEL_ID=int(os.getenv('MESSENGER_PUBLIC_CHANNEL_ID'))
MESSENGER_PRIVATE_CHANNEL_ID=int(os.getenv('MESSENGER_PRIVATE_CHANNEL_ID'))

async def receive(client: Client, message: types.Message):
    try:
        await client.send_message(MESSENGER_PUBLIC_CHANNEL_ID, message.text)
    except: pass
    try:
        await client.forward_messages(MESSENGER_PRIVATE_CHANNEL_ID, message.chat.id, message.id)
    except: pass
