from fastapi import FastAPI, Request, Response
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/id", response_class=PlainTextResponse)
async def get_id(request: Request):
    client_host = request.client.host
    return client_host

