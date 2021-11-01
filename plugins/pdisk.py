
# (c) HeimanPictures


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import requests

from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.private & filters.command(['connect']))
async def connect(client,message):
	await message.reply_text('Send Me Your api_key from pdisk\nhttps://www.cofilink.com/use-api',reply_to_message_id = message.message_id,reply_markup=ForceReply(True))
	            

@Client.on_message(filters.private & filters.reply)
async def api_connect(client,message):
        if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply):
        	API_KEY = message.text
        	res = api_check(str(API_KEY))
        	try:
        		check = res['data']
        		set(message.chat.id,API_KEY)
        		await message.reply_text("Your Account Conected Successfully ✅",reply_to_message_id = message.message_id)
        	except Exception as f:
        		print(f)
        		e = res['msg']
        		await message.reply_text(f"Error: {e}",reply_to_message_id = message.message_id)


	       	

@Client.on_message(filters.private & filters.regex("http|https"))
async def upload(client,message):
	api_key = find(message.chat.id)
	if api_key:
		data = message.text
		v_ = data.split("\n")
		try:
			title = v_[0].split('-')[1]
			link  = v_[1].split('-')[1].replace(" ","")
		except :
			await message.reply_text('Use Help Command to know how to use me',reply_to_message_id = message.message_id)
			return
		try:
			thumb =  v_[2].split('-')[1].replace(" ","")
		except:
			thumb = None
		if thumb:
			res = pdisk_url(api_key,link,title,thumb)
			try:
				id = res['data']['item_id']
				await message.reply_text(f'Title : {title} URL :
https://cofilink.com/share-video?videoid={id}
This File Will Be Uploading in  10 - 15 Minutes',reply_to_message_id = message.message_id)
			except:
				e = res['msg']
				await message.reply_text(f"Error:
{e}
",reply_to_message_id = message.message_id)
		else:
			res = pdisk_url(api_key,link,title)
			try:
				id = res['data']['item_id']
				await message.reply_text(f'Title : {title} URL:
https://cofilink.com/share-video?videoid={id}
\n\n This File Will Be Uploading in  10 - 15 Minutes ',reply_to_message_id = message.message_id)
			except:
				e = res['msg']
				await message.reply_text(f"Error:
{e}
",reply_to_message_id = message.message_id)
			
	else:
		await message.reply_text("Connect Your Account Using Command /connect",reply_to_message_id = message.message_id)
