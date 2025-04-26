import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class Connector:
    def __init__(self):
        self.url = lambda city : f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    
    def response(self,city=None):
        if city is None:
            res = requests.get("http://ip-api.com/json/")
            city = res.json().get("city", "London")

        response = requests.get(self.url(city))
        response = response.json()
        if response["cod"] == 200:
            response = {
                    "name": response["name"],
                    "description": response["weather"][0]["description"],
                    "temperature": response["main"]["temp"],
                    "feels_like": response["main"]["feels_like"],
                    "wind": response["wind"]["speed"],
                    "local_time": (datetime.utcnow() + timedelta(seconds=response["timezone"])).strftime('%H:%M'),
                    "sunrise": datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"]).strftime('%H:%M'),
                    "sunset": datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"]).strftime('%H:%M')
                }
        else:
            response = None
        print(response)
        return response

connector = Connector()
print(connector.response("Vien"))