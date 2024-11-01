from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.enums.chat_member_status import ChatMemberStatus

import os
import aiosmtplib
from datetime import timedelta
from email.mime.text import MIMEText
from email.header import Header
from dotenv import load_dotenv

async def collect_all(message: Message):
    return {
        'username' : message.from_user.username,
        'full_name' : message.from_user.full_name,
        'user_telegram_id' : message.from_user.id,
        'channels' : '/channels', # TODO
        'chats' : '/chats', # TODO
        'subscription' : None, # TODO
        'free_hours_left' : None,
        'password' : '/personal_data', # TODO
        'active_sessions' : '/sessions'
        }


async def send_email(topic: str, content: str, email: str):
    load_dotenv()
    login = os.getenv('GMAIL_LOGIN')
    password = os.getenv('GMAIL_PASSWORD')

    email = MIMEText(content, 'plain', 'utf-8')
    email['Subject'] = Header(topic, 'utf-8')
    email['From'] = login
    email['To'] = login

    con = aiosmtplib.SMTP(host='smtp.gmail.com', port=587)
    con.ehlo() # Not necessary
    con.starttls()
    con.ehlo() # Not necessary
    con.login(login, password)
    con.sendmail(email['From'], login, email.as_string())
    con.quit()


async def is_admin(event: Message, bot: Bot) -> bool:
    member = await bot.get_chat_member(event.chat.id, event.from_user.id)
    if member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
        return True
    return False

async def user_not_left(target_channel_username: int, event: Message, bot: Bot) -> bool:
    member = await bot.get_chat_member(target_channel_username, event.from_user.id)
    if member.status != ChatMemberStatus.LEFT:
        return True
    return False

async def process_period(period: str) -> timedelta | None:
    period_text = period[1]
    match period_text:
        case 'm':
            return timedelta(minutes=float(period_text[0]))
        case 'h':
            return timedelta(hours=float(period_text[0]))
        case 'd':
            return timedelta(days=float(period_text[0]))
        case 'w': 
            return timedelta(weeks=float(period_text[0]))
        case _:
            return None
