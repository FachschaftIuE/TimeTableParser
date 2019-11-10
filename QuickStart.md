# QuickStart - TimeTableParser (TTP)

Supported languages for QuickStart:  - english
				     - deutsch

Program language: english

# Deutsch

## Haftungsbeschränkung
Die Inhalte des TimeTableParser (TTP) wurden mit größtmöglicher Sorgfalt und nach bestem Gewissen erstellt. 
Dennoch übernimmt der Anbieter dieser Applikation keine Gewähr für die Aktualität, Vollständigkeit und 
Richtigkeit der bereitgestellten csv/ics-Dateien und weiterer Inhalte.

## Voraussetzungen

Zum Benutzen der Anwendung wird [Python Version 3.7.2](https://www.python.org) (oder höher) benötigt.

Installiere Abhängigkeiten mithilfe von `pip`

```bash
pip install -r requirements.txt
```

## Verwendung
* Windows
    1.  Führe TTP.exe in  release/vX-X-X/ aus. Hinweis: Du musst evtl. die Datei vorher entpacken.
    2.  Füge Stundenpläne hinzu, die konvertiert werden sollen.
    3.  Setze die Einstellungen, die du willst.
    4.  Lese und erkläre dich mit den AGB/TOS einverstanden. Hinweis: Hierfür musst du Englisch verstehen können.
    5.  Drücke auf 'Parse Timetable(s)'.
    6.  Wähle die Module aus, die in den Kalendar integriert werden sollen.
    7.  Drücke auf 'Create Calendar'.
    8.  Der Calendar befindet sich im Verzeichnis ./data/output.
    
* Andere Betriebssysteme
    1.  Führe ```python python-scripts/main.py``` in dem Wurzelverzeichnis aus.
    2.  Füge Stundenpläne hinzu, die konvertiert werden sollen.
    3.  Setze die Einstellungen, die du willst.
    4.  Lese und erkläre dich mit den AGB/TOS einverstanden. Hinweis: Hierfür musst du Englisch verstehen können.
    5.  Drücke auf 'Parse Timetable(s)'.
    6.  Wähle die Module aus, die in den Kalendar integriert werden sollen.
    7.  Drücke auf 'Create Calendar'.
    8.  Der Calendar befindet sich im Verzeichnis ./data/output.

## Ordnerstruktur
```
+---data
|   +---cache
|   +---input
|   +---output
+---python-scripts
    +---classes
    |   +---controller
    |   +---file_management
    |   +---interface
    |   +---models
    |   +---timetable_parts
    +---helper
    +---packages
```

 
# English
## Limitation of liability (Disclaimer)
The contents of the TimeTableParser (TTP) were compiled with the greatest possible care and in accordance 
with in the best of conscience. Nevertheless, the provider of this application does not assume any liability
for the topicality, completeness and correctness of the csv/ics files and other content provided. 

## Requirements

[Python version 3.7.2](https://www.python.org) (or higher) is needed to execute the application.

Install using `pip`

```bash
pip install -r requirements.txt
```

## Usage
* Windows
    1.  Run TTP.exe in  release/vX-X-X/. Hint: You might need to unzip it first. 
    2.  Add Timetables that are going to be parsed.
    3.  Adjust settings to your liking.
    4.  Read and agree to Terms of Service.
    5.  Press 'Parse Timetable(s)'.
    6.  Choose desired modules for the calendar.
    7.  Press 'Create Calendar'.
    8.  The calendar will be in ./data/output.
    
* Other OS
    1.  Run ```python python-scripts/main.py``` in root-directory.
    2.  Add Timetables that are going to be parsed.
    3.  Adjust settings to your liking.
    4.  Read and agree to Terms of Service.
    5.  Press 'Parse Timetable(s)'.
    6.  Choose desired modules for the calendar.
    7.  Press 'Create Calendar'.
    8.  The calendar will be in ./data/output.

## Folder Structure
```
+---data
|   +---cache
|   +---input
|   +---output
+---python-scripts
    +---classes
    |   +---controller
    |   +---file_management
    |   +---interface
    |   +---models
    |   +---timetable_parts
    +---helper
    +---packages
```
