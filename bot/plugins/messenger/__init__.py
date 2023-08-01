from pyrogram import filters
from .task import receive

handlers = [
    (receive, filters.private & filters.text & filters.regex(f'^(?!\/).*')),
]
