from aiogram.types import InlineKeyboardMarkup
import re


class Pattern:
    images:  list[str] | None
    content: str | None
    buttons: InlineKeyboardMarkup | None

    async def remove_pattern_text(self, pattern: str) -> None:
        pattern_words = pattern.split(' ')
        for word in pattern_words:
            re.sub(word, r'',Pattern.content)

    async def rewrite_content(self) -> None:
        ...

    async def remove_buttons(self) -> None:
        Pattern.buttons = None

    
    