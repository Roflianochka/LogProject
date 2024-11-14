from fastapi import APIRouter
from  api.handlers.user_handler import *
from  api.handlers.employee_log_handler import *
router = APIRouter(prefix="/handlers")
router.include_router(router=user_handler.router)
router.include_router(router=employee_log_handler.router)