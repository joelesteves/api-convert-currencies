from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router=router)

@app.get('/helloworld')
def helloworld():
    return "Hello World!!!!"
