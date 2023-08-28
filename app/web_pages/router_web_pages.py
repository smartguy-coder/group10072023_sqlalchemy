from fastapi import APIRouter
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix='/web',
    tags=['menu', 'landing'],
)

templates = Jinja2Templates(directory='app\\templates')
