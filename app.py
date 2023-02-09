from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/")
def healthcheck():
    test_response = jsonable_encoder({"status": "Ok"})
    return JSONResponse(content=test_response)
