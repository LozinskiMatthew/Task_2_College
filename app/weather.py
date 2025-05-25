import random

def get_weather(city):
    temp = round(random.uniform(-10, 35), 1)
    desc = random.choice(["Sunny", "Cloudy", "Rainy", "Snowy"])
    return f"{desc}, {temp}°C"
