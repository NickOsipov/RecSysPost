import yaml
import pandas as pd
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from catboost import CatBoostClassifier

from database import ENGINE


app = FastAPI()


def batch_load_sql(query: str, chunksize=200_000) -> pd.DataFrame:
    conn = ENGINE.connect().execution_options(stream_results=True)
    df = pd.DataFrame()
    for df_chunk in pd.read_sql(query, conn, chunksize=chunksize):
        df = pd.concat([df, df_chunk], ignore_index=True)
    conn.close()
    return df


def load_model():
    with open("config/config.yaml") as config:
        config = yaml.safe_load(config)
        model_path = config.get("MODEL_PATH")
    model = CatBoostClassifier()
    model.load_model(model_path)
    return model


@app.get("/test")
def healthcheck():
    test_response = jsonable_encoder({"status": "Ok"})
    return JSONResponse(content=test_response)
