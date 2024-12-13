import re
import os

# Funktion zur Lösung des Puzzles mit einer gegebenen Dateiname (filename)
def solve_puzzle(filename):
    try:
        # Ermittelt den absoluten Pfad des aktuellen Skripts und kombiniert ihn mit dem Dateinamen
        script_dir = os.path.dirname(os.path.realpath(__file__))
        input_path = os.path.join(script_dir, filename)

        # Öffnet die Datei und liest deren Inhalt
        with open(input_path, 'r') as file:
            data = file.read()

        # Regex Pattern zur Erkennung von gültigen mul(X,Y) Anweisungen
        mul_pattern = re.compile(r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)")
        # Regex Pattern zur Erkennung von do() Anweisungen
        do_pattern = re.compile(r"do\(\s*\)")
        # Regex Pattern zur Erkennung von don't() Anweisungen
        dont_pattern = re.compile(r"don't\(\s*\)")

        # Initialisierung der Variablen
        total = 0         # Zum Speichern der Summe der Multiplikationsergebnisse
        mul_enabled = True  # Zu Beginn sind mul Anweisungen aktiviert

        # Position zum Durchlaufen des Datenstrings
        pos = 0
        while pos < len(data):
            # Überprüft auf Übereinstimmungen mit den Patterns an der aktuellen Position
            mul_match = mul_pattern.match(data, pos)
            do_match = do_pattern.match(data, pos)
            dont_match = dont_pattern.match(data, pos)

            # Wenn eine gültige mul(X,Y) Anweisung gefunden wird
            if mul_match:
                # Wenn mul Anweisungen aktuell aktiviert sind
                if mul_enabled:
                    # Extrahiert die Zahlen X und Y und berechnet das Produkt
                    x, y = mul_match.groups()
                    total += int(x) * int(y)
                # Setzt die Position hinter das Ende der gefundenen mul Anweisung
                pos = mul_match.end()
            # Wenn eine do() Anweisung gefunden wird
            elif do_match:
                # Aktiviert zukünftige mul Anweisungen
                mul_enabled = True
                # Setzt die Position hinter das Ende der gefundenen do Anweisung
                pos = do_match.end()
            # Wenn eine don't() Anweisung gefunden wird
            elif dont_match:
                # Deaktiviert zukünftige mul Anweisungen
                mul_enabled = False
                # Setzt die Position hinter das Ende der gefundenen don't Anweisung
                pos = dont_match.end()
            else:
                # Wenn keine Übereinstimmung gefunden wird, erhöhe die Position um 1
                pos += 1

        # Gibt die berechnete Gesamtsumme zurück
        return total

    except FileNotFoundError:
        # Fehlerbehandlung, falls die Datei nicht gefunden wird
        print(f"File {filename} not found.")
        return None

# Hauptteil des Programms, wird nur ausgeführt wenn das Skript direkt aufgerufen wird
if __name__ == "__main__":
    # Definiert den Dateinamen der Eingabedaten
    input_filename = 'input.txt'
    # Ruft die Funktion solve_puzzle auf und speichert das Ergebnis
    result = solve_puzzle(input_filename)
    # Wenn ein Ergebnis vorliegt, wird es ausgegeben
    if result is not None:
        print(f"The sum of all valid and enabled mul(X,Y) instructions is: {result}")