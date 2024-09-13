from aiogram.types import (ReplyKeyboardMarkup, 
                           KeyboardButton, 
                           InlineKeyboardMarkup, 
                           InlineKeyboardButton)


other_features = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='New chat'), 
     KeyboardButton(text='Chats')],
    [KeyboardButton(text='New channel'), 
     KeyboardButton(text='Channels')], 
     [KeyboardButton(text='Automatization')],
     [KeyboardButton(text='Useful materials')],
    [KeyboardButton(text='Settings'), 
     KeyboardButton(text='Neural network mode'), 
     KeyboardButton(text='Change language')],
    [KeyboardButton(text='Contact the development team!')]
])

add_bot_features = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Managing a channel', callback_data='manage_channel')],
    [InlineKeyboardButton(text='Statistics', callback_data='statistics')],
    [InlineKeyboardButton(text='Configure later >>', callback_data='cancel')],
])

channel_topics = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='IT 🧑‍💻'),
     InlineKeyboardButton(text='Books 📚')],
    [InlineKeyboardButton(text='Nature 🌿'),
     InlineKeyboardButton(text='Art 🎭')],
    [InlineKeyboardButton(text='Design 📱'),
     InlineKeyboardButton(text='Health 🍎')],
    [InlineKeyboardButton(text='Science 🧪'),
     InlineKeyboardButton(text='Languages 🇬🇧🇩🇪🇫🇷')],
    [InlineKeyboardButton(text='Showbiz 🌟'),
     InlineKeyboardButton(text='Law ⚖️')],
    [InlineKeyboardButton(text='Geography 🌎'),
     InlineKeyboardButton(text='Biology 🧬')],
    [InlineKeyboardButton(text='History 👑'),
     InlineKeyboardButton(text='Chemistry ⚛️')],
    [InlineKeyboardButton(text='Maths ♾️'),
     InlineKeyboardButton(text='Physics ☣️')],
    [InlineKeyboardButton(text='Aesthetics 💎'),
     InlineKeyboardButton(text='Study 🕰️')],
    [InlineKeyboardButton(text='Configure later >>', callback_data='cancel')]
])

contact = InlineKeyboardMarkup(inline_keyboard=[
    InlineKeyboardButton(text='Contact', callback_data='contact_proceed')
])

choose_email_topic = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Problems with subsribtion')],
    [InlineKeyboardButton(text='AI does not work')],
    [InlineKeyboardButton(text='Problems with functionality')],
    [InlineKeyboardButton(text='Bot answering too slowly')],
    [InlineKeyboardButton(text='Suggest new features')],
    [InlineKeyboardButton(text='Thank the development team :)')],
    [InlineKeyboardButton(text='Other')],
    [InlineKeyboardButton(text='<< Cancel')],
])