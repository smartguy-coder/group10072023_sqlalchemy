from fastapi import Request, HTTPException, status, Depends

async def get_token(request: Request):
    token = request.cookies.get('token')
    if not token:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail='Token not presented'
        )
    return token



async def get_current_user_required(token=Depends(get_token)):
    return 5555555