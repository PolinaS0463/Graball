from aiogram.types import ChatShared

from dataclasses import dataclass


@dataclass
class UtilsText:
    CHANNEL = 'канал'

    @staticmethod
    async def process_period_text(period: str) -> str:
        if period:
            period_text = period[1]
            match period_text:
                case 'm':
                    return f'{period[0]} минут'
                case 'h':
                    return f'{period[0]} часов'
                case 'd':
                    return f'{period[0]} дней'
                case 'w': 
                    return f'{period[0]} недель'
        return 'навсегда'

@dataclass
class BaseInfoText:
    contact_us                = '✅ Наш инновационный бот всегда в процессе разработки, чтобы работать все более и более качественно для вас! Непростой в реализации функционал требует большого количества сосредоточенности, внимания и профессионализма от наших программистов!\n\nТем не менее, все мы не роботы, и время от времени могут происходить различного вида сбои, особенно при такой нагруженности бота и сложности реализуемого функционала!\n\n‼️ Чтобы мы сразу смогли отреагировать на изменения в работе бота, просим Вас оставлять нам обратную связь! Нам очень важно создать уникальный продукт, который будет упрощать жизнь и работать максимально качественно! Тем более что выявить некоторые уязвимости и недоработки можно только во время прода (реальной работы с пользователями 24/7)!\n\nЕсли Вы хотите написать нам, нажмите на кнопку <b>«Отправить</b> внизу. Мы постараемся как можно скорее ответить на Ваше обращение!'
    contact_us_notes          = '‼️ Пожалуйста, не стоит задавать вопросы по поводу интерфейса бота ‼️\nОб этом подробно разъяснено в самом боте! Также можно почитать документацию на странице проекта!'
    langs                     = 'На данный момент достпуно всего <b>два языка</b>: английский и русский!'
    lang_changed_successfully = '✅ Язык успешно изменен на <b>русский!</b>'
    advertisement             = '💡 Чтобы «заказать» рекламу вашего ресурса, пишите <b>@flamme_ss</b> в Telegram или на почту: graball_bot_team@gmail.com'
    subscribe_first           = 'Перед использованием бота подпишитесь, пожалуйста, на наш канал!'

    @staticmethod
    async def hello(name: str, users: int = 0, channels: int = 0, chats: int = 0) -> str:
        return f'Привет, <b>{name}!</b>\nЭто <b>«Graball»</b> - инновационный бот-граббер и бот-модератор! <b>Через него вы сможете:</b>\n- Мониторить чаты;\n- Вести каналы;\n- Автоматизировать процессы;\n- Использовать нейросеть <b>ChatGPT</b>;\n\nНам доверяют ❤️‍🩹\nСейчас у нас:\n<b>{users}</b> пользователей 👥\n<b>{channels}</b> каналов 🎙️\n<b>{chats}</b> чатов 📱'

    @staticmethod
    async def render_settings(settings: dict[str]) -> str:
        result = 'Настройки аккаунта:\n'
        for key, value in settings.items():
            result += f''
        return result
    
    @staticmethod
    async def send_chat_or_channel(text: str) -> str:
        return f'Отлично!\n\nА теперь нажми на кнопку «Отправить» ниже и выбери нужный канал!'


class NotificationsText:

    @staticmethod
    async def statistics(channel: str, period: str):
        return f'Хэй! Отчет по твоему каналу «{channel}» готов!\nПериод: <b>{period}</b>'

    @staticmethod
    async def post_gathered(channel: str, likes: int, comments: int) -> str:
        return f'Ваш пост в канале «{channel}» собрал:\n ❤️ {likes} лайков!\n 📝 {comments} комментариев!\n<a href="">Пост</a>'
    
    @staticmethod
    async def new_subscribers(channel: str, amount: int):
        return f'⬆️✅ В вашем канале «{channel}» {amount} новых подписчиков!\n<a href="">Кто?</a>'
    
    @staticmethod
    async def left_channel(channel: str, amount: int):
        return f'⬇️❌ От вашего канала «{channel}» отписалось {amount} человек!\n<a href="">Кто?</a>'


@dataclass
class SubscriptionText:
    free_mode_received   = 'Вы получили пробный период на 5 дней! 🕖'
    free_mode_expired    = 'Упс... 😬 Пробный период истек...\n Если Вам понравился наш бот, и Вы хотите продолжить использование, купите подписку!'
    subscription_expired = 'Упс... твоя платная подписка истекла...'

    @staticmethod
    async def render_subscribtion() -> str:
        pass

    @staticmethod
    async def gift_received(username: str, sub_title: str) -> str:
        return f'🥳 УРА!!!\nПользователь @{username} подарил тебе подписку на этого бота - «{sub_title}»!'

    
