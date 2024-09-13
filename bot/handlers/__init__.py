# Aiogram imports
from aiogram import Router

# Project imports
from .admin_handlers import admin_router
from .neuro_handlers import neuro_router
from .free_handlers import free_router
from .chat_handlers import chat_router
from .channel_handlers import channel_router

from ..middlewares.sub_middleware import SubMiddleware


main_router = Router()
main_router.include_routers(free_router, 
                            chat_router,
                            channel_router,
                            admin_router)
main_router.message.middleware(SubMiddleware())