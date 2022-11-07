from fastapi import FastAPI, Request, Response
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/id")
async def get_id(request: Request):
    if request.client.host is not None:
        return(request.client.host)
    else:
        return(request.headers)
    # client_host = request.client.host
    # return client_host

