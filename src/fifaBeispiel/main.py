"""
In dieser Datei wird die main Methode aufgerufen.
In der main Methode wird die runSpark Methode aufgerufen, welche aus der fifaBerechnungen.py Datei importiert wird.
Der Codeteil ist aus der Vorlesung übernommen und wurde nur leicht angepasst.
"""


def main():
    # Import runSpark from fifaBerechnungen.py
    from src.fifaBeispiel.main.fifaBerchnungen import runSpark
    # Call runSpark aus der fifaBerechnungen.py Datei
    runSpark()


# Call main function. Das ist der Einstiegspunkt in unsere App
if __name__ == '__main__':
    '''
    This is the main entry point of our App Everything starts here
    PLEASE KEEP THIS ROUTINE FLAT
    '''
    main()
