from aiogram.fsm.state import State, StatesGroup
from .utils import *

class SendEmailSteps(StatesGroup):
    topic   = State()
    content = State()
    email   = State()

class NewTopic(StatesGroup):
    topic = State()

class NewChannel(StatesGroup):
    features = State()
    topics   = State()

class Donors(StatesGroup):
    channels = State()