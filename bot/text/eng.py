from dataclasses import dataclass
from aiogram.types import ChatShared

start_new_channel = '''Hey, so I see you added a new channel!
                       Firstly, to make bot able to manage it, you need
                       сделать его админом канала. In case something goes wrong -
                       don't worry, ты всегда сможешь его удалить и у бота больше
                       не будет доступа к твоему каналу!
                       
                       Now I suggest you to select functions our bot will be
                       able to :'''

stat = '''📊 Switch in this feature for your channel and bot will 
          periodically notify you about new likes and comments
          под твоими постами, about new and left subscribers, and
          also will be able to create a statistics dashboard about channel's
          activity during one week / month / half-year!'''

@dataclass
class BaseInfoText:
    adding_chat_or_channel    = 'Adding... a chat or a channel?'
    contact_us                = '✅ Наш инновационный бот всегда в процессе разработки, чтобы работать все более и более качественно для вас! Непростой в реализации функционал требует большого количества сосредоточенности, внимания и профессионализма от наших программистов!\n\nТем не менее, все мы не роботы, и время от времени могут происходить различного вида сбои, особенно при такой нагруженности бота и сложности реализуемого функционала!\n\n‼️ Чтобы мы сразу смогли отреагировать на изменения в работе бота, просим Вас оставлять нам обратную связь! Нам очень важно создать уникальный продукт, который будет упрощать жизнь и работать максимально качественно! Тем более что выявить некоторые уязвимости и недоработки можно только во время прода (реальной работы с пользователями 24/7)!\n\nЕсли Вы хотите написать нам, нажмите на кнопку <b>«Отправить</b> внизу. Мы постараемся как можно скорее ответить на Ваше обращение!'
    contact_us_notes          = '‼️ Пожалуйста, не стоит задавать вопросы по поводу интерфейса бота ‼️\nОб этом подробно разъяснено в самом боте! Также можно почитать документацию на странице проекта!'
    langs                     = 'На данный момент достпуно всего <b>два языка</b>: английский и русский!'
    lang_changed_successfully = '✅ Language changed successfully to <b>English!</b>'
    advertisement             = '💡 Чтобы «заказать» рекламу вашего ресурса, пишите <b>@flamme_ss</b> в Telegram или на почту: graball_bot_team@gmail.com'
    subscribe_first           = 'Before using the bot, please subscribe to our channels!'

    @staticmethod
    async def hello(name: str, users: int = 0, channels: int = 0, chats: int = 0) -> str:
        return f'Привет, <b>{name}!</b>\nЭто <b>«Graball»</b> - инновационный бот-граббер и бот-модератор! <b>Через него вы сможете:</b>\n- Мониторить чаты;\n- Вести каналы;\n- Автоматизировать процессы;\n- Использовать нейросеть <b>ChatGPT</b>;\n\nНам доверяют ❤️‍🩹\nСейчас у нас:\n<b>{users}</b> пользователей 👥\n<b>{channels}</b> каналов 🎙️\n<b>{chats}</b> чатов 📱'

    @staticmethod
    async def render_settings(settings: dict[str]) -> str:
        result = 'Account settings:\n'
        for key, value in settings.items():
            result += f''
        return result
    
    @staticmethod
    async def send_chat_or_channel(text: str) -> str:
        return f'Отлично!\n\nА теперь нажми на кнопку «Отправить» ниже и выбери нужный {text}!'


class NotificationsText:

    @staticmethod
    async def statistics(channel: str, period: str):
        return f'Хэй! Отчет по твоему каналу «{channel}» готов!\nПериод: <b>{period}</b>'

    @staticmethod
    async def post_gathered(channel: str, likes: int, comments: int) -> str:
        return f'Your post in the channel «{channel}» has gathered:\n ❤️ {likes} likes!\n 📝 {comments} comments!\n<a href="">Пост</a>'
    
    @staticmethod
    async def new_subscribers(channel: str, amount: int):
        return f'⬆️✅ There are {amount} new subscribers in your channel «{channel}»!\n<a href="">Кто?</a>'
    
    @staticmethod
    async def left_channel(channel: str, amount: int):
        return f'⬇️❌ От вашего канала «{channel}» отписалось {amount} человек!\n<a href="">Кто?</a>'
    

