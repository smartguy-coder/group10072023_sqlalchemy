from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix='/web',
    tags=['menu', 'landing'],
)

templates = Jinja2Templates(directory='app\\templates')


@router.get('/')
async def get_main_page(request: Request):
    context = {
        'request': request,
    }

    return templates.TemplateResponse(
        'base.html',
        context=context,
    )



