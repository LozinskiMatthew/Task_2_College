from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from datetime import datetime
import os
from app.weather import get_weather

app = FastAPI()

PORT = int(os.getenv("PORT", 8080))
AUTHOR = "Matthew Lozinski"
START_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"[INFO] App started at {START_TIME}")
print(f"[INFO] Author: {AUTHOR}")
print(f"[INFO] Listening on TCP port: {PORT}")

countries = {
    "Poland": ["Warsaw", "Krakow"],
    "Germany": ["Berlin", "Munich"],
    "USA": ["New York", "Los Angeles"]
}

@app.get("/", response_class=HTMLResponse)
async def index():
    form = """
        <form method="get" action="/weather">
            <label>Country:</label>
            <select name="country">
                <option>Poland</option>
                <option>Germany</option>
                <option>USA</option>
            </select><br/>
            <label>City:</label>
            <select name="city">
                <option>Warsaw</option>
                <option>Berlin</option>
                <option>New York</option>
            </select><br/>
            <input type="submit" value="Get Weather" />
        </form>
    """
    return form

@app.get("/weather", response_class=HTMLResponse)
async def weather(request: Request):
    country = request.query_params.get("country")
    city = request.query_params.get("city")
    if country not in countries or city not in countries[country]:
        return "Invalid selection"
    weather_data = get_weather(city)
    return f"<h2>Weather in {city}</h2><p>{weather_data}</p>"
