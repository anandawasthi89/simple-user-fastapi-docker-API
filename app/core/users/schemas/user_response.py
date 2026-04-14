from app.core.users.schemas.base_user import base_user

class UserResponse(base_user):
    user_id: int
    status: str
    created_at: str
    updated_at: str