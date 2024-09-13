from aiogram import Bot, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, CallbackQuery, ChatPermissions, ContentType

from datetime import datetime, timedelta

from ..keyboards.ru import *
from ..text.ru import ManagingChatText, UtilsText
from ..utils import is_admin, process_period
from ..fsm import NewChatMember

chat_router = Router()
chat_router.message.filter(F.chat.type != "private")

    
# ======================
# NOT AUTOMATIC MANAGING
# ======================

# To ban a user /
# Чтобы заблокировать пользователя
# --------------------------------------------
@chat_router.message(Command('ban'))
async def cmd_ban(message: Message, command: CommandObject, bot: Bot):
    if message.reply_to_message:
        if await is_admin(message, bot):
            period = reason = None
            cmd_args_list = command.args.split()

            if len(cmd_args_list) == 2:
                reason = cmd_args_list[1]
                period = await process_period(command.args.split())
            else: 
                reason = cmd_args_list[0] 

            await bot.ban_chat_member(chat_id=message.chat.id, 
                                      user_id=message.reply_to_message.from_user.id,
                                      until_date=period)
            await message.answer(text=await ManagingChatText.user_banned(message.reply_to_message.from_user.username,
                                                                         message.from_user.id,
                                                                         reason=reason,
                                                                         until=await UtilsText.process_period_text(period)), parse_mode='html')
        else:
            await message.answer(text=await ManagingChatText.not_admin_to_commit(message.from_user.id), parse_mode='html')
        
    else:
        await message.answer(text=ManagingChatText.user_not_found, parse_mode='html')
# --------------------------------------------

# To unban a user /
# Чтобы разблокировать пользователя
# --------------------------------------------
@chat_router.message(Command('unban'))
async def cmd_unban(message: Message, bot: Bot):
    if message.reply_to_message:
        if await is_admin(message, bot):
            await bot.unban_chat_member(chat_id=message.chat.id, 
                                        user_id=message.reply_to_message.from_user.id,
                                        only_if_banned=True)
            await message.answer(text=await ManagingChatText.user_unbanned(message.reply_to_message.from_user.id,
                                                                           message.from_user.id), parse_mode='html')
        else:
            await message.answer(text=await ManagingChatText.not_admin_to_commit(message.from_user.id), parse_mode='html')
    else:
        await message.answer(text=ManagingChatText.user_not_found, parse_mode='html')
# --------------------------------------------

# To mute a user /
# Чтобы заглушить пользователя
# --------------------------------------------
@chat_router.message(Command('mute'))
async def cmd_mute(message: Message, command: CommandObject, bot: Bot):
    if message.reply_to_message:
        if await is_admin(message, bot):
            await bot.restrict_chat_member(chat_id=message.chat.id,
                                           user_id=message.reply_to_message.from_user.id,
                                           permissions=ChatPermissions(can_send_messages=False))
            await message.answer(text=await ManagingChatText.user_muted(message.reply_to_message.from_user.id,
                                                                        message.from_user.id,
                                                                        'r',
                                                                        'r'), parse_mode='html')
        else:
            await message.answer(text=await ManagingChatText.not_admin_to_commit(message.from_user.id), parse_mode='html')
    else:
        await message.answer(text=ManagingChatText.user_not_found, parse_mode='html')
# --------------------------------------------     

# To unmute a user /
# Чтобы снять ограничения с пользователя
# --------------------------------------------
@chat_router.message(Command('unmute'))
async def cmd_unmute(message: Message, command: CommandObject, bot: Bot):
    if message.reply_to_message:
        if await is_admin(message, bot):
            await bot.restrict_chat_member(chat_id=message.chat.id,
                                           user_id=message.reply_to_message.from_user.id,
                                           permissions=ChatPermissions(can_send_messages=True,
                                                                       can_send_other_messages=True))
            await message.answer(text=await ManagingChatText.user_unmuted(message.reply_to_message.from_user.id,
                                                                          message.from_user.id), parse_mode='html')
        else:
            await message.answer(text=await ManagingChatText.not_admin_to_commit(message.from_user.id), parse_mode='html')
    else:
        await message.answer(text=ManagingChatText.user_not_found, parse_mode='html')
# --------------------------------------------

# ==================
# AUTOMATIC MANAGING
# ==================


@chat_router.message(F.type==ContentType.NEW_CHAT_MEMBERS)
async def on_new_chat_member_1(message: Message, state: FSMContext):
    await message.answer(text=await ManagingChatText.on_new_user(message.from_user.username,
                                                                 message.chat.title), reply_markup=not_a_bot)
    await state.update_data(uid=message.from_user.id)
    remaining_time = timedelta(seconds=30)
    finish_time = datetime.now() + remaining_time
    await state.set_state(NewChatMember.commit)
    
@chat_router.callback_query(NewChatMember.commit)
async def on_new_chat_member_1(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data['uid'] == callback.from_user.id:
        await callback.message.delete()
    