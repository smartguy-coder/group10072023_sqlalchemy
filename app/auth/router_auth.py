from fastapi import APIRouter, status
from .schemas import AuthDetails, AuthRegistered


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post('/register', response_model=AuthRegistered, status_code=status.HTTP_201_CREATED)
async def register(auth_details: AuthDetails):


    return AuthRegistered(success=True, id=5656, login='kgdfhkj@ukr.net')
