from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.users.exceptions import user_not_found_exception, user_creation_exception, user_update_exception, user_deletion_exception

def user_not_found_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=404,
        content={"message": str(exc)},
    )

def user_creation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )

def user_update_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )

def user_deletion_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )

def validation_exception_handler(request: Request, exc: RequestValidationError):
    formatted = []

    for err in exc.errors():
        formatted.append({
            "field": err["loc"][-1],
            "message": err["msg"]
        })

    return JSONResponse(
        status_code=400,
        content={
            "error": "VALIDATION_ERROR",
            "details": formatted
        }
    )

def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred. Please try again later."},
    )

def register_global_exception_handler(app):
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(user_not_found_exception, user_not_found_exception_handler)
    app.add_exception_handler(user_creation_exception, user_creation_exception_handler)
    app.add_exception_handler(user_update_exception, user_update_exception_handler)
    app.add_exception_handler(user_deletion_exception, user_deletion_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)