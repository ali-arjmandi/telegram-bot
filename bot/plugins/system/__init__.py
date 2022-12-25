from pyrogram import filters
from .task import hi, upTime, help, info

handlers = [
    (hi, filters.me & filters.text & filters.command('hi'), 'say hi'),
    (upTime, filters.me & filters.text &
     filters.command('uptime'), 'get upTime'),
    (info, filters.reply & filters.outgoing & filters.text &
     filters.command('info'), 'get user\'s info'),
    (help, filters.me & filters.text &
     filters.command('help'), 'get documentation'),
]
