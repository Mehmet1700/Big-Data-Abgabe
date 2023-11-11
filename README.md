# Big-Data-Abgabe

Die Readme Datei ist in deutscher Sprache, da die Aufgabenstellung auch in deutscher Sprache ist.  
Allerdings sind die Kommentare im Code in englischer Sprache, da dies die gängige Sprache ist.  
Der Ordner testPySpark und vorlesungTests sind nicht relevant für die Abgabe und wurden nur zum Testen verwendet.


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
    * Die Fragestellungen sind in der Readme Datei zu finden. Es werden alle Fragestellungen nacheinander beantwortet
      und in der Konsole ausgegeben beim Ausführen.


5. Muss - Der Code muss bei der Abgabe lauffähig sein.
    * Der Code ist lauffähig. Es muss nur die main.py ausgeführt werden.
    * Das Programm soll getestet werden, indem der Code auf einem anderen System ausgeführt wird.


6. Soll - Der Code soll dementsprechend dokumentiert sein, insb. geschriebene Funktionen
   müssen/sollen eine Dokumentation enthalten.
    * Die Funktionen sind dokumentiert soweit es sinn ergibt. Die Funktionen sind nicht komplex und daher ist eine
      Dokumentation nicht unbedingt notwendig.


7. Muss - Der Code muss leserlich sein, d.h. entsprechende Einrückungen und Umbrüche
   haben.
   * Der Code ist leserlich. Es sind Einrückungen und Umbrüche vorhanden. 
   * Hierzu wird bei PyCharm Option+Command+L verwendet.


8. Soll - Methoden, Variablen, Klassen sollen einen ansprechenden Namen erhalten.
   * Die Methoden, Variablen und Klassen haben einen ansprechenden Namen.
   

9. Muss - Der Code muss auf Skalierung ausgelegt sein. Falls sie sich bei verwendeten
   Bibliotheken unsicher sind, lassen sie sie lieber weg
   * Der Code ist auf Skalierung ausgelegt. Es werden keine Bibliotheken verwendet, die nicht auf Skalierung ausgelegt
         sind.


10. Muss – Die ermittelten Statistiken müssen wieder abgespeichert werden
    Wenn vorhanden:
    * 


11. es sollen keine sicherheitssensitiven Informationen, wie Benutzernamen oder
    Passwörter im Source Code stehen
    * Es sind keine sicherheitssensitiven Informationen im Source Code vorhanden.