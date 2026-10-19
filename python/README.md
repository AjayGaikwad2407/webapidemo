# webapidemo (Python)

This is a Python port of the webapidemo WeatherForecast API using FastAPI.

Quick start

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

2. Run the app locally:

```bash
uvicorn app.main:app --reload --port 8000
```

3. Open the endpoint:

http://localhost:8000/WeatherForecast

Docker build

```bash
docker build -t webapidemo-python:latest -f Dockerfile .
docker run -p 80:80 webapidemo-python:latest
```
