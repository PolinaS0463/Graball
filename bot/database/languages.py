import redis.asyncio as aioredis

from ..config import RedisSettings


class LanguagesDatabase:
    """A database for keeping users's languages. Based on asynchronous Redis"""

    @staticmethod
    async def set_language(user_telegram_id: int, value: int):
        """Setting a user's language"""
        async with aioredis.Redis(host=RedisSettings.host, port=RedisSettings.port, db=RedisSettings.db,
                                  decode_responses=True) as client:
            await client.set(name=user_telegram_id, value=value)

    @staticmethod
    async def get_language(user_telegram_id: int):
        """Getting the language of the target user"""
        async with aioredis.Redis(host=RedisSettings.host, port=RedisSettings.port, db=RedisSettings.db,
                                  decode_responses=True) as client:
            language_code = await client.get(user_telegram_id)
            return language_code