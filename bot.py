# -*- coding: utf-8 -*-

from datetime import datetime
import telegram
from telegram.ext import *
d = 0

abcd = []
day = []
day.append(0)
abcd.append(0)
send = []
send.append(1)
#blocklist = []
f = open("b.txt","r")
blocklist = []
for line in f:
    blocklist.append(line)
f.close()
number=[]
f = open("admin.txt","r")
admins = []
for line in f:
    admins.append(line)
f.close()
num=0
text = [""]
updater = Updater(token='272130715:AAGuzZpBhV4dklVSCs4GovHwlLkTzm-BNAM')



dispatcher = updater.dispatcher

f = open("e.txt","r")
a = f.read()
f.close()
for i in range(int(a)):
    number.append(1)

def start(bot, update):
    f = open("a.txt", "r")
    a = ""
    for line in f:
        a = a + "\n" + line
    f.close()
    key = ['/start']

    custom_keyboard = [[item] for item in key]

    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)


    user = update.message.from_user
    bot.sendMessage(chat_id=update.message.chat_id, text=a,reply_markup=reply_markup)
    bot.sendMessage(chat_id=334721768, text=user.first_name+"("+str(user.id)+")", reply_markup=reply_markup)
    bot.sendMessage(chat_id=334721768, text="@"+user.username, reply_markup=reply_markup)

def osgol(bot,update):
    use = True


    user = update.message.from_user

    user_msg = update.message.text
    dispatcher.add_handler(MessageHandler(Filters.voice, voice))
    bot.sendMessage(chat_id=334721768, text=user.first_name+"("+str(user.id)+")"+":"+user_msg)
    bot.sendMessage(chat_id=334721768, text=user.username)

    for i in range(len(user_msg)-3):
        if user_msg[i] == user_msg[i+1] and user_msg[i+1] == user_msg[i+2] and user_msg[i] != " " and user_msg[i] != "\n" and user_msg[i] != ".":
            use = False
        elif user_msg[i] == user_msg[i+2] and user_msg[i+2] == user_msg[i+4] and user_msg[i+1] == user_msg[i+3] and user_msg[i+3] == user_msg[i+5] and user_msg[i] != "\n" and user_msg[i] != "." and user_msg[i+1] != "\n" and user_msg[i+1] != "." and user_msg[i] != " " and user_msg[i+1] != " ":
            use = False
    now = datetime.now()
    if user_msg[:6]=="sendid":
        bot.sendMessage(chat_id=user_msg[6:15], text= user_msg[16:])
        bot.sendMessage(chat_id=update.message.chat_id, text="sent :)")
    elif user_msg[:10]=="addtoadmin":
        admins.append(user_msg[10:19])
        f = open("admin.txt", "w")
        a = ""
        for i in admins:
            a = a + str(i) + "\n"
        f.write(a)
        f.close()
        bot.sendMessage(chat_id=update.message.chat_id,text="added")

    elif user_msg[:7] == "blockid":
        blocklist.append(user_msg[7:16])
        f = open("b.txt", "w")
        a=""
        for i in blocklist:
           a = a + "\n" +str(i)
        f.write(a)
        f.close()
        bot.sendMessage(chat_id=update.message.chat_id, text="user blocked")

    elif user_msg[:7] == "settext":
        text.append(user_msg[7:])
    else:#now.minute + now.hour*60 > abcd[::-1][0] + 120#(now.minute + now.hour*60 > abcd[::-1][0] + 120 or now.day != day[::-1][0])
        if user.id not in blocklist  and 10<len(user_msg) and len(user_msg)<3000 and ((now.minute + now.hour*60 > abcd[::-1][0] + 120 or now.day != day[::-1][0]) or str(user.id)=="334721768") and "@" not in user_msg and "joinchat"  not in user_msg and use==True :

            number.append(1)
            f = open("e.txt","w")
            f.write(str(len(number)))
            f.close()
            now = datetime.now()
            abcd.append(now.minute + now.hour*60)
            day.append(now.day)
            f = open("g.txt", "r")
            a = ""
            for line in f:
                a = a + "\n" + line
            f.close()
            bot.sendMessage(chat_id=-1001126198228, text=user_msg+"\n"+"\""+"#"+user.first_name+"\""+"\n"+"@azadadmintweetbot" +"\n"+str(len(number)+1))

            bot.sendMessage(chat_id=update.message.chat_id, text=a)

        elif now.minute + now.hour < abcd[::-1][0]+120 and day[::-1][0] == now.day:
            f = open("f.txt", "r")
            a = ""
            for line in f:
                a = a + "\n" + line
            f.close()
            bot.sendMessage(chat_id=update.message.chat_id,text=a)

        elif user.id not in blocklist:
            f = open("c.txt", "r")
            a = ""
            for line in f:
                a = a + "\n" + line
            f.close()
            bot.sendMessage(chat_id=update.message.chat_id, text=a)

        else:
            f = open("d.txt", "r")
            a = ""
            for line in f:
                a = a + "\n" + line
            f.close()
            bot.sendMessage(chat_id=update.message.chat_id, text=a)


