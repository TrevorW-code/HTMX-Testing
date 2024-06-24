import argparse
from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from settings import settings

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # You can specify your allowed origins here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.post('/blogs')
async def sample_blog(request: Request):

    return templates.TemplateResponse(
        request=request, name="list.html"
    ) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the server.")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload")
    args, unknown = parser.parse_known_args()

    if args.reload:
        uvicorn.run(
            "main:app",
            host=settings.FAST_API_HOST,
            port=settings.FAST_API_PORT,
            reload=True,
        )
    else:
        uvicorn.run(
            app, 
            host=settings.FAST_API_HOST, 
            port=settings.FAST_API_PORT
        )
