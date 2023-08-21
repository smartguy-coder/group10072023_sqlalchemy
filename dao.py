import asyncio

from sqlalchemy import insert, select, update, delete

from database import async_session_maker
from models import User, Order


async def create_user(
        name: str,
        login: str,
        password: str,
        notes: str = None,
        is_conflict: bool = False,
):
    async with async_session_maker() as session:
        query = insert(User).values(
            name=name,
            login=login,
            password=password,
            notes=notes,
            is_conflict=is_conflict,
        )
        print(query)
        await session.execute(query)
        await session.commit()


async def main():
    await asyncio.gather(
        create_user(
            name='name1',
            login='login1',
            password='password1',
        )
    )

asyncio.run(main())
