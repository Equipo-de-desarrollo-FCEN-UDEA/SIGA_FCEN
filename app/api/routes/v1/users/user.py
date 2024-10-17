from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, HTTPException, Depends, Security

from app.api.middleware.bearer import get_current_active_user
from app.schemas.users.user import UserCreate, UserUpdate, UserInDB, User
from app.schemas.users.user_rol_academic_unit import UserRolAcademicUnitCreate, UserRolAcademicUnit, UserRolAcademicUnitInDB
from app.services.users.user import user_svc
from app.services.users.user_rol_academic_unit import user_rol_academic_unit_svc

from app.api.middleware.postgres_db import get_db


router = APIRouter()


@router.post("", response_model=UserInDB, status_code=201)
def create_user(*, new_user: UserCreate, rol_id:UUID,
                acadeic_unit_id:UUID, db_postgres = Depends(get_db) ) -> UserInDB:
    """Endpoint to create a new user in db

    Args:
        new_user (UserCreate): Schema

    Returns:
        UserInDB: User in DB schema
    """

    user = user_svc.create(obj_in=new_user, db=db_postgres)
    user_rol_academic_unit_svc.create(
        obj_in=UserRolAcademicUnitCreate(
            rol_id=rol_id, user_id=user.id,
            academic_unit_id=acadeic_unit_id
        )
        , db=db_postgres
    )
    return user


@router.get("", response_model=list[UserInDB], status_code=200)
def get_all_user(
    *, skip: int = 0, 
    limit: int = 10, 
    db_postgres = Depends(get_db),
    current_user: Annotated[User, Security(get_current_active_user, scopes=[ "admin"])] = None
) -> list[UserInDB]:
    return user_svc.get_multi(skip=skip, limit=limit, db=db_postgres)


@router.get("/{id}", response_model=User, status_code=200)
def get_user(*, id: UUID, db_postgres = Depends(get_db)) -> User:
    user = user_svc.get(id=id, db=db_postgres)
    if not user:
        raise HTTPException(404, "User not found")
    user = UserInDB.model_validate(user)
    roles = user_rol_academic_unit_svc.get_by_user_id(user_id=id, db=db_postgres)

    user_roles_academic_units = [UserRolAcademicUnit.model_validate(role) for role in roles]

    response = User(
        **user.model_dump(),
        user_roles_academic_units=user_roles_academic_units
    )

    return response
    


@router.patch("/{id}", response_model=None)
def update_user(*, obj_in: UserUpdate, id: int) -> None:
    user = user_svc.get(id=id)
    if not user:
        raise HTTPException(404, "User not found")
    user_svc.update(id=id, obj_in=obj_in)
    return None


@router.delete("/{id}", response_model=None, status_code=204)
def delete_user(*, id: int) -> None:
    user = user_svc.delete(id=id)
    if user == 0:
        raise HTTPException(404, "User not found")
    return None


@router.get("/view/me", response_model=UserInDB, status_code=200)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]) -> UserInDB:
    return current_user