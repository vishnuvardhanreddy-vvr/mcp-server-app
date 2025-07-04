"""Get Temperature based on city"""

import requests

def temperature(city: str) -> float:
    """
    Fetch current temperature (°C) for a given city in one request using wttr.in.

    Args:
      city (str): City name (e.g., 'Bengaluru' or 'New York')

    Returns:
      float: Current temperature in Celsius

    Raises:
      ValueError: If the API fails or city not found.
    """
    url = f"https://wttr.in/{city}?format=j1"
    resp = requests.get(url, timeout=5)
    if not resp.ok:
        raise ValueError(f"Error fetching weather: HTTP {resp.status_code}")

    data = resp.json()
    try:
        current = data['current_condition'][0]
        return float(current['temp_C'])
    except (KeyError, IndexError, ValueError):
        raise ValueError(f"Could not parse temperature for city: {city}")
