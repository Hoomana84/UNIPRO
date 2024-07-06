from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# app = FastAPI()
#
# templates = Jinja2Templates(directory='templates')
#
#
# @app.get('/home/{username}', response_class=HTMLResponse)
# def index(request: Request, username: str):
#     return templates.TemplateResponse('home.html', {'request': request, 'username': username})
