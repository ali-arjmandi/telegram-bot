from pyrogram import Client
from bot import handlers

app = Client("bot", api_id=0, api_hash='', phone_number='')


def start():
    handlers.loadHandlers(app)
    print('running...')
    app.run()
