from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime

PROXY={'proxy_url': 'socks5://t1.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username':'learn', 'password':'python'}}
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log')

def great_user(bot, update):
    text="Вызван /start"
    print(text)
    update.message.reply_text(text)
    print(update)

def planet_constellation(bot, update):
    p_planet=input("Введите название планеты на английском: ")
    
    if p_planet.lower()=='mars':
        ret=ephem.constellation(ephem.Mars(datetime.datetime.now()))
    elif p_planet.lower()=='venus':
        ret=ephem.constellation(ephem.Venus(datetime.datetime.now()))
    elif p_planet.lower()=='vupiter':
        ret=ephem.constellation(ephem.Jupiter(datetime.datetime.now()))
    elif p_planet.lower()=='uranus':
        ret=ephem.constellation(ephem.Uranus(datetime.datetime.now()))
    elif p_planet.lower()=='neptune':
        ret=ephem.constellation(ephem.Neptune(datetime.datetime.now()))
    elif p_planet.lower()=='sun':
        ret=ephem.constellation(ephem.Sun(datetime.datetime.now()))
    elif p_planet.lower()=='moon':
        ret=ephem.constellation(ephem.Moon(datetime.datetime.now()))
    elif p_planet.lower()=='earth':
        ret=ephem.constellation(ephem.Earth(datetime.datetime.now()))
    elif p_planet.lower()=='mercury':
        ret=ephem.constellation(ephem.Mercury(datetime.datetime.now()))

    update.message.reply_text('Планета '+p_planet+' находится в созвездии '+ret[1])
    

def talk_to_me(bot, update):
    user_text=update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot=Updater("596268584:AAHjhVKfTgGCoSs4Xm54VkLMPzU9k0-061E", request_kwargs=PROXY)
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start", great_user))
    dp.add_handler(CommandHandler("planet", planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()