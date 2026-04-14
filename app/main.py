from fastapi import FastAPI
from app.core.global_exceptions.global_exception_handler import register_global_exception_handler
from app.core.transactions.routes.TransactionRoutes import router as TransactionRoutesClass
from app.core.users.routes.user_routes import router as UserRoutesClass
from app.core.db.DBConnection import Base, engine

app = FastAPI()
register_global_exception_handler(app)

Base.metadata.create_all(bind=engine)

app.include_router(TransactionRoutesClass, prefix="/transactions")
app.include_router(UserRoutesClass, prefix="/users")