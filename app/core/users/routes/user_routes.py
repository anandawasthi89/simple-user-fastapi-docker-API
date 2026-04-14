from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db.DBConnection import get_db
from app.core.users.schemas.user_request import UserRequest
from app.core.users.services.user_dao import UserDao

router = APIRouter()

@router.get("/")
def is_alive():
    return {"message": "User service is alive!"}

@router.get("/getUser")
def get_user(user_id: int, db: Session =Depends(get_db)):
    user = UserDao().getUserById(user_id, db)
    return {"user": user}

@router.post("/createUser")
def create_user(userRequest: UserRequest, db: Session =Depends(get_db)):
    user = UserDao().createUser(userRequest, db)
    return {"message": "User created successfully!", "user": user}

@router.put("/updateUser")
def update_user(user_id: int, userRequest: UserRequest, db: Session =Depends(get_db)):
    UserDao().updateUser(user_id, userRequest, db)
    return {"message": "User updated successfully!"}

@router.delete("/deleteUser")
def delete_user(user_id: int, db: Session =Depends(get_db)):
    UserDao().deleteUser(user_id, db)
    return {"message": "User deleted successfully!"}