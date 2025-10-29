from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.domain.post.repository import PostRepository
from app.domain.post.service import PostService
from app.domain.post.schemas import ResponsePost, CreatePost, UpdatePost

post_router = APIRouter()

def get_post_service(db: Session = Depends(get_db)):
	repository = PostRepository(db)
	return PostService(repository)

@post_router.post("/register", response_model=ResponsePost, summary=["Criar um novo post"])
def create(data: CreatePost, service: PostService = Depends(get_post_service)):
	return service.create(data)

@post_router.get("/", response_model=list[ResponsePost], summary=["Listar todos os posts"])
def get_all(service: PostService = Depends(get_post_service)):
	return service.get_all()

@post_router.get("/{post_id}", response_model=ResponsePost, summary=["Buscar um post pelo ID"])
def get_by_id(post_id: int, service: PostService = Depends(get_post_service)):
	return service.get_by_id(post_id)

@post_router.put("/{post_id}", response_model=ResponsePost, summary=["Atualizar um post pelo ID"])
def update(post_id: int, data: UpdatePost, service: PostService = Depends(get_post_service)):
	return service.update(post_id, data)

@post_router.delete("/{post_id}", response_model=ResponsePost, summary=["Deletar um post pelo ID"])
def delete(post_id: int, service: PostService = Depends(get_post_service)):
	return service.delete(post_id)

