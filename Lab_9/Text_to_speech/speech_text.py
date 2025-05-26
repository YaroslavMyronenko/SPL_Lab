import os
import asyncio
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

bot = Bot(token = '7916164042:AAGDTqr0Tpepmd9vw-yoNOzC0RwSoeSF5ig') # токен бота
dp = Dispatcher()

class MyStates(StatesGroup): # стани для управління станами бота
    choose_language = State()
    text_to_voice = State()
    voice_to_text = State()

# Клавіатура для вибору мови
def get_language_keyboard():
    """Клавіатура для вибору мови"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Українська', callback_data='lang_uk')],
        [InlineKeyboardButton(text='Англійська', callback_data='lang_en')]
    ])

# Клавіатура для вибору методу
def get_method_keyboard():
    """Клавіатура для вибору методу перетворення"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='текст в голос', callback_data='text_to_voice')],
        [InlineKeyboardButton(text='голос в текст', callback_data='voice_to_text')]
    ])

@dp.message(CommandStart()) #реакція чат бота на стартову команду
async def start_message(message: Message): # реакція чат бота на команду /start
    await message.answer(f'Вітаю {message.from_user.first_name}! Я бот, який може озвучувати текст або прочитати текст з аудіо чи голосового повідомлення.'
                         '\nКоманда /convert допоможе вам в цьому\n'
                         'Для отримання інструкцій та списку команд використайте /help')

@dp.message(Command('convert')) #реакція чат бота на текстове повідомлення
async def conv(message: Message, state: FSMContext): # реакція чат бота на команду /convert
    await state.clear()
    await message.answer('Оберіть мову:', reply_markup=get_language_keyboard()) # відповідь бота з клавіатурою для вибору мови
    await state.set_state(MyStates.choose_language) # встановлення стану вибору мови

@dp.callback_query(F.data.in_(['lang_uk', 'lang_en']), StateFilter(MyStates.choose_language)) 
async def choose_language(call: CallbackQuery, state: FSMContext): # реакція чат бота на натискання кнопки вибору мови
    lang = 'uk' if call.data == 'lang_uk' else 'en' # визначення мови на основі натиснутої кнопки
    await state.update_data(language=lang) # збереження вибраної мови в стані
    lang_text = 'Українська' if lang == 'uk' else 'Англійська' # текст для відображення вибраної мови
    await call.answer(f'Обрано мову: {lang_text}') 
    await call.message.edit_text(f'Обрана мова: {lang_text}\nОберіть що ви хочете перетворити:', reply_markup=get_method_keyboard()) # зміна тексту повідомлення та відображення клавіатури для вибору методу

@dp.callback_query(F.data == 'text_to_voice') #реакція чат бота на натискання кнопки
async def text_to_voice(call: CallbackQuery, state: FSMContext): # реакція чат бота на натискання кнопки "текст в мову"
    await call.answer('Обрано текст в голос')
    await call.message.delete() # Видалити повідомлення з кнопками
    await call.message.answer('Надішліть текст, який потрібно озвучити') 
    await state.set_state(MyStates.text_to_voice) # встановлення стану перетворення тексту в мову
    
@dp.callback_query(F.data == 'voice_to_text') #реакція чат бота на натискання кнопки
async def voice_to_text(call: CallbackQuery, state: FSMContext):  # реакція чат бота на натискання кнопки "мову в текст"
    await call.answer('Обрано голос в текст') 
    await call.message.delete() # Видалити повідомлення з кнопками
    await call.message.answer('Надішліть голосове повідомлення чи .mp3 файл, який потрібно розпізнати')
    await state.set_state(MyStates.voice_to_text) # встановлення стану перетворення мови в текст

async def process_text_to_voice(message: Message, state: FSMContext): # реакція чат бота на текстове повідомлення
    """Функція для обробки текстового повідомлення та перетворення його в аудіо"""
    converting_messg = await message.answer("⏳ Виконується конвертація тексту в голос...")
    data = await state.get_data() # отримання даних зі стану
    lang = data.get('language', 'uk') # отримання вибраної мови, якщо не вказана, то за замовчуванням українська
    tts = gTTS(text=message.text, lang=lang) # створення об'єкту gTTS для перетворення тексту в мову
    tts.save('output.mp3')
 
    sound = AudioSegment.from_mp3('output.mp3') # завантаження збереженого аудіо
    sound.export('output.ogg', format='ogg', codec='libopus') # конвертація в формат OGG

    voice_file = FSInputFile('output.ogg') # створення об'єкту FSInputFile для відправки аудіо
    await message.answer_voice(voice_file) # відправка голосового повідомлення користувачу

    os.remove('output.mp3') # видалення тимчасового файлу mp3
    os.remove('output.ogg') # видалення тимчасового файлу ogg
    await message.answer('Готово! Текст перетворено в голосове повідомлення')
    await converting_messg.delete()
    
