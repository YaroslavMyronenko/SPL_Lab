import telebot
from telebot import types
from currency_converter import CurrencyConverter

bot = telebot.TeleBot('8028050406:AAFQXIET6m0p_nTqPdwVUG7tZf9rVMsugEE') # токен бота
currency = CurrencyConverter()
amount = 0

# команда /start ждя привітання
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'👋Привіт, {message.from_user.first_name}! Я бот 🤖 для конвертації валют\n' 
                     '💱 Я допоможу тобі дізнатися курс валют, а також конвертувати одну валюту в іншу\n'
                     '▶ Введи /convert, щоб конвертувати валюти або, /help щоб дізнатися як зі мною працювати\n')

# команда /convert для конвертації валют
@bot.message_handler(commands= ['convert'])
def convert(message):
    bot.send_message(message.chat.id, '💰 Введіть суму для конвертації')
    bot.register_next_step_handler(message, summa)

# функція для обробки введеної суми
def summa(message):
    global amount
    try:
        amount = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, '❗ Введіть ціле число або розділене крапкою, наприклад 12.5')
        bot.register_next_step_handler(message, summa)
        return
    
    if amount > 0:
        murkup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton('💵 USD → EUR', callback_data='USD/EUR')    
        button2 = types.InlineKeyboardButton('💶 EUR → USD', callback_data='EUR/USD')
        button3 = types.InlineKeyboardButton('💲 USD → PLN', callback_data='USD/PLN')
        button4 = types.InlineKeyboardButton('💴 USD → JPY', callback_data='USD/JPY')
        button5 = types.InlineKeyboardButton('🔄 Інше значення', callback_data='else')
        murkup.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, '🔽 Виберіть пару валют для конвертації', reply_markup=murkup)
    else:
        bot.send_message(message.chat.id, 'Введіть коректну суму для конвертації')
        bot.register_next_step_handler(message, summa)

# функція для обробки натискання кнопок
@bot.callback_query_handler(func=lambda call: True)
def collback(call):
    if call.data != 'else':
        vallue = call.data.split('/')
        result = currency.convert(amount, vallue[0], vallue[1])
        bot.send_message(call.message.chat.id, f"✅ {amount} {vallue[0]} = {round(result, 2)} {vallue[1]},\n"
                        "Можете заново ввести суму")
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введіть іншу пару валют через слеш, наприклад USD/EUR')
        bot.register_next_step_handler(call.message, mycurrency)
        
# функція для обробки введеної пари валют
def mycurrency(message):
    value = message.text.upper().split('/')
    try:
        result = currency.convert(amount, value[0], value[1])
        bot.send_message(message.chat.id, f"✅ {amount} {value[0]} = {round(result, 2)} {value[1]},\n"
                        "Можете заново ввести суму")
        bot.register_next_step_handler(message, summa)
    except Exception as e:
        bot.send_message(message.chat.id, '❗ Введіть коректну пару валют через слеш, наприклад USD/EUR')
        bot.register_next_step_handler(message, mycurrency)

# команда /exchange для отримання курсу валют
@bot.message_handler(commands = ['exchange']) 
def exchange(message):
    try:
        # currency.currencies - всі підтримувані валюти
        all_rates = []
        for code in sorted(currency.currencies):
            if code != 'USD':  # не показуємо курс USD до USD
                try:
                    rate = currency.convert(1, 'USD', code)
                    all_rates.append(f"USD → {code}: {round(rate, 2)}")
                except Exception:
                    continue  # якщо для якоїсь валюти немає курсу, пропускаємо
        rates_text = '\n'.join(all_rates)
        bot.send_message(message.chat.id, f'📈 Курс USD до всіх підтримуваних валют:\n{rates_text}')
    except Exception as e:
        bot.send_message(message.chat.id, '❌ Не вдалося отримати курс валют. Спробуйте пізніше.')
       
# команда /help для отримання довідки 
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Я можу конвертувати валюти та показати курс валют.\n'
                     'Введіть /convert, щоб конвертувати валюти\n'
                     'Введіть /exchange, щоб дізнатися курс валют\n'
                     'Після введення команди /convert, я запитаю у вас суму для конвертації.\n'
                     'Потім ви зможете вибрати пару валют для конвертації.\n'
                     'Якщо ви хочете ввести свою пару валют, введіть її у форматі "USD/EUR".\n'
                     'Я підтримую конвертацію між багатьма валютами, такими як USD, EUR, PLN, JPY та іншими.\n')        

bot.polling(none_stop=True)