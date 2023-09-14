from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, users
from starlette import status
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=RedirectResponse)
async def root():
    return RedirectResponse('/todos', status_code=status.HTTP_302_FOUND)


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