async def process_voice_to_text(message: Message, state: FSMContext): # реакція чат бота на голосове повідомлення
    """Функція для обробки аудіо та розпізнавання тексту """
    converting_messg = await message.answer("⏳ Виконується конвертація аудіо в текст...")
    data = await state.get_data() # отримання даних зі стану
    lang = data.get('language', 'uk') # отримання вибраної мови, якщо не вказана, то за замовчуванням українська
    recog_lang = 'uk-UA' if lang == 'uk' else 'en-US' 
    
    file_id = None # отримання file_id голосового або аудіо повідомлення
    file_ext = None # розширення файлу для збереження
    # Перевіряємо тип повідомлення: voice (ogg) чи audio (mp3)
    if message.voice: # якщо це голосове повідомлення
        file_id = message.voice.file_id # отримання file_id голосового повідомлення
        file_ext = 'ogg' # встановлення розширення файлу як ogg
    elif message.audio: # якщо це аудіофайл
        file_id = message.audio.file_id  # отримання file_id аудіофайлу
        file_ext = 'mp3' # встановлення розширення файлу як mp3
    else:
        await message.answer('Це не голосове повідомлення чи .mp3-файл!')
        return
    
    file_info = await bot.get_file(file_id) # отримання інформації про файл з сервера Telegram
    downloaded_file = await bot.download_file(file_info.file_path) # завантаження файлу з сервера Telegram
 
    with open(f'voice.{file_ext}', 'wb') as new_file: # збереження завантаженого файлу
        new_file.write(downloaded_file.getvalue()) # запис даних у файл

    if file_ext == 'ogg': 
        audio = AudioSegment.from_ogg('voice.ogg') # якщо файл ogg, то завантажуємо його
    else:
        audio = AudioSegment.from_mp3('voice.mp3') # якщо файл mp3, то завантажуємо його
    audio.export('voice.wav', format='wav') # конвертуємо в формат wav для розпізнавання
     
    recognizer = sr.Recognizer() # створення об'єкту Recognizer для розпізнавання голосу
    with sr.AudioFile('voice.wav') as source: # відкриття аудіофайлу для розпізнавання
        audio_data = recognizer.record(source) # зчитування аудіо даних з файлу
        try:
            text = recognizer.recognize_google(audio_data, language=recog_lang) # розпізнавання тексту з аудіо даних
            await message.answer(f'Розпізнаний текст: -> {text}') # відправка розпізнаного тексту користувачу
        except sr.UnknownValueError:
            await message.answer('Не вдалося розпізнати текст з аудіо.')
        except sr.RequestError:
            await message.answer('Помилка сервісу розпізнавання. Спробуйте пізніше.')
    
    await converting_messg.delete()    
    try: # Видаляємо тимчасові файли
        os.remove('voice.wav')
        if os.path.exists('voice.ogg'): 
            os.remove('voice.ogg')
        if os.path.exists('voice.mp3'):
            os.remove('voice.mp3')
    except Exception: # Якщо не вдалося видалити файли, це означеє що вони не існують
        pass
    
@dp.message(StateFilter(MyStates.text_to_voice))  # реакція чат бота на текстове повідомлення
async def handle_text_to_voice(message: Message, state: FSMContext): 
    await process_text_to_voice(message, state) # обробка текстового повідомлення та перетворення його в голосове повідомлення
    await state.clear() # очищення стану після обробки

@dp.message(StateFilter(MyStates.voice_to_text))  # реакція чат бота на голосове повідомлення
async def handle_voice_to_text(message: Message, state: FSMContext): # обробка голосового повідомлення та розпізнавання тексту
    await process_voice_to_text(message, state) # 
    await state.clear() # очищення стану після обробки
    
@dp.message(Command('help'))  # реакція чат бота на команду /help
async def help_message(message: Message):
    await message.answer('Список команд:\n'
                         '/start - почати роботу з ботом\n'
                         '/convert - перетворення тексту в аудіо або навпаки\n'
                         '/help - отримати список команд та інструкцій\n'
                         'Для перетворення тексту в голос або навпаки, використовуйте команду /convert\n'
                         'Після цього оберіть мову та метод перетворення.\n'
                         'Надішліть текст, голосове повідомлення або .mp3 файл, і бот виконає перетворення\n'
                         'Підтримуються українська та англійська мови\n'
                         )

async def main():  # основна функція для запуску бота
    await dp.start_polling(bot) # запуск бота

if __name__ == "__main__": # точка входу в програму 
    asyncio.run(main()) # запуск основної функції



