import telebot 

bot = telebot.TeleBot('TOKEN') # токен бота

# // start - команда, яка запускає бота
@bot.message_handler(commands = ['start']) #реакція чат бота 
                                         #на стартову команду
def start_message(message):
    bot.send_message(message.chat.id, 'Вітаю! Я чат-бот, який може реагувати на різні запити. Напишіть мені щось!')

# // github - команда, яка надсилає посилання на GitHub
@bot.message_handler(commands = ['github'])
def github_message(message):
    bot.send_message(message.chat.id, 'GitHub: https://github.com/YaroslavMyronenko/SPL_Lab/tree/master/Lab_8')

# Функція для надсилання фото мотоцикла Yamaha MT-09
def get_yamaha(message):
    bot.send_message(message.chat.id, 'Yamaha MT-09')
    bot.send_photo(message.chat.id, 'https://mir-s3-cdn-cf.behance.net/projects/404/480aa5118321869.Y3JvcCwzOTk5LDMxMjgsMCwyMTE4.jpg')

# Функція для надсилання фото мотоцикла Honda Cbf 600
def get_honda(message):    
    bot.send_photo(message.chat.id, 'https://upload.wikimedia.org/wikipedia/commons/2/23/Cbf_600_n_for_wiki.JPG', caption="Honda Cbf 600")   

# коли в чат надіслано текст yamaha виводить підтис а потім фото мотоцикла
@bot.message_handler(func = lambda message: message.text.lower() == "yamaha") #реакція чат бота
def yamaha_message(message):
    get_yamaha(message) #функція для надсилання фото
    
# коли в чат надіслано текст honda виводить фото мотоцикла з підписом 
@bot.message_handler(func = lambda message: message.text.lower() == "honda") #реакція чат бота
def honda_message(message):    
    get_honda(message)
    
# // moto - команда, яка надсилає фото мотоциклів
@bot.message_handler(commands = ['moto']) #реакція чат бота
def moto_message(message):
    get_honda(message) #функція для надсилання фото
    get_yamaha(message) #функція для надсилання фото
        
# // sticker - команда, яка надсилає стікер
@bot.message_handler(commands = ['sticker']) #реакція чат бота
def bike_sticker(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANJaCZrJq1EnltWGQ4tVixkFTwuJGQAAhwbAAIdVTBIb1SXCROygI42BA') #стикер

# коли в чат надіслано стікер, бот відповідає file_id стікера
@bot.message_handler(content_types=['sticker'])
def get_sticker_id(message):
    bot.send_message(message.chat.id, f"file_id стікера: {message.sticker.file_id}")

# функцція для надсилання анімації з підписом
def fox_gif(message):
    bot.send_animation(message.chat.id, 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3ljMHNpd2NlMmRvZGE5bjQxZThpZWZpNmJ6bHZudTkwOHA2ejRkMiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/XijnjGLwbq5u8/giphy.gif') #анімашка)
    bot.send_message(message.chat.id, 'fox') #підпис до анімації

# // fox - команда, яка надсилає анімацію з підписом
@bot.message_handler(commands = ['fox']) #реакція чат бота
def fox_command(message):
    fox_gif(message)

# коли в чат надіслано текст fox, бот відповідає анімацією з підписом
@bot.message_handler(func = lambda message: message.text.lower() == "fox") #реакція чат бота 
def fox_text(message): #надіслати анімацію з підписом   
    fox_gif(message)

# Функція для надсилання аудіо
def audio(message):
    bot.send_audio(message.chat.id, 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3') #надіслати аудіо 
    
# Функція для надсилання відео
def video(message):
    bot.send_video(message.chat.id, 'https://filesamples.com/samples/video/mp4/sample_640x360.mp4')

# коли в чат надіслано текст track, бот відповідає аудіо
@bot.message_handler(func = lambda message: message.text.lower() == "track") #реакція чат бота
def get_track(message):
    audio(message)
        
# коли в чат надіслано текст video, бот відповідає відео
@bot.message_handler(func = lambda message: message.text.lower() == "video") #реакція чат бота  
def get_video(message):
    video(message)
    
# // film - команда, яка надсилає аудіо та відео
@bot.message_handler(commands = ['film']) #реакція чат бота
def audio_video(message):
    audio(message)
    video(message)

# // help - команда, яка надсилає список команд
@bot.message_handler(commands = ['help']) #реакція чат бота
def help_message(message):
    bot.send_message(message.chat.id, '🆘 Список команд:\n'
        '/start - Вітання\n'
        '/help - допомога\n'
        '/moto - надіслати фото мотоциклів\n'
        '/sticker - надіслати стікер\n'
        '/github - Гітхаб з лаб 8\n'
        '/fox - надіслати анімацію з підписом\n'
        '/film - надіслати аудіо та відео\n'
        'Написавши в чат слово "fox" ви отримаєте анімацію з підписом\n'
        'Написавши в чат слово "track" ви отримаєте аудіо\n'
        'Написавши в чат слово "video" ви отримаєте відео\n'
        'Написавши в чат слово "yamaha" ви отримаєте фото мотоцикла Yamaha MT-09\n'
        'Написавши в чат слово "honda" ви отримаєте фото мотоцикла Honda Cbf 600\n'
        'Надіславши стікер, ви отримаєте його file_id\n'
        )
    
bot.polling(none_stop=True) # необхідно, щоб бот не вимкнувся відразу 
