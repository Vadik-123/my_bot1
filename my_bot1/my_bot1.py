import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('3231596323c89f2cac873949f944c594', config_dict)
mgr = owm.weather_manager()
bot = telebot.TeleBot('1882322249:AAEFHHnKpCSjD3UoaoqS6I8HOpq5VxfJHnA')


@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет, я бот, который показывает тебе погоду в любом городе.\n"
                                      "Вся информация берётся с сайта https://openweathermap.org\n"
                                      "К сожалению, это все мои функции\n"
                                      "Если есть какие-либо вопросы или советы - пиши мне\nhttps://t.me/hello_nigger.")
    bot.send_message(message.chat.id, "Чтобы узнать погоду, напиши\n/weather")


@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.chat.id, "Чтобы выбрать город, пиши так (без ковычек) - 'Москва'")

    @bot.message_handler(content_types=['text'])
    def city(message):
        try:
            observation = mgr.weather_at_place(message.text)
            w = observation.weather
            # температура
            temp = w.temperature('celsius')
            temp_real = temp['temp']
            temp_for_people = temp['feels_like']
            t_max = temp['temp_max']
            t_min = temp['temp_min']
            # влажность
            humi = w.humidity
            # статус
            det = w.detailed_status
            pogoda = "Максимальная температура " + str(t_max) + "℃\nСредняя температура " + str(
                temp_real) + "℃\nМинимальная температура " + str(t_min) + "℃\nОщущается " + str(
                temp_for_people) + "℃\nВлажность " + str(humi) + "%\nСтатус - " + str(det) + "."
            if det == 'переменная облачность':
                bot.send_message(message.chat.id, pogoda)
                sti = open('перемен.tgs', 'rb')
                bot.send_sticker(message.chat.id, sti)
            elif det == 'облачно с прояснениями':
                bot.send_message(message.chat.id, pogoda)
                sti = open('прояснения.tgs', 'rb')
                bot.send_sticker(message.chat.id, sti)
            elif det == 'пасмурно':
                bot.send_message(message.chat.id, pogoda)
                sti = open('пасмурно.tgs', 'rb')
                bot.send_sticker(message.chat.id, sti)
            elif det == 'небольшая облачность':
                bot.send_message(message.chat.id, pogoda)
                sti = open('неболобл.tgs', 'rb')
                bot.send_sticker(message.chat.id, sti)
            elif det == 'ясно':
                bot.send_message(message.chat.id, pogoda)
                sti = open('ясно.tgs', 'rb')
                bot.send_sticker(message.chat.id, sti)
            elif det == 'дождь':
                bot.send_message(message.chat.id, pogoda)
                sti = open('дождь.tgs', 'rb')
                bot.send_sticker(message.chat.id, sti)
            elif det == 'мгла':
                bot.send_message(message.chat.id, pogoda)
                sti = open('мгла.tgs', 'rb')
                bot.send_sticker(message.chat.id, sti)
            elif det == 'небольшой дождь' or det == 'небольшая морось':
                bot.send_message(message.chat.id, pogoda)
                sti = open('неболдож.tgs', 'rb')
                bot.send_sticker(message.chat.id, sti)
        except:
            bot.send_message(message.chat.id, "Вы ввели город, которого нет в базе\nВыберите город заново.")


bot.polling(none_stop=True, interval=0)
