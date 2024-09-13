from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, Chat, ReactionTypeEmoji
from aiogram.fsm.context import FSMContext


from ..text.ru import *

neuro_router = Router()

@neuro_router.message(F.text == 'Режим нейросети')
@neuro_router.message(F.text == 'Neural network mode')
@neuro_router.message(Command('neuro_mode'))
async def cmd_neuro_mode(message: Message):
    await message.answer(text=Neuro.neuro_switch, parse_mode='html')


