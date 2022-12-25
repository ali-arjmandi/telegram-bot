from pyrogram import types
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


async def help(_, message: types.Message):
    await message.reply(getHelp())
