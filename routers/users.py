from starlette import status
from starlette.responses import RedirectResponse, HTMLResponse
from fastapi import Request, Form, APIRouter, Depends
from fastapi.templating import Jinja2Templates
import models
from .auth import get_current_user, verify_password, get_password_hash
from database import SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel

router = APIRouter(
    prefix='/user',
    tags=['User'],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)

templates = Jinja2Templates(directory='templates')


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class SUserChangePassword(BaseModel):
    username: str
    password: str
    new_password: str
    verify_new_password: str


@router.get("/change-password", response_class=HTMLResponse)
async def user_view(request: Request):
    user = await get_current_user(request)
    if not user:
        return RedirectResponse(url="/auth", status_code=status.HTTP_401_UNAUTHORIZED)
    return templates.TemplateResponse("change-password.html", {"request": request, "user": user})


@router.post('/change-password', response_class=HTMLResponse)
async def change_password(request: Request,
                          username: str = Form(...),
                          password: str = Form(...),
                          new_password: str = Form(...),
                          verify_new_password: str = Form(...),
                          db: Session = Depends(get_db)):
    user = await get_current_user(request)
    if not user:
        return RedirectResponse(url="/auth", status_code=status.HTTP_401_UNAUTHORIZED)

    user_model = db.query(models.Users).filter(models.Users.username == username).first()

    msg = "Username or Password is incorrect"
    delete_token = False
    return_page = "change-password.html"
    if user_model is not None:
        if username == user_model.username and verify_password(password, user_model.hashed_password):
            if new_password == verify_new_password:
                user_model.hashed_password = get_password_hash(new_password)
                db.add(user_model)
                db.commit()
                delete_token = True
                msg = "Password changed successful"
                return_page = "login.html"
            else:
                msg = "Verification password does not match new password"

    response = templates.TemplateResponse(return_page, {"request": request,
                                                        "msg": msg,
                                                        "user": user})
    if delete_token:
        response.delete_cookie(key="access_token")
    return response
