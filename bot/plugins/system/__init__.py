from pyrogram import filters
from .task import hi, upTime, help

handlers = [
    (hi, filters.me & filters.text & filters.command('hi'), 'say hi'),
    (upTime, filters.me & filters.text &
     filters.command('uptime'), 'get upTime'),
    (help, filters.me & filters.text &
     filters.command('help'), 'get documentation'),
]
