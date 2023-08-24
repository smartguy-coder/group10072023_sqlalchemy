from fastapi import FastAPI

app = FastAPI(
    title='First our app',
    description='we are champions',
    version='0.0.1',
    debug=True
)


@app.get('/')
@app.post('/')
async def main_page() -> dict:

    return {'greeting': 'HELLO'}


@app.get('/{user_name}')
@app.get('/{user_name}/{user_nick}')
async def user_page(user_name: str, user_nick: str = '', limit: int = 10, skip: int = 0) -> dict:
    data = [i for i in range(1000)][skip:][:limit]

    return {'user_name': user_name, 'user_nick': user_nick, 'data': data}
