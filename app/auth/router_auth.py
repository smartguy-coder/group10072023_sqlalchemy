from fastapi import APIRouter, status, HTTPException, Request, Response

from .auth_lib import AuthHandler
from .schemas import AuthDetails, AuthRegistered, AuthLogin
import dao


router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post('/register', response_model=AuthRegistered, status_code=status.HTTP_201_CREATED)
async def register_api(request: Request, response: Response, auth_details: AuthDetails):
    # print(request.cookies,          88888888888888888)
    # print(request.__dict__,          88888888888888888)

    is_login_already_used = await dao.get_user_by_login(auth_details.login)
    if is_login_already_used:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'User with email {auth_details.login} already exists'
        )

    hashed_password = await AuthHandler.get_password_hash(auth_details.password)

    user_data = await dao.create_user(
        name=auth_details.name,
        login=auth_details.login,
        password=hashed_password,
        notes=auth_details.notes,
    )

    token = await AuthHandler.encode_token(user_data[0])
    response.set_cookie(key='my_name', value='Vasyl', max_age=10, httponly=True)
    response.set_cookie(key='token', value=token, httponly=True)

    return AuthRegistered(success=True, id=user_data[0], login=user_data[1])

@router.post('/login')
async def login_api(response: Response, user_data: AuthLogin):
    pass