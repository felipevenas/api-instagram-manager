from fastapi import HTTPException, status

from app.domain.post.repository import PostRepository
from app.domain.post.schemas import BasePost, CreatePost, UpdatePost


class PostService:
	def __init__(self, repository: PostRepository):
		self.repository = repository

	def create(self, data: CreatePost):
		post = self.repository.create(data)
		if post:
			return post
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Não foi possível criar o post")

	def get_all(self):
		posts = self.repository.get_all()
		if posts:
			return [p for p in posts]
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum post encontrado")

	def get_by_id(self, post_id: int):
		post = self.repository.get_by_id(post_id)
		if post:
			return post
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post não encontrado")

	def update(self, post_id: int, data: UpdatePost):
		updated = self.repository.update(post_id, data)
		if updated:
			return updated
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post não encontrado para atualização")

	def delete(self, post_id: int):
		deleted = self.repository.delete(post_id)
		if deleted:
			return deleted
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post não encontrado para deletar")

