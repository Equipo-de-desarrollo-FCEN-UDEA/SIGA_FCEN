from typing import List
from app.schemas.users import user
from app.core.config import get_settings

settings = get_settings()

init_users: List[user.UserCreate] =[
    user.UserCreate(
       
    )
]

