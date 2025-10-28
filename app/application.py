from fastapi import FastAPI
from dotenv import load_dotenv

from app.domain.user.model import User
from app.domain.customer.model import Customer
from app.domain.post.model import Post

from app.domain.user.routes import user_router

load_dotenv()

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["User"])