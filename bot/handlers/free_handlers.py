from aiogram import Router, F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message, CallbackQuery, Chat, ReactionTypeEmoji
from aiogram.fsm.context import FSMContext


from ..text.ru import *
from ..keyboards.ru import *
from ..utils import collect_all, send_email
from ..fsm import *

free_router = Router()

# Start / Старт
# ------------------------------------------
@free_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.react(reaction=[ReactionTypeEmoji(type='emoji', emoji='👏')])
    await message.reply(text=await BaseInfoText.hello(name=message.from_user.first_name), 
                        parse_mode='html', 
                        reply_markup=features)
# ------------------------------------------

# Settings / Настройки
# ------------------------------------------
@free_router.message(F.text == 'Настройки')
@free_router.message(F.text == 'Settings')
@free_router.message(Command('settings'))
async def cmd_settings(message: Message):
    data = await collect_all(message)
    await message.answer(text=await BaseInfoText.render_settings(data))
# ------------------------------------------

# Contact the development team / 
# Связаться с командой разработчиков
# ------------------------------------------
@free_router.message(F.text == 'Связаться с командой разработчиков!')
@free_router.message(F.text == 'Contact the development team!')
@free_router.message(Command('contact'))
async def cmd_contact_1(message: Message):
    await message.answer(text=BaseInfoText.contact_us, reply_markup=contact, parse_mode='html')
    
@free_router.callback_query(F.data == 'contact_proceed')
async def cmd_contact_2(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=BaseInfoText.contact_us_notes)
    await callback.message.answer(text=SendEmailText.select_topic, reply_markup=select_email_topic)
    await state.set_state(SendEmailSteps.topic)

@free_router.callback_query(SendEmailSteps.topic)
async def cmd_contact_3(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'other':
        await callback.message.answer(text=SendEmailText.input_topic)
        await state.set_state(NewTopic.topic)
    else:
        topic = None
        markup = callback.message.reply_markup.inline_keyboard
        for button in markup:
            if button[0].callback_data == callback.data:
                topic = button[0].text
        await callback.message.edit_text(text=await SendEmailText.selected_topic(topic), parse_mode='html')
        await callback.message.answer(text=SendEmailText.input_content)
        await state.update_data(topic=topic)
        await state.set_state(SendEmailSteps.content)

@free_router.message(NewTopic.topic)
async def cmd_contact_4_1(message: Message, state: FSMContext):
    await message.answer(text=await SendEmailText.selected_topic(message.text), parse_mode='html')
    await message.answer(text=SendEmailText.input_content)
    await state.update_data(topic=message.text)
    await state.set_state(SendEmailSteps.content)

@free_router.message(SendEmailSteps.content)
async def cmd_contact_4_2(message: Message, state: FSMContext):
    await state.update_data(content=message.text)
    await message.answer(text=SendEmailText.input_your_email)
    await state.set_state(SendEmailSteps.email)

@free_router.message(SendEmailSteps.email)
async def cmd_contact_5(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    data = await state.get_data()
    await state.clear()
    await message.answer(text=SendEmailText.success)
# ------------------------------------------

# Changing language / Изменение языка
# ------------------------------------------
@free_router.message(F.text == 'Изменить язык')
@free_router.message(F.text == 'Change language')
@free_router.message(Command('change_lang'))
async def cmd_change_language(message: Message, bot: Bot):
    # await bot.cop
    pass

# ------------------------------------------

@free_router.callback_query(F.text == 'channels')
@free_router.message(Command('channels'))
async def cmd_channels(message: Message, command: CommandObject):
    # await message.react(reaction=[ReactionTypeEmoji(type='emoji', emoji='🔥')])
    print(command.args.split(' '))


@free_router.callback_query(F.text == 'chats')
@free_router.message(Command('chats'))
async def cmd_chats(message: Message):
    pass # TODO

    # await message.react(reaction=[ReactionTypeEmoji(type='emoji', emoji='🔥')])