import telebot 
from pyowm import OWM
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot('7673865383:AAH0PaYCKkATUftdflkaVykNCEkwQYlCkOM')
config_dict = get_default_config()
config_dict['language'] = 'ua' 
owm = OWM( '0f8480e94c08f6fa663ead777cd2ee53', config_dict  )

@bot.message_handler(commands=['start']) #реакція чат бота на стартову команду
def start_message(message):
    bot.send_message(message.chat.id, 'Для перевірки погоди введи команду /city')

@bot.message_handler(commands=['city']) #команда для отримання початкових даних
def cmd_city(message):
    send = bot.send_message(message.chat.id, 'Введи місто')
    bot.register_next_step_handler(send, city)

def city(message): #основна робота з декількома варіантами в залежності від результату
    bot.send_message(message.chat.id, 'Дізнаюсь погодні умови в місті {city}'.format(city=message.text))

    data = message.text
    mgr = owm.weather_manager()
    try:
        observation = mgr.weather_at_place(data)
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        t = w.temperature('celsius')['temp']

        answer = f"В місті {message.text} зараз {w.detailed_status} \n"
        answer += f"Приблизна температура {round(t)} ℃\n\n"

        if t < 0:
            answer += 'Зараз температура нижче нуля, одягайся тепліше!'
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBNGgqSVY5Tss_Hu-ADYdUaTeigfN2AAKGAAP3AsgPDkBo3fYTYH02BA') 
        elif t < 15:
            answer += 'Зараз прохолодно, варто тепліше одягтися!' 
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBMGgqSP-MZVY7O1tqlcr6b28dv-uLAAKgCQAC2K-ZSkeNePSDa2AnNgQ') 
        else:
            answer += 'Зараз досить тепло, можна одягтися легко!'
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBMmgqSRmVJEIGsb4_JaZohzsL_yAUAAJ-DAAC6-nRSIJMsuVXQZfvNgQ') 
            
        bot.send_message(message.chat.id, answer)
    except Exception:
        bot.send_message(message.chat.id, 'Не можу знайти місто {city}'.format(city=message.text))
        bot.register_next_step_handler(message, city)

# /weather - команда, яка надсилає погоду в таких містах як Київ, Львів, Одеса, Кропивницький
@bot.message_handler(commands=['weather']) #реакція чат бота
def weather_message(message):
    data = ['Київ', 'Львів', 'Одеса', 'Кропивницький']
    mgr = owm.weather_manager()      
    
    answer = f"Погода в містах:\n"
    for city in data:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        t = w.temperature('celsius')['temp']
        answer += f"{city}: {w.detailed_status}, температура: {round(t)} ℃\n"
        
    bot.send_message(message.chat.id, answer)
    
# / help - команда, яка надсилає список команд
@bot.message_handler(commands=['help']) #реакція чат бота
def help_message(message):
    bot.send_message(message.chat.id, '🆘 Список команд:\n'
        '/start - Вітання\n'
        '/help - допомога\n'
        '/city - перевірка погоди в місті\n'
        '/weather - перевірка погоди в декількох містах\n'
        'Введи місто, щоб дізнатися погоду в ньому')
      
bot.polling(none_stop=True) # необхідно, щоб бот не вимкнувся одразу
