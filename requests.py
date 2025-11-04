from app.database.models import async_session
from app.database.models import User, Category, Item
from sqlalchemy import select


async def set_user(user_id: int, username: str ) -> None:
    async with async_session() as session: 
        user = await session.scalar(select(User).where(User.user_id == user_id) )

        if not user:
            session.add(User(user_id=user_id, username=username))
        else:
            user.username = username

        await session.commit()



