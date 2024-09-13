from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from typing import Dict, Any, Callable, Awaitable



class AuthMiddleware(BaseMiddleware):

    async def __call__(self, 
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]) -> Any:
        
        if event.from_user.id != 0:
            return await handler(event, data)