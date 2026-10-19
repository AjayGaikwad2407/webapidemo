from pydantic import BaseModel
from datetime import date


class WeatherForecast(BaseModel):
    date: date
    temperatureC: int
    temperatureF: int
    summary: str
