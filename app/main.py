from fastapi import FastAPI

app = FastAPI(
    title='First our app',
    description='we are champions',
    version='0.0.1',
)


@app.get('/')
@app.post('/')
async def main_page() -> dict:
    return {'data': 'something'}


@app.get('/{user_name}')
@app.get('/{user_name}/{user_nik}')
async def user_page(user_name: str, user_nik: str = '', limit: int = 10, skip: int = 0) -> dict:
    data = [i for i in range(1000)]

    return {'user_name': user_name, 'user_nik': user_nik, 'data': data}
