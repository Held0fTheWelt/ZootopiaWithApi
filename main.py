import json
import os


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


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
data_path = os.path.join(BASE_DIR, "data", "animals_data.json")
output_path = os.path.join(BASE_DIR, "_static", "animals.html")


def main():
    print("Lade Daten aus:", data_path)
    animals_data = load_data(data_path)
    print(f"  -> {len(animals_data)} Tiere gelesen")

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

