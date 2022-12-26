from pyrogram import filters
from .task import scrap, getBoob, getAss, getPussy, getDick, getDepth, getAnal, getLesbian, getShemale

handlers = [
    (scrap, filters.me & filters.text & filters.command(
        'sh_scrap'), 'scrap images from shahvani.com'),
    (getDepth, filters.me & filters.text & filters.command(
        'sh_depth'), 'show page depth when scrap shahvani.com'),
    (getBoob, filters.incoming & filters.private & filters.text &
     filters.regex('ممه')),
    (getAss, filters.incoming & filters.private &
     filters.text & filters.regex('کون')),
    (getPussy, filters.incoming & filters.private & filters.text &
     filters.regex('^ک(س|ص)$')),
    (getDick, filters.incoming & filters.private & filters.text &
     filters.regex('کیر')),
    (getAnal, filters.incoming & filters.private & filters.text &
     filters.regex('آنال')),
    (getLesbian, filters.incoming & filters.private & filters.text &
     filters.regex('لزبین')),
    (getShemale, filters.incoming & filters.private & filters.text &
     filters.regex('شیمیل')),
]
