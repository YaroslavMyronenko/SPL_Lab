import telebot
from telebot import types
from currency_converter import CurrencyConverter

bot = telebot.TeleBot('8028050406:AAFQXIET6m0p_nTqPdwVUG7tZf9rVMsugEE') # токен бота
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привіт, {message.from_user.first_name}! Я бот для конвертації валют\n' 
                     'Я допоможу тобі дізнатися курс валют, а також конвертувати одну валюту в іншу\n'
                     'Введи /convert, щоб конвертувати валюти або, /help щоб дізнатися як зі мною працювати\n')

@bot.message_handler(commands= ['convert'])
def convert(message):
    bot.send_message(message.chat.id, 'Введіть суму для конвертації')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Введіть число')
        bot.register_next_step_handler(message, summa)
        return
    
    if amount > 0:
        murkup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton('USD/EUR', callback_data='USD/EUR')    
        button2 = types.InlineKeyboardButton('EUR/USD', callback_data='EUR/USD')
        button3 = types.InlineKeyboardButton('USD/UAH', callback_data='USD/UAH')
        button4 = types.InlineKeyboardButton('UAH/USD', callback_data='UAH/USD')
        button5 = types.InlineKeyboardButton('Інше значення', callback_data='else')
        murkup.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, 'Виберіть пару валют для конвертації', reply_markup=murkup)
    else:
        bot.send_message(message.chat.id, 'Введіть коректну суму для конвертації')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func=lambda call: True)
def collback(call):
    vallue = call.data.split('/')
    result = currency.convert(amount, vallue[0], vallue[1])
    bot.send_message(call.message.chat.id, f"{amount} {vallue[0]} = {round(result, 2)} {vallue[1]},\n"
                     "Можете заново ввести суму")
    bot.register_next_step_handler(call.message, summa)

bot.polling(none_stop=True)