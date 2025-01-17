from typing import List
import logging
from pathlib import Path
import aiofiles

from bson.objectid import ObjectId
from fastapi import APIRouter, HTTPException, Depends, File, UploadFile
from marshmallow.exceptions import ValidationError
from starlette import status
from starlette.responses import JSONResponse

from src.models.user import User
from src.serializers.user import UserInSerializer, UserSerializer
from .auth_api import get_current_user

router = APIRouter()


@router.get("/test")
async def test():
    return {"message": "Hello World"}

@router.post("/single-file")
async def test(file: UploadFile = File(...)):
    logging.info(file.filename)
    logging.info(Path.cwd())
    # f = open('files/test.txt', 'w')
    # f.write(file.filename)
    # f.close()
    async with aiofiles.open(Path.cwd() / 'files' / file.filename, 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write
    return {"filename": file.filename}


@router.get("", response_model=List[UserSerializer],
            status_code=status.HTTP_200_OK)
async def get_users_api(_: User = Depends(get_current_user)):
    cursor = User.find()
    return [user.dump() for user in await cursor.to_list(length=10)]


@router.post("", response_model=UserSerializer,
             status_code=status.HTTP_201_CREATED)
async def create_user_api(user_in: UserInSerializer):
    user_exists = await User.get_by_email(user_in.email)
    if user_exists:
        raise HTTPException(
            422,
            [{
                'loc': ["body", 'email'],
                'msg': f"Email '{user_in.email}' is already registered",
                'type': 'value_error',
            }]
        )
    try:
        user = await User.register_new_user(email=user_in.email,
                                            full_name=user_in.full_name,
                                            password=user_in.password)
        return user.dump()
    except ValidationError as e:
        return JSONResponse({'field_errors': [e.messages]}, status.HTTP_400_BAD_REQUEST)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_api(user_id: str, current_user: User = Depends(get_current_user)):
    user = await User.find_one({'_id': ObjectId(user_id)}, {'_id': 1})
    if not user:
        raise HTTPException(detail="User Not Found", status_code=status.HTTP_404_NOT_FOUND)
    await user.remove()


@router.get('/me', response_model=UserSerializer, status_code=status.HTTP_200_OK)
async def get_user_me_api(current_user: User = Depends(get_current_user)):
    return current_user.dump()
