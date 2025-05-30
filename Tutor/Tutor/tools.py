import os 
import requests
from datetime import datetime

def get_date():
    """Returns the current date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")


weather_api_key = os.getenv("WEATHER_API_KEY")
if not weather_api_key:
    raise EnvironmentError("WEATHER_API_KEY not set in environment variables.")

# Use a session for connection reuse
session = requests.Session()

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

            Args:
                city (str): The name of the city for which to retrieve the weather report.

            Returns:
                dict: status and result or error msg.
    """
    base = "http://api.weatherapi.com/v1/current.json"
    url = f"{base}?key={weather_api_key}&q={city}&aqi=no"
    try:
        response = session.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if 'error' in data:
            return {"status": "error", "msg": data['error'].get('message', 'Unknown API error')}

        return {
            "status": "success",
            "report": (
                f"The current weather condition in {data['location']['name']} is "
                f"{data['current']['condition']['text']}. The temperature is {data['current']['temp_c']}°C. "
                f"Wind is {data['current']['wind_kph']} kph and humidity is {data['current']['humidity']}%. "
                f"It feels like {data['current']['feelslike_c']}°C, and the heat index is {data['current']['heatindex_c']}°C. "
                f"There is a projected chance of rain of {data['current']['precip_mm']} mm.\n"
                f"The timezone is {data['location']['tz_id']}."
            )
        }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "msg": f"Failed to fetch weather for {city}. Please try again later."}
