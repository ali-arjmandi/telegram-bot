from pyrogram import types
from pyrogram.client import Client
from datetime import datetime
from ...help import get as getHelp
time = datetime.now()


async def hi(_, message: types.Message):
    await message.reply('Hi...')


async def upTime(_, message: types.Message):
    now = datetime.now()
    s = (now - time).seconds
    hours, remainder = divmod(s, 3600)
    minutes, seconds = divmod(remainder, 60)
    await message.reply('{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds)))


async def info(client: Client, message: types.Message):
    await message.delete()
    replied_user = message.reply_to_message.from_user
    id = replied_user.id
    full_name = f'{replied_user.first_name} {replied_user.last_name}'
    username = replied_user.username
    await client.send_message("me", f'ID: {id}\nname: {full_name}'+(f'\nusername: @{username}' if username else ''))


async def help(_, message: types.Message):
    await message.reply(getHelp())
