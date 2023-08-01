from pyrogram import Client
from bot import handlers
from dotenv import load_dotenv
from os.path import join, dirname
import os

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

app = Client("bot", api_id=int(os.getenv('API_ID')), api_hash=os.getenv('API_HASH'), bot_token=os.getenv('BOT_TOKEN'))


def start():
    handlers.loadHandlers(app)
    print('running...')
    app.run()
