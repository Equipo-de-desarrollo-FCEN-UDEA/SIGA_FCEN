from fastapi import APIRouter
from typing import Type
from pydantic import BaseModel


class BaseRouter:
    def __init__(self, schem_in_db: Type[BaseModel], schem_create: Type[BaseModel], schem_update: Type[BaseModel], service, router: APIRouter, tags: list[str], methods: list[str] = None):
        self.schem_in_db = schem_in_db
        self.schem_create = schem_create
        self.schem_update = schem_update
        self.service = service
        self.router = router
        self.tags = tags
        self.methods = methods or ["create", "get-all", "get", "update", "delete"]
        self._create_routes()

    def _create_routes(self):
        if "create" in self.methods:
            @self.router.post("/create", response_model=self.schem_in_db, status_code=201, tags=self.tags)
            def create(*, obj_in: self.schem_create) -> self.schem_in_db:
                return self.service.create(obj_in=obj_in)
            
        