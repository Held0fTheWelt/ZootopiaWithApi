import json
import urllib.request
import urllib.parse
import urllib.error


API_KEY = "dYc5rkFfHySUZSJRb5GwT5xBmIyXJ7mkZwXsnmqj"
API_BASE = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    params = urllib.parse.urlencode({"name": animal_name})
    url = f"{API_BASE}?{params}"
    req = urllib.request.Request(url, headers={"X-Api-Key": API_KEY})
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print(f"API error: {e.code} – {e.reason}")
        return []
    except urllib.error.URLError as e:
        print(f"Network error: {e.reason}")
        return []
    except json.JSONDecodeError as e:
        print(f"Invalid API response: {e}")
        return []
