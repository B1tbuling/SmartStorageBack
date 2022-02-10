from typing import Optional

from fastapi import FastAPI

from db import get_last_three_value, get_sensor_one_data, get_sensor_two_data, get_sensor_three_data

app = FastAPI()

@app.get("/")
def get_data():
    return get_last_three_value()


@app.get("/sensor1")
def get_data(limit):
    return get_sensor_one_data(limit)

@app.get("/sensor2")
def get_data():
    return get_sensor_two_data()

@app.get("/sensor3")
def get_data():
    return get_sensor_three_data()