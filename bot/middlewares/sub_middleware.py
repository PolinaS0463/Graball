from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from ..text.ru import BaseInfoText
from ..utils import user_not_left
from ..keyboards.ru import graball_channel
from ..settings import GRABALL_CHANNEL_USERNAME, ADMIN_CHANNEL_USERNAME
from typing import Dict, Any, Callable, Awaitable


class SubMiddleware(BaseMiddleware):

    async def __call__(self, 
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]) -> Any:
        
        if await user_not_left(GRABALL_CHANNEL_USERNAME, event, event.bot):
            return await handler(event, data)
        else:
            await event.answer(text=BaseInfoText.subscribe_first, reply_markup=graball_channel)
