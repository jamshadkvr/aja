#@Aadhi000 #Neo #neo

from datetime import datetime
import asyncio
import os
import math
import time
import heroku3
import requests
from pyrogram import Client, filters

#━━━━━━━━━━━━━━〔─〕━━━━━━━━━━━━━━
BOT_START_TIME = time.time()
#━━━━━━━━━━━━━━〔─〕━━━━━━━━━━━━━━

@Client.on_message(filters.command("ping"))
async def ping(_, message):
    start_t = time.time()  
    avr = await message.reply_text("‹○○○›")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = time.strftime("%HH | %MM | %SS", time.gmtime(time.time() - BOT_START_TIME))   
    await avr.edit(f"‹ ᴄᴜʀʀᴇɴᴛ ʙᴏᴛ sᴛᴀᴛᴜs ›\n\n‹› ᴘᴏɴɢ : {time_taken_s:.3f} ms\n‹› ʙᴏᴛ ᴜᴘᴛɪᴍᴇ : {uptime}")
    start_time = datetime.now()
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))


@Client.on_message(filters.command("pong"))
async def pong(_, message):
    start_time = datetime.now()
    # do your work here
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
