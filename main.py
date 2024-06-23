from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify your allowed origins here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_index():
    return HTMLResponse('index.html')

@app.post('/blogs')
async def sample_blog():
    data = '''
    <ul>
        <li>Sample Post 1</li>
        <li>Sample Post 2</li>
        <li>Sample Post 3</li>
        <li>Sample Post 4</li>
    </ul>
    '''
    return Response(content=data, media_type='text/html')

if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=5000)
