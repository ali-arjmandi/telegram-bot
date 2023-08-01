from pyrogram import filters
from .task import scrap, getDepth, getMedia

handlers = [
    (scrap, filters.me & filters.text & filters.command(
        'sh_scrap'), 'scrap images from shahvani.com'),
    (getDepth, filters.me & filters.text & filters.command(
        'sh_depth'), 'show page depth when scrap shahvani.com'),
    (lambda *args: getMedia(*args, 'boob'), filters.incoming & filters.private & filters.text &
     filters.command('ممه', prefixes='')),
    (lambda *args: getMedia(*args, 'ass'), filters.incoming & filters.private &
     filters.text & filters.command('کون', prefixes='')),
    (lambda *args: getMedia(*args, 'pussy'), filters.incoming & filters.private & filters.text &
     filters.regex('^(کس|کص)$')),
    (lambda *args: getMedia(*args, 'dick'), filters.incoming & filters.private & filters.text &
     filters.command('کیر', prefixes='')),
    (lambda *args: getMedia(*args, 'anal'), filters.incoming & filters.private & filters.text &
     filters.command('آنال', prefixes='')),
    (lambda *args: getMedia(*args, 'lesbian'), filters.incoming & filters.private & filters.text &
     filters.command('لزبین', prefixes='')),
    (lambda *args: getMedia(*args, 'shemale'), filters.incoming & filters.private & filters.text &
     filters.command('شیمیل', prefixes='')),
]
