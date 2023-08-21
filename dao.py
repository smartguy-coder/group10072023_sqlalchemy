import asyncio

from sqlalchemy import insert, select, update, delete

from database import async_session_maker
from models import User, Order


async def create_user(
        name: str,
        login: str,
        password: str,
        notes: str = '',
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


async def fetch_users(skip: int = 0, limit: int = 10):
    async with async_session_maker() as session:
        query = select(User).offset(skip).limit(limit)
        result = await session.execute(query)
        print(result.scalars().all()[0].id)
        # print(result.scalars().all()[0].__dict__)
        return result.all()


async def main():
    # await asyncio.gather(
    #     create_user(
    #         name='name1',
    #         login='login2',
    #         password='password1',
    #         notes='*'*200
    #     )
    # )
    await asyncio.gather(fetch_users())

asyncio.run(main())
