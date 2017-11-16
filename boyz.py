# -*- coding: utf-8 -*-
import telegram
from telegram.ext import *

updater = Updater(token='Token')

dispatcher = updater.dispatcher

def start(bot,update):
    usr = update.message.from_user
    msg = update.message.text

    bot.sendMessage(chat_id=update.message.chat_id,text="خوش آمدید برای ثبت نام روی لینک زیر کلیک کنید")
