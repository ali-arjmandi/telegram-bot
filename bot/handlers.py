from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from bot import plugins, help


def loadHandlers(app: Client):
    handlers = [
        handler for plugin in plugins.active_plugins.keys() for handler in plugins.active_plugins[plugin].handlers
    ]
    help.generateHelp(handlers)

    for handler in handlers:
        app.add_handler(MessageHandler(handler[0], handler[1]))
