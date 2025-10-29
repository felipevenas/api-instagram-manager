from sqlalchemy.orm import Session

from app.domain.user.model import User
from app.domain.user.schemas import ResponseUserSimple, CreateUser, UpdateUser

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: CreateUser):
        db_user = User(**data.model_dump())
        self.db.add(db_user)
        self.db.commit()
        return db_user

    def get_all(self) -> list[ResponseUserSimple]:
        return self.db.query(User).all()

    def get_by_id(self, user_id: int):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            return db_user
        return None
    
    def update(self, user_id: int, data: UpdateUser):
        db_user = self.get_by_id(user_id)
        if db_user:
            for key, value in data.dict().items():
                setattr(db_user, key, value)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def delete(self, user_id: int):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return db_user
        return None