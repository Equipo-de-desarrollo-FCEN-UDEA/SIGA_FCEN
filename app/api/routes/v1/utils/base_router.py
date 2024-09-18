from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from typing import Type
from pydantic import BaseModel
from uuid import UUID


class BaseRouter:
    def __init__(self, schem_in_db: Type[BaseModel], schem_create: Type[BaseModel], schem_update: Type[BaseModel], service, router: APIRouter, methods: list[str] = None):
        self.schem_in_db = schem_in_db
        self.schem_create = schem_create
        self.schem_update = schem_update
        self.service = service
        self.router = router
        self.methods = methods or ["create", "get-all", "get", "update", "delete"]
        self._create_routes()

    def _create_routes(self):
        if "create" in self.methods:
            @self.router.post("/create", response_model=self.schem_in_db, status_code=201)
            def create(*, obj_in: self.schem_create) -> self.schem_in_db:
                return self.service.create(obj_in=obj_in)
            
        if "get-all" in self.methods:
            @self.router.get("/get-all", response_model=list[self.schem_in_db], status_code=200)
            def get_all(*, skip: int=0, limit: int=10) -> list[self.schem_in_db]:
                return self.service.get_multi(skip=skip, limit=limit)
            
        if "get" in self.methods:
            @self.router.get("/get/{id}", response_model=self.schem_in_db, status_code=200)
            def get_entity(*, id: UUID) -> self.schem_in_db:
                entity = self.service.get(id=id)
                if entity is None:
                    raise HTTPException(status_code=404, detail=f"entity not found")
                return entity
            
        if "update" in self.methods:
            @self.router.patch("/update/{id}", response_model=self.schem_in_db, status_code=200)
            def update(*, id: UUID, obj_in: self.schem_update) -> self.schem_in_db:
                self.service.update(id=id, obj_in=obj_in)
                return JSONResponse(status_code=200, content={"message": "entity updated"})
            
        if "delete" in self.methods:
            @self.router.delete("/delete/{id}", response_model=None, status_code=204)
            def delete(*, id: UUID) -> None:
                self.service.delete(id=id)
                return HTMLResponse(status_code=204)