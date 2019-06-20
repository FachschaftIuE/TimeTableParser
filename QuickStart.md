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

* Lege die auszulesende Stundenplan-PDF in den Input-Ordner ab (`data/input`)
* ``` 
  python python-scripts/main.py
	```
* Es folgt eine Konsolenabfrage zu den gewünschten Modulen.
* Formatierter Stundenplan ist in dem Output-Ordner in Form von einer `.csv`- oder `.ics`-Datei, je nach Wunsch, zu im Output-Ordner zu finden (`data/output`)
* Importiere das gewünschte Format in den Kalender
* `.ics` = für Apple Anwendungen 
* `.csv` = für Meisten anderen Kalenderanwendungen

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
*	Save timetable-PDF in input-folder (`data/input`)
* ```bash
  python python-scripts/main.py
  ```
* A console query will ask you to choose your modules
* Formatted timetable will be created in form of a `.csv`- or `.ics`-file, depending on your choice, in the output-folder (`data/output`)
* Import your prefered file to your calendar
* `.ics` = for Apple Applications
* `.csv` = for most other Applications

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
