# Big-Data-Abgabe

Für die Big Data Abgabe wurde ein Github Repository erstellt, welches unter folgendem Link zu finden ist:
https://github.com/Mehmet1700/Big-Data-Abgabe

Zum testen des Codes müssen die Dependencies installiert werden. Hierzu kann die Pipfile genutzt werden. Wenn die Pipenv läuft, kann der Code ausgeführt werden.
Die Abgabe kann getestet werden indem das Repository geklont wird und die main.py (unte dem Ordner src/fifaBeispiel) ausgeführt wird.
Hierzu bitte folgende Befehle in die Konsole eingeben:

```
pipenv install
pipenv shell
cd src/fifaBeispiel
python3 main.py
```


Der Ordner testPySpark und vorlesungTests sind nicht relevant für die Abgabe und wurden nur zum Testen verwendet.
Dieser wurde nicht gelöscht, um die Entwicklung nachvollziehen zu können.
Es wurden zuerst Tests mit PySpark durchgeführt, um die Funktionstüchtigkeit von PySpark zu testen.


Aufgabenstellung und/oder Fragestellungen
Angelehnt an das FIFA Beispiel sollen folgende Fragestellungen beantwortet werden.  
Falls ein eigenes Datenset verwendet wird, bitte die Fragen in den Code dokumentieren.

* Welche Mannschaften/Länder haben am meisten im Heimspiel bzw Auswärts gewonnen?
* Wer sind die erfolgreichsten Mannschaften/Länder der letzten 10 Jahre bzw wie oft haben diese gewonnen?
* Welche Mannschaft/Land hat die meisten Tore geschossen?

Die Bewertungskriterien sollen Schritt für Schritt erläutert werden, um die Bewertung nachvollziehbar zu machen.
Es soll als eine Checkliste fungieren, die abgearbeitet werden kann.

## Bewertungskriterien

1. Muss - ein Ressourcen File muss vorhanden sein (setup.py, pom.xml, build.sbt...) wo alle
   Abhängigkeiten aufgelistet werden.
    * Es wird eine pipfile verwendet, die alle Abhängigkeiten auflistet.
    * Außerdem wurde eine setup.py erstellt, die sich an der Datei aus der Vorlesung orientiert.

2. Muss - Es muss eine Hauptfunktion (z.B. Java public static void main, Python if
   __name__ == "__main__”) geben
    * Die Hauptfunktion ist in der Datei /src/fifaBeispiel/main.py
   

3. Muss - Es muss mindestens ein Sub-Modul/Paket vorhanden sein, welches nicht im
   selben Directory liegt wie die Hauptfunktion
    * Das Sub-Modul bzw. Paket ist unter /src/fifaBeispiel/ zu finden und lautet main.
    * In diesem Paket befindet sich eine init.py, fifaberechnungen.py und fifaberechnunngen.ipynb.
    * In der init.py werden die Funktionen aus fifaberechnungen.py importiert.
    * In fifaberechnungen.py befinden sich die Funktionen, die die Berechnungen durchführen.
    * Die Datei fifaberechnungen.ipynb ist dazu da, um bei der Entwicklung zu helfen und Funktionen zu testen. Diese kann gerne angeschaut werden, aber ist nicht einfach nachvollziehbar. Es diente nur als Spielewiese, um Funktionen zu testen.


4. Muss - Es muss mindestens eine inhaltliche Frage (Beispiele siehe oben -
   Fragestellungen angelehnt an das Reddit Beispiel) bearbeitet werden
    * Die Fragestellungen sind in der Readme Datei zu finden. Es werden alle Fragestellungen nacheinander beantwortet und in der Konsole ausgegeben beim Ausführen.


5. Muss - Der Code muss bei der Abgabe lauffähig sein.
    * Der Code ist lauffähig. Es muss nur die main.py ausgeführt werden.
    * Das Programm soll getestet werden, indem der Code auf einem anderen System ausgeführt wird.


6. Soll - Der Code soll dementsprechend dokumentiert sein, insb. geschriebene Funktionen
   müssen/sollen eine Dokumentation enthalten.
    * Die Funktionen sind dokumentiert soweit es sinn ergibt. Die Funktionen sind nicht komplex und daher ist eine Dokumentation nicht unbedingt notwendig.


7. Muss - Der Code muss leserlich sein, d.h. entsprechende Einrückungen und Umbrüche
   haben.
   * Der Code ist leserlich. Es sind Einrückungen und Umbrüche vorhanden. 
   * Hierzu wird bei PyCharm Option+Command+L verwendet.


8. Soll - Methoden, Variablen, Klassen sollen einen ansprechenden Namen erhalten.
   * Die Methoden, Variablen und Klassen haben einen ansprechenden Namen.
   

9. Muss - Der Code muss auf Skalierung ausgelegt sein. Falls sie sich bei verwendeten
   Bibliotheken unsicher sind, lassen sie sie lieber weg
   * Der Code ist auf Skalierung ausgelegt. Es werden keine Bibliotheken verwendet, die nicht auf Skalierung ausgelegt sind. Eigentlich wird nur PySpark verwendet, welches auf Skalierung ausgelegt ist.


10. Muss – Die ermittelten Statistiken müssen wieder abgespeichert werden
    Wenn vorhanden:
    * Die Ergebnisse aus der Analyse werden in dem Ordner data als .csv Datei abgespeichert.


11. es sollen keine sicherheitssensitiven Informationen, wie Benutzernamen oder
    Passwörter im Source Code stehen
    * Es sind keine sicherheitssensitiven Informationen im Source Code vorhanden.