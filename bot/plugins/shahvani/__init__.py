from pyrogram import filters
from .task import scrap, getBoob, getAss, getPussy, getDick, getDepth

handlers = [
    (scrap, filters.me & filters.text & filters.command(
        'sh_scrap'), 'scrap images from shahvani.com'),
    (getDepth, filters.me & filters.text & filters.command(
        'sh_depth'), 'show page depth when scrap shahvani.com'),
    (getBoob, filters.incoming & filters.private & filters.text &
     filters.command('ممه', prefixes='')),
    (getAss, filters.incoming & filters.private &
     filters.text & filters.command('کون', prefixes='')),
    (getPussy, filters.incoming & filters.private & filters.text &
     filters.regex('^(کس|کص)$')),
    (getDick, filters.incoming & filters.private & filters.text &
     filters.command('کیر', prefixes='')),
]
