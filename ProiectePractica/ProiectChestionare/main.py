from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse

from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

import logging

from src.Backend.API.OAuth2PasswordBearerWithCookie import OAuth2PasswordBearerWithCookies
from src.Backend.API.User import router as users_routes


logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

oauth2_scheme = OAuth2PasswordBearerWithCookies(tokenUrl="token")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static") # HTML
app.mount("/dist", StaticFiles(directory="dist"), name="dist") # JS
app.mount("/dist2", StaticFiles(directory="dist2"), name="dist2") # JS
app.include_router(users_routes)



from src.Backend.API.Handlers import validation_exception_handler as vse
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request:Request, exception : RequestValidationError):
    return await vse(request, exception)

from src.Backend.API.Handlers import http_exception_handler as heh
@app.exception_handler(HTTPException)
async def http_exception_handler(request:Request, exception : HTTPException):
    return await heh(request, exception)



@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("static/index.html")

@app.get("/login", response_class=FileResponse)
async def login_page():
    return FileResponse("static/login.html")

@app.get("/register")
async def register_page():
    return FileResponse("static/register.html")

