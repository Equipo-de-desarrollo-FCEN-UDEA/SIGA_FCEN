from typing import List
from app.schemas.users import user
from app.core.config import get_settings

settings = get_settings()

init_users: List[user.UserCreate] = [
    user.UserCreate(
    name = "pedro",
    last_name = "perez",
    email = "pedro@local.com",
    identification_type = "cedula_ciudadania",
    identification_number="123456789",
    phone="123456789",
    hashed_password= "123456789",    
    is_active = True
       
    )
]

