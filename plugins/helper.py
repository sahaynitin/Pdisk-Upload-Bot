# (c) HeimanPictures
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START = """
Hey  {}!
        
I am Pdisk Uploader Bot. It Can Upload any Link To PDisk.

➠ I Can Upload any link 🖇️ to Pdisk
➠ Use @Tellylinkgeneratorbot For Generating link First

Use /help Command to know how to use me...

 **Made With 💕 By @Tellybots_4u**
"""

HELP = """
**How to Use Me...**

⦿ Its Easy to Use me 
✪ » Send me Any Direct Link or YouTube Link
✪ » i will upload to PDisk & Give Link

➠ If you want Upload Telegram file,Videos to PDisk
✪ » First Send any File to @Tellylinkgeneratorbot to generate Direct Link
✪ » Copy Generated Link and Paste here...
✪ » Wait Sometimes it will done

➠ If You Want add Custom Tittle & Thumbnail Follow These Steps

✪ » link | Title

✪ » Video link | Title | Thumbnail link
        (generate Thumbnail Link with Telegraph bot[@TGraphXbot])

NOTE:
➢ Do Not Spam, Send Link One By One, 
➢ The Video File is Available on Your LINK ones Upload Process is Complete, it Take Time Depend on Your File Size & My Server Upload Speed
So,be Patient 😴😴😴😴"""


ABOUT = """
**About me...**
🤖 My Name : [Pdisk Uploader Bot](https://t.me/tellypdiskuploaderbot)

👲 Developer : [Tellybots_4u](https://t.me/tellybots_4u)

⚗️ Credits : Everyone in this Journey

📚 Library : [Python](https://python.in)

🪐 Server : [Heroku](https://heroku.com)

🌇 Build Status : Version 2.1

💫 Source Code : [Tellybots_digital](https://t.me/tellybots_digital)


# NON_OWNER = "You Can't Use Me Ask My [Owner](tg://user?id={})"


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🍿 Source Code 🍿', url='https://github.com/OO7ROBot/Pdisk-Upload-Bot')
        ],[
        InlineKeyboardButton('Channel', url='https://telegram.me/MyTestBotZ'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Back', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )



@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=START.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )


@Client.on_message(filters.command('help') & filters.private)
async def help(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )


@Client.on_message(filters.command('about') & filters.private)
async def help(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=ABOUT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )

@Client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    else:
        await update.message.delete()
