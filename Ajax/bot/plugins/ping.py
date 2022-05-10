from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
import time
import shutil, psutil
from utils_bot import *
from Ajax import StartTime

@Client.on_message(filters.command('ajax') & filters.private & ~filters.edited)
async def ajax(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  botstats = f'<b>Bot Uptime:</b> {currentTime}' 
            
  await update.reply_text(botstats)
