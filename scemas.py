from typing import List, Optional

from pydantic import BaseModel

from datetime import datetime


class SensorData(BaseModel):
    D1:float = None
    D2:float = None 
    D3:float = None
    Time:datetime = None
    ID:int = None


class SensorOneData(BaseModel):
    D1:float = None
    Time:datetime = None

class SensorTwoData(BaseModel):
    D2:float = None
    Time:datetime = None 

class SensorThreeData(BaseModel):
    D3:float = None
    Time:datetime = None 

