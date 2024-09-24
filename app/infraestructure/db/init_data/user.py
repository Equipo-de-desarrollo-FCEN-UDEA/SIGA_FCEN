from typing import List
from app.schemas.users import user

init_user: List[user.UserCreate] = [
    user.UserCreate(
    name = "pedro",
    last_name = "perez",
    email = "pedro@local.com",
    identification_type = "cedula_ciudadania",
    identification_number="123456789",
    phone="123456789",
    password = "123456",   
    is_active = True
       
    )
]

