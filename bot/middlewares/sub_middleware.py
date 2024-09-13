from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from typing import Dict, Any, Callable, Awaitable
from ..settings import GRABALL_CHANNEL_ID



class SubMiddleware(BaseMiddleware):
    async def __call__(self, 
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]) -> Any:
        
        status = await event.bot.get_chat_member(chat_id=GRABALL_CHANNEL_ID, user_id=event.from_user.id)
        if status['status'] != 'left':
            return await handler(event, data)
        else:
            await event.answer(text='text')