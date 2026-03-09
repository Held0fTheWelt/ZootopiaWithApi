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


def _no_results_message(animal_name):
    """Return HTML for the 'no animals found' message to show on the website."""
    escaped = animal_name.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (
        '<li class="cards__item">'
        '<div class="card__text">'
        f'<p>No animals found for &quot;{escaped}&quot;. Please try another search.</p>'
        "</div></li>"
    )


def main():
    """Ask for an animal name, fetch data, generate HTML and write to _static."""
    animal_name = input("Please enter an animal: ").strip() or "Fox"
    data = data_fetcher.fetch_data(animal_name)

    with open(template_path, encoding="utf-8") as template_file:
        template_content = template_file.read()

    if not data:
        output = _no_results_message(animal_name)
        print("No animals found. A message has been shown on the website.")
    else:
        output = "".join(serialize_animal(animal) for animal in data)
        print(f"  -> {len(data)} animals loaded")

    text = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)

    print("Done. _static/animals.html has been updated.")


if __name__ == "__main__":
    main()
