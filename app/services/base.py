from datetime import date
from typing import Generic, TypeVar, Any
from uuid import UUID
from app.errors.base import BaseErrors

from app.protocols.db.crud.base import CRUDProtocol

from app.schemas.utils.base_model import CreateSchemaType, UpdateSchemaType


ModelType = TypeVar("ModelType")

CrudType = TypeVar("CrudType", bound=CRUDProtocol)


class ServiceBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType, CrudType]):
    def __init__(self):
        self.observer: CrudType | None = None

    def register_observer(self, observer: CrudType) -> None:
        self.observer = observer
        return None

    def unregister_observer(self) -> None:
        self.observer = None
        return None

    def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        if self.observer is None:
            raise BaseErrors(code=503, detail="Service not available")
        return self.observer.create(obj_in=obj_in)

    def get(self, *, id: UUID) -> ModelType:
        if self.observer is None:
            raise BaseErrors(code=503, detail="Service not available")
        return self.observer.get(id=id)

    def get_multi(
        self,
        *,
        payload: dict[str, Any] | None = None,
        skip: int = 0,
        limit: int = 10,
        order_by: str | None = None,
        date_range: dict[str, date] | None = None,
        values: tuple[str] | None = None
    ) -> list[ModelType | dict[str, Any]]:
        if self.observer is None:
            raise BaseErrors(code=503, detail="Service not available")
        return self.observer.get_multi(
            payload=payload,
            skip=skip,
            limit=limit,
            order_by=order_by,
            date_range=date_range,
            values=values,
        )

    def update(self, *, id: UUID, obj_in: UpdateSchemaType) -> ModelType:
        if self.observer is None:
            raise BaseErrors(code=503, detail="Service not available")
        return self.observer.update(id=id, obj_in=obj_in)

    def delete(self, *, id: int) -> int:
        if self.observer is None:
            raise BaseErrors(code=503, detail="Service not available")
        return self.observer.delete(id=id)