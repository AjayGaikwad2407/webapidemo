from fastapi import FastAPI
from datetime import date, timedelta
import random
from app.models import WeatherForecast

SUMMARIES = [
    "Freezing",
    "Bracing",
    "Chilly",
    "Cool",
    "Mild",
    "Warm",
    "Balmy",
    "Hot",
    "Sweltering",
    "Scorching",
]

app = FastAPI(title="webapidemo (Python)")


@app.get("/WeatherForecast", response_model=list[WeatherForecast])
def get_weather():
    rng = random.Random()
    forecasts = []
    for i in range(5):
        d = date.today() + timedelta(days=i)
        temp_c = rng.randint(-20, 55)
        temp_f = 32 + int(temp_c / 0.5556)
        summary = rng.choice(SUMMARIES)
        forecasts.append(
            WeatherForecast(
                date=d, temperatureC=temp_c, temperatureF=temp_f, summary=summary
            )
        )
    return forecasts