@dataclass
class RegisterText:
    info               = '<b>Почему регистрация - это важно?</b>\n\nДело в том, что если ты случайно потеряешь доступ к твоему Telegram аккаунту, и тебе придется создавать новый, то автоматически бот перестанет тебе распознавать!'
    create_login       = 'Придумайте логин. Он должен быть <b>уникальным</b> и не содержать кириллицы!'
    invalid_login      = 'Невалидный логин! Попробуйте еще раз!'
    create_password    = 'Придумайте пароль. Он должен быть хотя бы <b>пять символов</b> в длину и не содержать кириллицы!'
    invalid_password   = 'Невалидный пароль! Попробуйте еще раз!'
    registered_success = 'Вы успешно зарегестрированы!'
    confirm_deleting   = 'Вы уверены, что хотите удалить свой аккаунт? Это действие необратимо!\n👇 <b>ВАЖНО!</b>\nКаналы и чаты удалены не будут! Вся информация останется на месте! Вы просто перепревяжетесь на свой Telegram ID!\n\n<b>Если вы хотите удалить всю информацию аккаунта, нажми: /clear</b>'
    deleted_success    = 'Аккаунт успешно удален!'


@dataclass
class ClearText:
    confirm_clearing = 'Вы уверены, что хотите очистить свой аккаунт? Это действие необратимо!\n<b>Удалятся все Ваши активные каналы!</b>'
    success          = 'Аккаунт успешно очищен!'
    error            = 'Упс... в процессе очистки произошла ошибка... Попробуйте еще раз!\nЕсли проблема сохраниться, напишите в поддержку: /contact'


@dataclass
class LoginText:
    input_login             = 'Введите логин:'
    input_password          = 'Введите пароль:'
    wrong_login_or_password = 'Неверный логин или пароль!'
    logged_in_success       = 'Вы успешно авторизованы!'
    logged_out_success      = 'Вы успешно вышли из аккаунта!'


@dataclass
class SessionsText:
    not_registered_error = 'У Вас нет аккаунта в нашем боте, поэтому у Вас не может быть других активных сессий, кроме этого устройства!'
    active_sessions      = 'Активные сессии на других устройствах:'
    remove_session       = 'Удалить сессию?'
    removed_success      = 'Сессия успешно удалена!'


@dataclass
class SendEmailText:
    select_topic     = 'Выберите тему для обращения:'
    input_topic      = 'Введите тему:'
    input_content    = 'Введите текст сообщения:'
    input_your_email = 'Введите свою почту. На нее придет ответ от нашей команды:'
    success          = 'Обращение успешно создано! Ожидайте ответа на свою почту, мы постараемся разобраться как можно скорее!'

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
    deleted_successfully = 'Канал успешно удален!'
    updated_successfully = 'Настройки канала успешно обновлены!'
    what_are_donors      = '❓<b>Что такое доноры?</b>\n\nКаналы-доноры - это такие каналы, с которых бот будет граббить информацию. Вы можете выбрать конкретные каналы, с которых бот будет граббить посты.'
    send_channels_donors = 'Хорошо, теперь отправь мне те каналы, с которых хочешь граббить посты! Нажми на кнопку '

    @staticmethod
    async def render_settings(settings: dict[str]) -> str:
        result = 'Настройки канала:\n'
        for key, value in settings.items():
            result += f''
        return result

    @staticmethod
    async def posts_created(channel: str, amount: int) -> str:
        return f'Привет!\nСгенерировал <b>{amount}</b> идей для твоего канала «{channel}»! Лови!'
    
    @staticmethod
    async def added_donors(channels: dict[str, list[ChatShared]]) -> str:
        result = f'Отлично! Вот выбранные каналы доноры:\n'
        for channel in channels['channels']:
            result += f'<b><a href="t.me/{channel.username}">{channel.title}</a></b>\n'
        return result
    
    @staticmethod
    async def new_topic_added(topic: str) -> str:
        return f'Добавлена новая тема: {topic}'
     

@dataclass
class FunctionsText:
    manage_channel       = '<b>Ведение канала</b>\nДобавляй эту функцию, и <b>бот сможет:</b>\n- 📆 По расписанию создавать посты в канале (он может делать это полностью автоматически или уточняя у админа канала);\n- 💡 Предлагать вам идеи для дальнейших постов;'
    stat                 = '<b>Ведение канала</b>\n📊 Включи эту функцию для своего канала и бот будет периодически уведомлять тебя о новых лайках и комментариях под твоими постами, о новых и об ушедших подписчиках, а также сможет строить статистику о работе канала за неделю / месяц / полгода!'
