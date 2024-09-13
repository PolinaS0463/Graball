# Aiogram imports
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery




admin_router = Router()

@admin_router.message(F.text == 'Статистика')
@admin_router.message(Command('statistics'))
async def cmd_statistics(message: Message):
    ...


@admin_router.message(F.text == 'Рассылка')
@admin_router.message(Command('set_newsletter'))
async def cmd_set_newsletter(message: Message):
    ...


@admin_router.message(F.text == 'Подписка на ChatGPT')
@admin_router.message(Command('chatgpt_sub'))
async def cmd_chatgpt_sub(message: Message):
    ...