import configparser
import argparse
import json
import sys
from urllib import parse, request, error


# getting api_key
base_url = "http://api.openweathermap.org/data/2.5/weather"


def _getapi_key():
    config = configparser.ConfigParser()
    config.read("secret.ini")
    return config["openweather"]["api_key"]


def api_query(city_name, imperial=False):
    api_key = _getapi_key()
    city_name = ' '.join(city_name)
    url_encoded_city_name = parse.quote_plus(city_name)
    unit = "metric"
    if imperial:
        unit = "imperial"
    url = (f"{base_url}?q={url_encoded_city_name}&units={unit}&appid={api_key}")
    return url

# reading from the command prompt


def read_cli():
    parser = argparse.ArgumentParser(
        description="Helps to get weather forecast by city name")
    parser.add_argument(
        "city", nargs="+", type=str, help="Eter city name"
    )
    parser.add_argument(
        "-i", "--imperial", action="store_true", help="get weather info in imperial units"
    )

    return parser.parse_args()


def weather_data(url):
    try:
        response = request.urlopen(url)
    except error.HTTPError:
        sys.exit("Data for given city not available.")
    data = response.read()
    return json.loads(data)


def display(weather, imp=False):
    city = weather["name"]
    weather_dec = weather["weather"][0]["description"]
    curr_temp = weather["main"]["temp"]
    feel_temp = weather["main"]["feels_like"]
    min_temp = weather["main"]["temp_min"]
    max_temp = weather["main"]["temp_max"]

    print(f"{city}")
    print(f"{weather_dec.capitalize()}")
    print(f"temp : {curr_temp}°{'F' if imp else 'C'}", end=' ')
    print(f"\t(feels like : {feel_temp}°{'F' if imp else 'C'})")
    print(f"min temp : {min_temp}°{'F' if imp else 'C'}")
    print(f"max temp : {max_temp}°{'F' if imp else 'C'}")


if __name__ == "__main__":
    obj = read_cli()
    url = api_query(obj.city, obj.imperial)
    weather = weather_data(url)
    display(weather, obj.imperial)
