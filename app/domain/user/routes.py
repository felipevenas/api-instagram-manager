from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.domain.user.repository import UserRepository
from app.domain.user.service import UserService
from app.domain.user.schemas import ResponseUser, CreateUser, UpdateUser

user_router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    return UserService(repository)

@user_router.post("/register", response_model=ResponseUser, summary=["Criar um novo usuário"])
def create(data: CreateUser, service: UserService = Depends(get_user_service)):
    return service.create(data)

@user_router.get("", response_model=list[ResponseUser], summary=["Listar todos os usuários"])
def get_all(service: UserService = Depends(get_user_service)):
    return service.get_all()

@user_router.get("/{user_id}", response_model=ResponseUser, summary=["Buscar um usuário pelo ID"])
def get_by_id(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_by_id(user_id)

@user_router.put("/{user_id}", response_model=UpdateUser, summary=["Atualizar um usuário pelo ID"])
def update(user_id: int, data: UpdateUser, service: UserService = Depends(get_user_service)):
    return service.update(user_id, data)

@user_router.delete("/{user_id}", response_model=ResponseUser, summary=["Delete um usuário pelo ID"])
def delete(user_id: int, service: UserService = Depends(get_user_service)):
    return service.delete(user_id)