from app.domain.user.repository import UserRepository
from app.domain.user.schemas import CreateUser, UpdateUser

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, data: CreateUser):
        return self.repository.create(data)
    
    def get_all(self):
        return self.repository.get_all()
    
    def get_by_id(self, user_id: int):
        return self.repository.get_by_id(user_id)
    
    def update(self, user_id: int, data: UpdateUser):
        return self.repository.update(user_id, data)
    
    def delete(self, user_id: int):
        return self.repository.delete(user_id)