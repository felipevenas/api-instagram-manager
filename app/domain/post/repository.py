from sqlalchemy.orm import Session

from app.domain.post.model import Post
from app.domain.post.schemas import CreatePost, UpdatePost

class PostRepository:
	def __init__(self, db: Session):
		self.db = db

	def create(self, data: CreatePost):
		post = Post(**data.model_dump())
		self.db.add(post)
		self.db.commit()
		self.db.refresh(post)
		return post

	def get_all(self):
		return self.db.query(Post).all()

	def get_by_id(self, post_id: int):
		return self.db.query(Post).filter(Post.id == post_id).first()

	def update(self, post_id: int, data: UpdatePost):
		db_post = self.get_by_id(post_id)
		if db_post:
			for key, value in data.model_dump(exclude_unset=True).items():
				setattr(db_post, key, value)
			self.db.commit()
			self.db.refresh(db_post)
		return db_post

	def delete(self, post_id: int):
		db_post = self.get_by_id(post_id)
		if db_post:
			self.db.delete(db_post)
			self.db.commit()
			return db_post
		return None