@dataclass
class Neuro:
    neuro_switch      = 'Вижу, Вы переключились на режим нейросети!\nЗадавайте любые вопросы и наш бот, в которого встроен <b>ChatGPT</b> последней версии, ответит на все из них!\nЕсли наш бот Вам не отвечает, а у Вас есть активная подписка на ChatGPT, то скорее всего, его подписка на ChatGPT истекла... такое может быть и тогда нам сразу нужно переподключить ее. Система автоматизации оплаты может не сработать! Поэтому для налаживания проблемы свяжитесь с нами, командой <b>Graball</b>: /contact'
    answer_generating = 'Ожидайте! Ответ на Ваш вопрос генерируется...'
    error             = 'Oops... something went wrong... Try again later!\nIf the problem persists, write to support: /contact'

    @staticmethod
    async def answer(answer: str) -> str:
        return f'<b>ChatGPT</b> an:\n{answer}'


@dataclass
class SubscriptionText:
    free_mode_received   = 'You received a free trial period for 5 days! 🕖'
    free_mode_expired    = 'Oops... 😬\n Free trial has expired...\nIf you liked our bot and want to continue using it, get a subscription!'
    subscription_expired = 'Oops... your paid subscription has expired...'

    @staticmethod
    async def render_subscribtion() -> str:
        pass

    @staticmethod
    async def gift_received(username: str, sub_title: str) -> str:
        return f'🥳 УРА!!!\nПользователь @{username} подарил тебе подписку на этого бота - «{sub_title}»!'

    
@dataclass
class RegisterText:
    info               = '<b>Why registration might be essential?</b>\n\nДело в том, что если ты случайно потеряешь доступ к твоему Telegram аккаунту, и тебе придется создавать новый, то автоматически бот перестанет тебе распознавать!'
    create_login       = 'Create a username. It must be <b>unique</b> and not containing kyrillic alphabet symbols!'
    invalid_login      = 'Invalid username! Try again!'
    create_password    = 'Придумайте пароль. Он должен быть хотя бы <b>пять символов</b> в длину и не содержать кириллицы!'
    invalid_password   = 'Invalid password! Try again!'
    registered_success = 'You registered successfully!'
    confirm_deleting   = 'Are you sure you want to delete your account? Это действие необратимо!\n👇 <b>IMPORTANT!</b>\nКаналы и чаты удалены не будут! Вся информация останется на месте! Вы просто перепревяжетесь на свой Telegram ID!\n\n<b>Если вы хотите удалить всю информацию аккаунта, нажми: /clear</b>'
    deleted_success    = 'Account deletes successfully!'


@dataclass
class ClearText:
    confirm_clearing = 'Вы уверены, что хотите очистить свой аккаунт? Это действие необратимо!\n<b>Удалятся все Ваши активные чаты и каналы!</b>'
    success          = 'Аккаунт успешно очищен!'
    error            = 'Oops... в процессе очистки произошла ошибка... Попробуйте еще раз!\nЕсли проблема сохраниться, напишите в поддержку: /contact'


@dataclass
class LoginText:
    input_login             = 'Input username:'
    input_password          = 'Input password:'
    wrong_login_or_password = 'Invalid login on password!'
    logged_in_success       = 'You logged in successfully!'
    logged_out_success      = 'You logged out successfully!'


@dataclass
class SessionsText:
    not_registered_error = 'У Вас нет аккаунта в нашем боте, поэтому у Вас не может быть других активных сессий, кроме этого устройства!'
    active_sessions      = 'Активные сессии на других устройствах:'
    remove_session       = 'Удалить сессию?'
    removed_success      = 'Сессия успешно удалена!'


@dataclass
class SendEmail:
    select_topic = 'Select a topic for your email:'
    input_topic = 'Input topic text:'
    input_content = 'Input email content:'
    input_your_email = 'Input your email address. A response from our team will be sent to it:'
    success = 'Email sent successfully! Ожидайте ответа на свою почту, мы постараемся разобраться как можно скорее!'
    

    @classmethod
    async def selected_topic(cls, topic: str) -> str:
        return f'Вы выбрали тему: <b>{topic}</b>'


