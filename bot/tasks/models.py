from sqlalchemy import String, Text, Float, Integer, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Task(Base):
    __tablename__ = 'task'

    task_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    time_to_complete: Mapped[int]

