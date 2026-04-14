from sqlalchemy.orm import Session
from app.core.users.schemas.user import User
from datetime import datetime
from app.core.users.exceptions import user_not_found_exception, user_creation_exception, user_update_exception, user_deletion_exception

class UserDao:

    def getUserById(self, user_id, db: Session):
        # Logic to retrieve a user by ID from the database
        try:
            user = db.query(User).filter(User.user_id == user_id).first()
            return user
        except Exception as e:
            raise user_not_found_exception(user_id)

    def createUser(self, userRequest, db: Session):
        # Logic to create a new user in the database
        try:
            user = User(
                first_name=userRequest.first_name,
                last_name=userRequest.last_name,
                full_name=userRequest.full_name,
                email=userRequest.email,
                bank_id=userRequest.bank_id,
                bank_account=userRequest.bank_account,
                status="active",
                created_at=str(datetime.now()),
                updated_at=str(datetime.now())
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            raise user_creation_exception(userRequest.full_name, userRequest.email)

    def updateUser(self, user_id, userRequest, db: Session):
        # Logic to update an existing user in the database
        try:
            user = db.query(User).filter(User.user_id == user_id).first()
            for key, value in userRequest.dict().items():
                setattr(user, key, value)
            user.updated_at = str(datetime.now())
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            raise user_update_exception(userRequest.full_name, userRequest.email)

    def deleteUser(self, user_id, db: Session):
        # Logic to delete a user from the database
        try:
            user = db.query(User).filter(User.user_id == user_id).first()
            db.delete(user)
            db.commit()
            return user
        except Exception as e:
            raise  user_deletion_exception(user.full_name, user.email)


    def getAllUsers(self, page: int, size: int):
        # Logic to retrieve all users with pagination
        pass

    def findUsersByName(self, firstname: str, lastname: str, page: int, size: int):
        # Logic to find users by name with pagination
        pass