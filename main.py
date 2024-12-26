from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

# Static files for CSS and images
app.mount("/static", 
          StaticFiles(directory="static"), 
          name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Home route
# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
    # return templates.TemplateResponse("index.html", 
                                    #   {"request": request})

# Resume route
@app.get("/", response_class=HTMLResponse)
async def get_resume(request: Request):
    return templates.TemplateResponse("resume.html", 
                                      {"request": request})

# Project route
@app.get("/project", response_class=HTMLResponse)
async def project(request: Request):
    return templates.TemplateResponse("project.html", 
                                      {"request": request})
