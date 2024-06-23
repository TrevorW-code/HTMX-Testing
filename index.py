from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify your allowed origins here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/home", StaticFiles(directory="static"), name="static")

@app.post('/blogs')
async def sample_blog():
    data = '''
    <li>
        <ul>Sample Post 1</ul>
        <ul>Sample Post 2</ul>
        <ul>Sample Post 3</ul>
        <ul>Sample Post 4</ul>
    </li>
    '''
    return Response(content=data, media_type='text/html')

if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=5000)
