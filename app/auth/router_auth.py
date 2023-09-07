from fastapi import APIRouter, status

from .schemas import AuthDetails, AuthRegistered
import dao


router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post('/register', response_model=AuthRegistered, status_code=status.HTTP_201_CREATED)
async def register(auth_details: AuthDetails):

    user_data = await dao.create_user(
        name=auth_details.name,
        login=auth_details.login,
        password=auth_details.password,
        notes=auth_details.notes,
    )

    return AuthRegistered(success=True, id=user_data[0], login=user_data[1])
