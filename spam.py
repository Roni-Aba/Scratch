import time

# Pfad zur Ausgabedatei
output_file = "/Users/work/PycharmProjects/Visure/roni.txt"

print("Starte das Schreiben der Zahlen 1-100 in", output_file)
print("Drücke Strg+C, um das Skript zu beenden.")

try:
    condition = True
    for i in range(1, 100):
        with open(output_file, "a", encoding="utf-8") as f:
            f.write(f"{i}\n")
        # Warte 1 Sekunde, bevor der nächste Satz geschrieben wird
        time.sleep(.1)
except KeyboardInterrupt:
    print("Skript wurde manuell beendet.")