from aiogram.types import InlineKeyboardMarkup

from dataclasses import dataclass


class Pattern:
    images:  list[str] | None
    content: str | None
    buttons: InlineKeyboardMarkup | None

    async def rewrite_content(self) -> None:
        ...

    async def remove_buttons(self) -> None:
        ...
    