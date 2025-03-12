import os
import time
import threading

# Globaler Flag, der angibt, ob das Skript weiterlaufen soll
running = True


def wait_for_quit():
    global running
    while running:
        user_input = input("Geben Sie 'quit' ein, um das Tracking zu beenden: ")
        if user_input.strip().lower() == "quit":
            running = False
            print("Quit-Befehl empfangen. Das Tracking wird beendet.")


# Starte einen separaten Thread, der auf Benutzereingaben wartet
input_thread = threading.Thread(target=wait_for_quit, daemon=True)
input_thread.start()

# Pfade zur Log-Datei, Marker-Datei und Ausgabedatei
log_file = "/Users/work/PycharmProjects/Visure/roni.txt"
marker_file = "/Users/work/PycharmProjects/Visure/marker.txt"
output_file = "/Users/work/PycharmProjects/Visure/NewEntries.txt"

# Lese den letzten Leseoffset aus der Marker-Datei (falls vorhanden)
if os.path.exists(marker_file):
    with open(marker_file, 'r', encoding='utf-8') as mf:
        try:
            last_pos = int(mf.read().strip())
        except ValueError:
            last_pos = 0
else:
    last_pos = 0

print("Log-Tracking gestartet. Neue Einträge werden an die Ausgabedatei angehängt.")

# Endlosschleife, die das Log überwacht, bis der Benutzer 'quit' eingibt
while running:
    with open(log_file, 'r', encoding='utf-8') as lf:
        lf.seek(last_pos)
        new_content = lf.read()
        new_pos = lf.tell()

    # Falls neue Inhalte vorhanden sind, diese an die Ausgabedatei anhängen
    if new_content:
        with open(output_file, 'a', encoding='utf-8') as of:
            of.write(new_content)
        print(f"Neue Einträge wurden an '{output_file}' angehängt.")
        last_pos = new_pos
        # Marker-Datei aktualisieren
        with open(marker_file, 'w', encoding='utf-8') as mf:
            mf.write(str(last_pos))

    time.sleep(.25)  # Überprüfe alle 1 Sekunde

print("Log-Tracking wurde beendet.")