# Weather Forecast App

This GitHub project is a simple command-line weather forecast
application that provides current weather information for a given city.
It utilizes the OpenWeatherMap API to fetch weather data.

## Features

- Retrieves current weather data for a specified city
- Supports both metric (Celsius) and imperial (Fahrenheit)unit   systems
- Displays the city name, weather description, current temperature,feels like temperature, minimum temperature, and maximum temperature

## Requirements

- Python 3.x
- 'configparser' library
- 'argparse' library
- 'json' library
- 'urllib' library

## Setup and Usage
1. Clone the repository or download the code files.
2. Obtain an API key from OpenWeatherMap by signing up for a free account.
3. Create a file named secret.ini in the same directory as the code files and add the following content:
 ```
 ; secrets.ini
 [openweather]
 api_key = YOUR_API_KEY
 ```
4. Open a command prompt or terminal and navigate to the project directory.
5. Run the application using the following command:

```
python weather_forecast.py CITY_NAME [-i]

```

6. Replace CITY_NAME with the name of the city for which you want to retrieve the weather forecast.
7. Use the optional -i flag to get the weather information in imperial units (Fahrenheit).

## Example Usage

To get the weather forecast for New York City in metric units:

```
python weather_forecast.py "New York City"

```

To get the weather forecast for London in imperial units:

```
python weather_forecast.py London -i

```

## Acknowledgments

- This project utilizes the OpenWeatherMap API for fetching weather data.
- The code makes use of the configparser, argparse, json, and urllib libraries in Python.
