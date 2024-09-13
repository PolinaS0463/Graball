from dataclasses import dataclass

@dataclass
class BaseInfo:
    pass

langs = '''На данный момент в нашем боте достпуно всего <b>два языка</b>: английский и русский!'''

languages = '''На данный момент в нашем боте достпуно всего <b>два языка</b>: английский и русский!\n
               Чтобы перевести интерфейс на другие языки, нам нужно больше времени и рабочих сил!
               <b>Если вы чувствуете, что можете помочь нам в этом, пишите на почту: @email</b>!
               Приветствуются люди, говорящие на:\n
               - 🥇 - немецком 🇩🇪\n
               - 🥈 - французском 🇫🇷\n
               - 🥉 - итальянском 🇮🇹\n
               Также мы будем заинтересованы, если вы говорите на испанском 🇪🇸 и на португальском 🇵🇹 :)'''

start_new_channel = '''Hey, so I see you added a new channel!
                       Firstly, to make bot able to manage it, you need
                       сделать его админом канала. In case something goes wrong -
                       don't worry, ты всегда сможешь его удалить и у бота больше
                       не будет доступа к твоему каналу!
                       
                       Now I suggest you to select functions our bot will be
                       able to :'''

manage_chat = '''Добавляй бота в чат твоего канала, и <b>он сможет:</b>\n
                   - Фильтровать 🤬 мат & оскорбления в чате;\n
                   - <-> 🤫 политические дискуссии / призывы различного рода в чате;\n
                   - <-> 🔞 контент;\n
                   - <-> 💸 различные виды мошенничества;\n
                   Пользователи, регулярно нарушающие вышеупомянутые правила, могут быть заблокированы и удалены из чата!'''

manage_channel = '''Добавляй бота в чат твоего канала, и <b>он сможет:</b>\n
                      - По расписанию создавать посты в канале (он может делать это полностью автоматически или уточняя у админа канала);\n
                      - Предлагать вам идеи для дальнейших постов;'''

stat = '''📊 Switch in this feature for your channel and bot will 
          periodically notify you about new likes and comments
          под твоими постами, about new and left subscribers, and
          also will be able to create a statistics dashboard about channel's
          activity during one week / month / half-year!'''


newsletter = ''''''

class Notifications:
    @classmethod
    async def post_gathered(channel: str, likes: int, comments: int) -> str:
        return f'Ваш пост в канале {channel} собрал:\n ❤️ {likes} лайков!\n 📝 {comments} комментариев!\n<a href="">Пост</a>'
    
    @classmethod
    async def new_subscribers(channel: str, amount: int):
        return f' В вашем канале {channel} {amount} новых подписчиков!\n<a href="">Кто?</a>'
    
    @classmethod
    async def left_channel(channel: str, amount: int):
        return f'⬇️ От вашего канала {channel} отписалось {amount} человек!\n<a href="">Кто?</a>'
    
neuro_switch = '''Вижу, Вы переключились на режим нейросети!\n
                  Задавайте любые вопросы и наш бот, в которого встроен <b>ChatGPT</b> последней
                  версии, ответит на все из них!\n
                  Если наш бот Вам не отвечает, то скорее всего, его подписка на ChatGPT истекла...
                  такое может быть и тогда нам сразу нужно переподключить ее. Система автоматизации
                  оплаты может не сработать! Поэтому для налаживания проблемы свяжитесь с нами, командой
                  <b>Graball</b>: /contact'''

contact_us = '✅ Наш инновационный бот всегда в процессе разработки, чтобы работать все более и более качественно для вас! Непростой в реализации функционал требует большого количества сосредоточенности, внимания и профессионализма от наших программистов!\n\nТем не менее, все мы не роботы, и время от времени могут происходить различного вида сбои, особенно при такой нагруженности бота и сложности реализуемого функционала!\n‼️ Чтобы мы сразу смогли отреагировать на изменения в работе бота, просим Вас оставлять нам обратную связь! Нам очень важно создать уникальный продукт, который будет упрощать жизнь и работать максимально качественно! Тем более что выявить некоторые уязвимости и недоработки можно только во время прода (реальной работы с пользователями 24/7)!\nЕсли Вы хотите написать нам, нажмите на кнопку <b>«Отправить</b> внизу. Мы постараемся как можно скорее ответить на Ваше обращение!'''

contact_us_notes = '''
                    '''


@dataclass
class Subscriptions:
    pass


@dataclass
class SendEmail:
    select_topic = 'Select a topic for your email:'
    input_topic = 'Input topic text:'
    input_content = 'Input email content:'
    input_your_email = 'Input your email address. A response from our team will be sent to it:'
    success = 'Email sent successfully! Ожидайте ответа на свою почту, мы постараемся разобраться как можно скорее!'
    