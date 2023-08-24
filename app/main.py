from fastapi import FastAPI

app = FastAPI(
    title='First our app',
    description='we are champions',
    version='0.0.1',
)


@app.get('/')
async def main_page():
    return {'data': 'something'}
