from aiogram.fsm.state import State, StatesGroup
from .utils import *

class SendEmailSteps(StatesGroup):
    topic   = State()
    content = State()
    email   = State()

class NewTopic(StatesGroup):
    topic = State()

class NewChat(StatesGroup):
    chat = State()

class NewChannel(StatesGroup):
    features = State()
    topics   = State()

class NewChatMember(StatesGroup):
    uid    = State()
    commit = State()

class Donors(StatesGroup):
    channels = State()