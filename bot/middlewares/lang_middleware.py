from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

import os
from typing import Dict, Any, Callable, Awaitable
from dotenv import load_dotenv
from ..database.languages import LanguagesDatabase


class LangMiddleware(BaseMiddleware):
    """Middleware to determine user's set language."""
    
    async def __call__(self, 
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]) -> Any:

        target_user_language = await LanguagesDatabase.get_language(event.from_user.id)
