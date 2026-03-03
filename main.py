import json
import os
import urllib.request
import urllib.parse


API_BASE = "https://api.api-ninjas.com/v1/animals"
API_KEY = "dYc5rkFfHySUZSJRb5GwT5xBmIyXJ7mkZwXsnmqj"


def fetch_animals_from_api(name):
    """Holt Tier-Daten von der API Ninja Animals API."""
    params = urllib.parse.urlencode({"name": name})
    url = f"{API_BASE}?{params}"
    req = urllib.request.Request(url, headers={"X-Api-Key": API_KEY})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())


def serialize_animal(animal):
    animal_output = ""
    animal_output += '<li class="cards__item">\n'

    if 'name' in animal:
        animal_output += f'<div class="card__title">{animal["name"]}</div>\n'
        animal_output += '<div class="card__text"><ul>'
        if 'characteristics' in animal:
            chars = animal['characteristics']
            if 'diet' in chars:
                animal_output += f"<li><strong>Diet:</strong> {chars['diet']}</li>\n"

        if 'locations' in animal and animal['locations']:
            animal_output += f"<li><strong>Location:</strong> {animal['locations'][0]}</li>\n"

        if 'characteristics' in animal:
            chars = animal['characteristics']
            if 'type' in chars:
                animal_output += f"<li><strong>Type:</strong> {chars['type']}</li>\n"
        animal_output += '</ul></div>'
    animal_output += "</li>\n"
    return animal_output


# Pfade relativ zum Projektroot (dieses Script liegt im Projektroot)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

template_path = os.path.join(BASE_DIR, "_static", "animals_template.html")
output_path = os.path.join(BASE_DIR, "_static", "animals.html")


def main():
    animal_name = input("Tier suchen (z.B. Fox): ").strip() or "Fox"
    print(f"Rufe API auf für: {animal_name!r}")
    try:
        animals_data = fetch_animals_from_api(animal_name)
    except urllib.error.HTTPError as e:
        print(f"API-Fehler: {e.code} – {e.reason}")
        return
    except urllib.error.URLError as e:
        print(f"Netzwerkfehler: {e.reason}")
        return
    except json.JSONDecodeError as e:
        print(f"Ungültige API-Antwort: {e}")
        return

    if not animals_data:
        print("Keine Tiere gefunden. Versuche einen anderen Suchbegriff.")
        return
    print(f"  -> {len(animals_data)} Tiere von der API geladen")

    print("Lade Template:", template_path)
    with open(template_path, encoding="utf-8") as template_file:
        template_content = template_file.read()

    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    text = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    print("Schreibe Ausgabe:", output_path)
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)

    print("Fertig. _static/animals.html wurde aktualisiert.")


if __name__ == "__main__":
    main()

