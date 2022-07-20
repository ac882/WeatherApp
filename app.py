import requests
import json
import os  # api management
from dotenv import load_dotenv  # api management
import os.path


def configure():
    load_dotenv()

class Weather:
    def __init__(self) -> None:
        configure()
        self.API_KEY = os.getenv("API_KEY")
        self.city_value = ""
        self.units = "metric"
        self.error_code = 0

    def handle_error(self, code):
        if code == 404:
            raise CityNotFound(code)

    def showWeather(self, city, isFahrenheit):
        try:
            response_API = requests.get(
                "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}".format(
                    city, self.API_KEY, self.units
                )
            )
            data = response_API.text
            parse_json = json.loads(data)

            response_API.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e.response.status_code)
            self.handle_error(e.response.status_code)

        country = parse_json["sys"]["country"]
        city = parse_json["name"]
        current_temp = int(parse_json["main"]["temp"])
        feels_like = int(parse_json["main"]["feels_like"])
        temp_max = int(parse_json["main"]["temp_max"])
        temp_min = int(parse_json["main"]["temp_min"])
        pressure = int(parse_json["main"]["pressure"])
        humidity = int(parse_json["main"]["humidity"])

        if isFahrenheit == 1:
            current_temp = (current_temp * 1.8) + 32
            feels_like = (feels_like * 1.8) + 32
            temp_max = (temp_max * 1.8) + 32
            temp_min = (temp_min * 1.8) + 32

        weather = "Country: {}\nCity: {}\nCurrent Temp: {}\nFeels Like: {}\nTemp Max: {}\nTemp Min: {}\nPressure: {}\nHumidity: {}\n".format(
            country,
            city,
            current_temp,
            feels_like,
            temp_max,
            temp_min,
            pressure,
            humidity,
        )
        print("\n##### WEATHER INFO #####\n")
        print(weather)
        return weather


class CityNotFound(Exception):
    def __init__(self, code, msg="City not found"):
        self.code = code
        self.msg = msg
        super().__init__(self.msg)
