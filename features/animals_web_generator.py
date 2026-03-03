"""Generates the animals HTML page from fetched animal data."""
import os
from data import data_fetcher


def serialize_animal(animal):
    """Return HTML list item for one animal (name, diet, location, type)."""
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


_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_BASE_DIR)
template_path = os.path.join(_PROJECT_ROOT, "_static", "animals_template.html")
output_path = os.path.join(_PROJECT_ROOT, "_static", "animals.html")


def main():
    """Ask for an animal name, fetch data, generate HTML and write to _static."""
    animal_name = input("Please enter an animal: ").strip() or "Fox"
    data = data_fetcher.fetch_data(animal_name)

    if not data:
        print("No animals found. Try a different search term.")
        return

    print(f"  -> {len(data)} animals loaded")

    with open(template_path, encoding="utf-8") as template_file:
        template_content = template_file.read()

    output = ""
    for animal in data:
        output += serialize_animal(animal)

    text = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)

    print("Done. _static/animals.html has been updated.")


if __name__ == "__main__":
    main()
