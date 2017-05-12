import time
import random
import datetime
import telepot
import urllib
"""
After **inserting token** in the source code, run it:
```
$ python2.7 diceyclock.py
```
[Here is a tutorial](http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/)
teaching you how to setup a bot on Raspberry Pi. This simple bot does nothing
but accepts two commands:
- `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
- `/time` - reply with the current time, like a clock.
"""

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/cocina':
	htmlfile=urllib.urlopen("http://cocina/json")
        htmltext=htmlfile.read()
        bot.sendMessage(chat_id, str(htmltext))
    elif command == '/outdoor':
        htmlfile=urllib.urlopen("http://outdoor/json")
        htmltext=htmlfile.read()
        bot.sendMessage(chat_id, str(htmltext))
    elif command == '/bedroom':
        htmlfile=urllib.urlopen("http://bedroom/json")
        htmltext=htmlfile.read()
        bot.sendMessage(chat_id, str(htmltext))
    elif command == '/livingroom':
        htmlfile=urllib.urlopen("http://livingroom/json")
        htmltext=htmlfile.read()
        bot.sendMessage(chat_id, str(htmltext))
    elif command == '/reiniciar_cocina':
        htmlfile=urllib.urlopen("http://cocina/?cmd=reboot")
        htmltext=htmlfile.read()
        bot.sendMessage(chat_id, str(htmltext))
    elif command == '/reiniciar_outdoor':
        htmlfile=urllib.urlopen("http://outdoor/?cmd=reboot")
        htmltext=htmlfile.read()
        bot.sendMessage(chat_id, str(htmltext))
    elif command == '/reiniciar_bedroom':
        htmlfile=urllib.urlopen("http://bedroom/?cmd=reboot")
        htmltext=htmlfile.read()
        bot.sendMessage(chat_id, str(htmltext))
    elif command == '/reiniciar_livingroom':
        htmlfile=urllib.urlopen("http://livingroom/?cmd=reboot")
        htmltext=htmlfile.read()
        bot.sendMessage(chat_id, str(htmltext))
    elif command == '/roomba':
        htmlfile=urllib.urlopen("http://roomba")
        htmltext=htmlfile.read()
        bot.sendMessage(chat_id, str(htmltext))
    elif command == '/roombastart':
        htmlfile=urllib.urlopen("http://roomba/roombastart")
        htmltext=htmlfile.read()
        bot.sendMessage(chat_id, str(htmltext))
    elif command == '/roombadock':
        htmlfile=urllib.urlopen("http://roomba/roombadock")
        htmltext=htmlfile.read()
        bot.sendMessage(chat_id, str(htmltext))
    elif command == '/luz':
        htmlfile=urllib.urlopen("http://api.thingspeak.com/channels/259633/feeds/last.json?api_key=ADIY3ISFSNZEG8Y5")
        htmltext=htmlfile.read()
        bot.sendMessage(chat_id, str(htmltext))

bot = telepot.Bot('188270811:AAGOrZpT4Aq4lG9uebzZKYm_0SlPRWbEqi0')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)
