from fastapi import FastAPI

import sentry_sdk


sentry_sdk.init(
    dsn="https://1a6b12e7dbf7418233793cb807de9e53@o4505229726318592.ingest.sentry.io/4505761003864065",
    traces_sample_rate=1.0,
)

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
