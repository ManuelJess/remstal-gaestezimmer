# Readme

Um die Webseite zu ändern, entweder lokal installieren und bearbeiten oder direkt auf GitHub. GitHub änderungen werden sofort deployed, lokale Änderungen nach push.

## Lizenz

Diese Webseite steht unter einer [CC-BY-SA Lizenz](https://creativecommons.org/licenses/by-sa/4.0/deed.de)

## Seite lokal aktualisieren

    python -m venv venv
    source venv/bin/activate
    pip install lektor
    lektor server

## TODO
- Automatisches Deploy auf github geht derzeit nicht
- add js form that generates an (example) email
- add caldav integration that shows when we have free space left
