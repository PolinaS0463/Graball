from aiogram.types import (ReplyKeyboardMarkup, 
                           KeyboardButton, 
                           InlineKeyboardMarkup, 
                           InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.types import KeyboardButtonRequestChat


features = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Новый канал / чат'), KeyboardButton(text='Каналы / чаты')], 
    [KeyboardButton(text='Автоматизация'), KeyboardButton(text='Режим нейросети')],
    [KeyboardButton(text='Настройки'), KeyboardButton(text='Изменить язык')],
    [KeyboardButton(text='Связаться с командой разработчиков!')]], resize_keyboard=True, one_time_keyboard=False)

add_bot_features = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ведение канала', callback_data='manage_channel')],
    [InlineKeyboardButton(text='Статистика', callback_data='statistics')],
    [InlineKeyboardButton(text='Настроить позже >>', callback_data='cancel')]])

channel_topics = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='IT 🧑‍💻', callback_data='topic_opt_1'),
     InlineKeyboardButton(text='Книги 📚', callback_data='topic_opt_2')],
    [InlineKeyboardButton(text='Природа 🌿', callback_data='topic_opt_3'),
     InlineKeyboardButton(text='Искусство 🎭', callback_data='topic_opt_4')],
    [InlineKeyboardButton(text='Дизайн 📱', callback_data='topic_opt_5'),
     InlineKeyboardButton(text='Здоровье 🍎', callback_data='topic_opt_6')],
    [InlineKeyboardButton(text='Наука 🧪', callback_data='topic_opt_7'),
     InlineKeyboardButton(text='Языки 🇬🇧🇩🇪🇫🇷', callback_data='topic_opt_8')],
    [InlineKeyboardButton(text='Шоубиз 🌟', callback_data='topic_opt_9'),
     InlineKeyboardButton(text='Право ⚖️', callback_data='topic_opt_10')],
    [InlineKeyboardButton(text='География 🌎', callback_data='topic_opt_11'),
     InlineKeyboardButton(text='Биология 🧬', callback_data='topic_opt_12')],
    [InlineKeyboardButton(text='История 👑', callback_data='topic_opt_13'),
     InlineKeyboardButton(text='Химия ⚛️', callback_data='topic_opt_14')],
    [InlineKeyboardButton(text='Математика ♾️', callback_data='topic_opt_15'),
     InlineKeyboardButton(text='Физика ☣️', callback_data='topic_opt_16')],
    [InlineKeyboardButton(text='Эстетика 💎', callback_data='topic_opt_17'),
     InlineKeyboardButton(text='Учеба 🕰️', callback_data='topic_opt_18')],
    [InlineKeyboardButton(text='Настроить позже >>', callback_data='cancel')],
    [InlineKeyboardButton(text='Добавить каналы-доноры самому ❓', callback_data='donors')]])

contact = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отправить', callback_data='contact_proceed')]])

chat_or_channel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Чат', callback_data='new_chat')],
    [InlineKeyboardButton(text='Канал', callback_data='new_channel')]
])

send_chat = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить', request_chat=KeyboardButtonRequestChat(
        request_id=1, chat_is_channel=True, request_title=True, request_username=True
    ))]], 
    resize_keyboard=True, one_time_keyboard=True)

send_chats = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить', request_chat=KeyboardButtonRequestChat(
        request_id=1, chat_is_channel=True, request_title=True, request_username=True
    ))],
    [KeyboardButton(text='Готово!')]], 
    resize_keyboard=True, one_time_keyboard=True)

contribution = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Python Developer', callback_data='python_developer')],
    [InlineKeyboardButton(text='Переводчик', callback_data='translator')]
])

select_email_topic = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Проблемы с подпиской', callback_data='opt1')],
    [InlineKeyboardButton(text='Не работает ИИ (нейросеть)', callback_data='opt2')],
    [InlineKeyboardButton(text='Проблемы с функционалом', callback_data='opt3')],
    [InlineKeyboardButton(text='Бот отвечает слишком медленно', callback_data='opt4')],
    [InlineKeyboardButton(text='Предложить новые функции', callback_data='opt5')],
    [InlineKeyboardButton(text='Поблагодарить команду разработчиков :)', callback_data='opt6')],
    [InlineKeyboardButton(text='Другое', callback_data='other')],
])

not_a_bot = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Я не бот', callback_data='not_a_bot')]
])

async def add_feature(feature: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Подключить', callback_data=f'add_{feature}')]])