# Lets create a telegram bot!

This is a plugin base and clean template for telegram bots using **Pyrogram**. there is two plugins for sample:

- **system**: base functionalities like up time, help command and "Hi" for pinging.
- **shahvani**: this plugin scraps a pornography website and sends you some nudes.

# Deploy

you can use this bot on your own telegram easily:

- copy source code to your server (or google colab)
- go to `/bot/__init__.py` and replace your account information, (api_id, api_hash, phone_number or token)
- install dependencies by `pip install -r requirements.txt`
- run bot by `python main.py`
  > **Note:** for the first time, bot needs to login to your account. so telegram sends you a verification code and you need to enter the code in terminal after running bot.
