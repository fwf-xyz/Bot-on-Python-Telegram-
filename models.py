from datetime import datetime, timezone
from sqlalchemy import BigInteger, String, ForeignKey, DateTime, Enum, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine 

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )


class Workouts(Base):
    __tablename__ = 'workouts'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    workout_type: Mapped[str] = mapped_column(Enum('Силовая', 'Кардио', 'Гибкость', name='workout_type_enum'))
    duration: Mapped[int] = mapped_column()
    intensity: Mapped[int] = mapped_column()
    notes: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )
    
    __table_args__ = (
        CheckConstraint('duration >= 1 AND duration <= 240', name='duration_range_check'),
        CheckConstraint('intensity >= 1 AND intensity <= 5', name='intensity_range_check')
    )


#    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) 
    print('Бот запущен!')