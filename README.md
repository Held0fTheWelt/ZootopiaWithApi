# ZootopiaWithApi

Kleine Anwendung, die Tierdaten von der [API Ninja Animals API](https://www.api-ninjas.com/api/animals) lädt und daraus eine HTML-Seite erzeugt.

## Voraussetzungen

- Python 3.x
- API-Key von [API Ninjas](https://api-ninjas.com/)

## Installation

```bash
pip install -r requirements.txt
```

## Konfiguration

Im Projektroot eine Datei `.env` anlegen mit deinem API-Key:

```
API_KEY='dein-api-key-hier'
```

(Keine Leerzeichen zwischen Key und Wert.)

## Start

```bash
python main.py
```

Beim Start wird nach einem Tiernamen gefragt (z. B. „Fox“). Die generierte Seite liegt danach unter `_static/animals.html`.

## Projektstruktur

- `main.py` – Einstiegspunkt
- `data/data_fetcher.py` – holt Tierdaten von der API
- `features/animals_web_generator.py` – baut die HTML-Seite aus den Daten
- `_static/` – Template und generierte HTML-Datei
- `data/` – Datenmodul und optionale JSON-Daten
