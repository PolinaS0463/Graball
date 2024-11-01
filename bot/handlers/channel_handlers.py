from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, LinkPreviewOptions

from ..keyboards.ru import *
from ..fsm import NewChannel, Donors
from ..text.ru import ManagingChannelText, FunctionsText


channel_router = Router()

@channel_router.message(Command('new_channel'))
async def cmd_new_channel_1(message: Message, state: FSMContext):
    await message.answer(text=ManagingChannelText.start_new_channel, reply_markup=add_bot_features, parse_mode='html')

@channel_router.callback_query(F.data == 'manage_channel')
async def manage_channel(callback: CallbackQuery):
    await callback.message.answer(text=FunctionsText.manage_channel, reply_markup=await add_feature('manage_channel'), parse_mode='html')

@channel_router.callback_query(F.data == 'statistics')
async def statistics(callback: CallbackQuery):
    await callback.message.answer(text=FunctionsText.stat, reply_markup=await add_feature('statistics'), parse_mode='html')

@channel_router.callback_query(F.data == 'add_manage_channel')
async def add_manage_channel_1(callback: CallbackQuery):
    await callback.message.edit_text(text=ManagingChannelText.topics, reply_markup=channel_topics)


@channel_router.callback_query(F.data.regexp(r'topic_opt_[\d]+', mode='fullmatch'))
async def add_topics_1(callback: CallbackQuery):
    topic = None
    markup = callback.message.reply_markup.inline_keyboard
    for button in markup:
        if button[0].callback_data == callback.data:
            topic = button[0].text
    await callback.message.answer(text=await ManagingChannelText.new_topic_added(topic))


@channel_router.callback_query(F.data == 'add_statistics')
async def add_manage_channel_2(callback: CallbackQuery):
    await callback.answer()


@channel_router.callback_query(F.data == 'donors')
async def donors(callback: CallbackQuery):
    await callback.message.edit_text(text=ManagingChannelText.what_are_donors, reply_markup=await add_feature('donors'), parse_mode='html')

@channel_router.callback_query(F.data == 'add_donors')
async def add_donors(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text=ManagingChannelText.send_channels_donors, reply_markup=send_chats)
    await state.set_state(Donors.channels)

@channel_router.message(Donors.channels)
async def add_donors_2(message: Message, state: FSMContext):
    data = await state.get_data()
    if message.text == 'Готово!':
        await message.answer(text=await ManagingChannelText.added_donors(data), parse_mode='html', 
                             link_preview_options=LinkPreviewOptions(is_disabled=True), reply_markup=features)
        await state.clear()
    else:
        if data:
            data['channels'].append(message.chat_shared)
            await state.update_data(channels=data['channels'])
        else: 
            await state.update_data(channels=[message.chat_shared])
    