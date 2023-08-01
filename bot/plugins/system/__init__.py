from pyrogram import filters
from .task import hi, upTime, help

handlers = [
    (hi, filters.private & filters.text & filters.command('hi'), 'say hi'),
    (upTime, filters.private & filters.text &
     filters.command('uptime'), 'get upTime'),
    (help, filters.private & filters.text &
     filters.command('help'), 'get documentation'),
]
