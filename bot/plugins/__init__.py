from . import system, shahvani, messenger

all_plugins = {
    'system': system,
    'shahvani': shahvani,
    'messenger': messenger,
}

active_plugins = all_plugins.copy()
