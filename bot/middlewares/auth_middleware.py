from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

import os
from typing import Dict, Any, Callable, Awaitable
from dotenv import load_dotenv


class AuthMiddleware(BaseMiddleware):

    async def __call__(self, 
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]) -> Any:
        
        load_dotenv()
        if event.from_user.id != 0:
            return await handler(event, data)