def voice(bot,update):
    if str(update.message.chat_id)+"\n" in admins or str(update.message.chat_id) in admins:

        number.append(1)
        bot.send_voice(chat_id=-1001126198228, voice=update.message.voice.file_id,
                       caption=text[::-1][0] + "\n" + "@azadadmintweetbot" + "\n" +  str(len(number) + 1))

        text.pop(len(text))
        text.append("")

    else :
        f = open("eror.txt" ,"r")
        a=""
        for line in f:
           a=a+line
        f.close()
        bot.sendMessage(chat_id=update.message.chat_id,text=a)
        bot.send_voice(chat_id=334721768, voice=update.message.voice.file_id)

def news(bot,update):
    f = open("news.txt","r")
    a=""
    for line in f:
       a = a + line
    f.close()
    bot.sendMessage(chat_id=update.message.chat_id,text=a)

def sticker(bot,update):
    if str(update.message.chat_id) + "\n" in admins or str(update.message.chat_id) in admins:
        bot.send_sticker(-1001126198228,update.message.sticker.file_id)

def photo(bot,update):
    if str(update.message.chat_id) + "\n" in admins or str(update.message.chat_id) in admins:
        number.append(1)
        bot.send_photo(-1001126198228,update.message.photo[-1].file_id,caption=text[::-1][0]+ "\n"+"@azadadmintweetbot" +"\n"+str(len(number)+1))

        text.pop(len(text))
        text.append("")
    else:
        f = open("eror.txt", "r")
        a = ""
        for line in f:
            a = a + line
        f.close()
        bot.sendMessage(chat_id=update.message.chat_id, text=a)
        bot.send_photo(334721768, update.message.photo[-1].file_id)



def gif(bot,update):
    if str(update.message.chat_id) + "\n" in admins or str(update.message.chat_id) in admins:
        bot.send_video(chat_id=-1001126198228,video=update.message.video.file_id,caption=text[::-1][0])
        text.pop(len(text))
        text.append("")
    else:
        f = open("eror.txt", "r")
        a = ""
        for line in f:
            a = a + line
        f.close()
        bot.sendMessage(chat_id=update.message.chat_id, text=a)
        bot.send_video(chat_id=334721768, video=update.message.video.file_id)

def document(bot,update):
    if str(update.message.chat_id) + "\n" in admins or str(update.message.chat_id) in admins:
        bot.send_document(chat_id=-1001126198228,document=update.message.document.file_id,caption=text[::-1][0])
        text.pop(len(text))
        text.append("")
    else:
        f = open("eror.txt", "r")
        a = ""
        for line in f:
            a = a + line
        f.close()
        bot.sendMessage(chat_id=update.message.chat_id, text=a)
        bot.send_document(chat_id=334721768, video=update.message.document.file_id)

def audio(bot,update):
    if str(update.message.chat_id) + "\n" in admins or str(update.message.chat_id) in admins:
        bot.sendAudio(chat_id=-1001126198228,audio=update.message.audio.file_id,caption=text[::-1][0])
        text.pop(len(text))
        text.append("")
    else:
        f = open("eror.txt", "r")
        a = ""
        for line in f:
            a = a + line
        f.close()
        bot.sendMessage(chat_id=update.message.chat_id, text=a)
        bot.sendAudio(chat_id=334721768, audio=update.message.audio.file_id)
        print("ok")


dispatcher.add_handler((MessageHandler(Filters.audio,audio)))

dispatcher.add_handler(MessageHandler(Filters.document,document))

dispatcher.add_handler(CommandHandler('start', start))

dispatcher.add_handler(CommandHandler('qqqq',news))

dispatcher.add_handler(MessageHandler(Filters.video,gif))

dispatcher.add_handler(MessageHandler(Filters.photo,photo))

dispatcher.add_handler(MessageHandler(Filters.text, osgol))

dispatcher.add_handler(MessageHandler(Filters.voice,voice))

dispatcher.add_handler(MessageHandler(Filters.sticker,sticker))



updater.start_polling()
