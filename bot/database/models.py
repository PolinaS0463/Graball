from sqlalchemy import String, Text, Float, Integer, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Subscription(Base):
    __tablename__ = 'subscription'

    pk: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    subscription_chart: Mapped[int] = mapped_column(nullable=False)
    is_active: Mapped[Boolean] = mapped_column(Boolean, nullable=False)


class SubscriptionChart(Base):
    __tablename__ = 'subscription_chart'

    pk: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text(300), nullable=False)
    price: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    duration: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)



class Channel(Base):
    __tablename__ = 'channel'

    pk: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(String(500), unique=True, nullable=True)
    reading_stat: Mapped[bool] = mapped_column(Boolean, default=False)
    automanaging: Mapped[bool] = mapped_column(Boolean, default=False)
    selfmanaging: Mapped[bool] = mapped_column(Boolean, default=False)

    # owner: Mapped[int] = 

class Chat(Base):
    __tablename__ = 'chat'

    pk: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(String(500), unique=True, nullable=True)
    reading_stat: Mapped[bool] = mapped_column(Boolean, default=False)
    automanaging: Mapped[bool] = mapped_column(Boolean, default=False)
    selfmanaging: Mapped[bool] = mapped_column(Boolean, default=False)


class User(Base):
    __tablename__ = 'user'

    pk: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
    password: Mapped[str] = mapped_column(String(100), nullable=True)
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    # subscription: Mapped[int] = 
    # user_telegram_id: Mapped[int] =  mapped_column(Inte)


class Task(Base):
    __tablename__ = 'task'

    pk: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    timestamp: Mapped[int] = mapped_column(Integer, nullable=False)




class ReadStat(Base):
    pass
    
