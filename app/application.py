from fastapi import FastAPI

from app.domain.user.schemas import ResponseUser
from app.domain.customer.schemas import ResponseCustomer
from app.domain.post.schemas import ResponsePost

from app.domain.user.routes import user_router
from app.domain.customer.routes import customer_router
from app.domain.post.routes import post_router

app = FastAPI()

ResponseUser.model_rebuild()
ResponseCustomer.model_rebuild()
ResponsePost.model_rebuild()

app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(customer_router, prefix="/customer", tags=["Customer"])
app.include_router(post_router, prefix="/post", tags=["Post"])