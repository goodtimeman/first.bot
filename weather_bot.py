from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import telebot


owm = OWM('fa58f7d14ffa8802beed83b64e464721')
mgr = owm.weather_manager()
bot = telebot.TeleBot("1411055913:AAH4nbNOhQPUOOYMZVuhxGrTM8eT8UUE9HM")
@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    result =f'Сегодня в городе {message.text}\n{temp} градусов \n{w.detailed_status}\n'
    if int(temp) <= 10:
        result += ('Дубак')
    elif 10 < int(temp) < 20:
        result +=('Накинь куртец')
    else:
        result +=('Расчехляй шорты!')
    bot.send_message(message.chat.id, result)

bot.polling(none_stop=True)