@dataclass
class ManagingChannelText:
    empty_sequence       = 'Похоже, пока что Вы не добавили ни одного канала...'
    topics               = 'Выбери темы, на которые бот сможет делать посты в твоем канале:'
    start_new_channel    = 'Привет, вижу, ты добавил новый канал!\nИтак, чтобы бот смог им управлять, тебе нужно сделать его админом канала. Если что-то пойдет не так - не переживай, ты всегда сможешь его удалить и у бота больше не будет доступа к твоему каналу!\n\nПредлагаю выбрать те функции, которые сможет выполнять бот в твоем канале:'
    switch_off_stat      = '<b>Выключить уведомления о статистике?</b>\nВам перестанут приходить уведомления о статистике активности канала, новых пользователях, лайках и комментариях!'
    automanaging         = ''
    selfmanaging         = ''
    confirm_deleting     = 'Ты уверен, что хочешь удалить канал? Это действие необратимо!'
    deleted_successfully = 'Channel deleted successfully!'
    updated_successfully = 'Channel settings updated successfully!'
    what_are_donors      = '❓<b>What are donors?</b>\n\Channel-donors - это такие каналы, с которых бот будет граббить информацию. Вы можете выбрать конкретные каналы, с которых бот будет граббить посты.'
    send_channels_donors = 'Хорошо, теперь отправь мне те каналы, с которых хочешь граббить посты! Нажми на кнопку '

    @staticmethod
    async def render_settings(settings: dict[str]) -> str:
        result = 'Channel settings:\n'
        for key, value in settings.items():
            result += f''
        return result

    @staticmethod
    async def posts_created(channel: str, amount: int) -> str:
        return f'Hey!\Generated <b>{amount}</b> ideas for your channel «{channel}»! Here you go!'
    
    @staticmethod
    async def added_donors(channels: dict[str, list[ChatShared]]) -> str:
        result = f'Great! Here are the donors you added:\n'
        for channel in channels['channels']:
            result += f'<b><a href="t.me/{channel.username}">{channel.title}</a></b>\n'
        return result

@dataclass
class ManagingChatText:
    empty_sequence   = 'Похоже, пока что Вы не добавили ни одного чата...'
    start_new_chat   = ''
    delete_intruders = 'Удалять пользователей, нарушающих правила чата?'
    user_not_found   = '😐 <b>User not found!</b>'

    @staticmethod
    async def on_new_user(cls, username: str, chat_title: str) -> str:
        return f'Привет, @{username}! Добро пожаловать в {chat_title}!\nЧтобы подтвердить, что вы не бот, нажми на кнопку ниже! 👇'

    @staticmethod
    async def users_deleted(cls, users: int, chat: str) -> str:
        return f'🚨 {users} пользователей были удалены из чата «{chat}» за нарушение правил в течение этого дня!'

    @staticmethod
    async def user_banned(cls, user_username: str, user_banned_by: str, reason: str, until: str) -> str:
        return f'🚨 <b>Пользователь @{user_username} был заблокирован</b> пользователем @{user_banned_by} по причине: {reason}\nПериод: {until}'
    
    @staticmethod
    async def user_muted(cls, user_username: str, user_muted_by: str, reason: str, until: str) -> str:
        return f'⚠️ <b>Пользователь @{user_username} был заглушен</b> пользователем @{user_muted_by} по причине: {reason}\nПериод: {until}'
    
    @staticmethod
    async def user_unbanned(cls, user_username: str, user_unbanned_by: str) -> str:
        return f'✅ <b>Пользователь @{user_username} был разблокирован</b> пользователем @{user_unbanned_by}!'
    
    @staticmethod
    async def user_unmuted(cls, user_username: str, user_unmuted_by: str) -> str:
        return f'✅ <b>Пользователю @{user_username} снова разрешено</b> писать сообщения пользователем @{user_unmuted_by}!'
    
    @staticmethod
    async def not_admin_to_commit(cls, user_username: str) -> str:
        return f'❗️ @{user_username}, чтобы блокировать / разблокировать пользователя, <b>надо быть администратором чата</b> ❗️'

@dataclass
class FunctionsText:
    manage_channel = '<b>Managing a channel</b>\Add this feature, and <b>the bot will be able to:</b>\n- 📆 По расписанию создавать посты в канале (он может делать это полностью автоматически или уточняя у админа канала);\n- 💡 Предлагать вам идеи для дальнейших постов;'
    manage_chat    = 'Add the bot in you chat, and <b>it will be able to:</b>\n- Filter 🤬 obscenities & insults in a chat;\n- <-> 🤫 political discussions / призывы различного рода в чате;\n- <-> 🔞 content;\n- <-> 💸 различные виды мошенничества;\nПользователи, регулярно нарушающие вышеупомянутые правила, могут быть заблокированы и удалены из чата!'
    stat           = '<b>Ведение канала</b>\n📊 Включи эту функцию для своего канала и бот будет периодически уведомлять тебя о новых лайках и комментариях под твоими постами, о новых и об ушедших подписчиках, а также сможет строить статистику о работе канала за неделю / месяц / полгода!'

