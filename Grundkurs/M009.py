# Input
# Präsentiert dem User einen Text, wartet dann auf eine Usereingabe
# name = input("Gib deinen Namen ein: ")
# print(f"Hallo {name}")
#
# x = input("Gib eine Zahl ein: ")
# y = input("Gib eine Zahl ein: ")
# # print(x + y)
# print(int(x) + int(y))

################################################

# open
# Mit externen Resourcen interagieren (hier Dateien)

file = open("Output.txt", "w")
file.write("Hallo")  # Der Inhalt wird nur in einen Buffer geschrieben
file.flush()  # Buffer niederschreiben
file.close()  # WICHTIG: Streams sollten immer geschlossen werden

file2 = open("Output.txt", "r")
for line in file2:
	print(line)
file2.close()

################################################

# Das with Statement
# Schließt das File am Ende vom Block automatisch
# Sollte immer verwendet werden
with open("Output.txt", "w") as f:
	f.write("With Hallo")
# Automatisch schließen

################################################

# Escape-Sequenzen
# Undruckbare Zeichen in den String einbetten
# \n: Zeilenumbruch
# \t: Tabulator
# \\: Einzelner Backslash
# https://learn.microsoft.com/de-de/cpp/c-language/escape-sequences?view=msvc-170

# Raw String
# String, welcher Escape Sequenzen ignoriert
# Besonders nützlich bei Windows-Pfaden
pfad = "C:\\Users\\lk3\\source\\repos\\Python_Grundkurs_2026_01_19\\.venv\\Scripts\\python.exe"
pfadR = r"C:\Users\lk3\source\repos\Python_Grundkurs_2026_01_19\.venv\Scripts\python.exe"

################################################

# os.path
# Bibliothek zum Arbeiten mit Pfaden
# os.path.exists: Existiert ein File/Directory?
# os.path.join: Pfade zusammenbauen (Betriebssystemunabhängig)
import os.path

ordner = "Folder"
datei = "Output.txt"

p = ordner + "\\" + datei  # Funktioniert nur auf Windows Systemen
p = os.path.join(ordner, datei)  # Funktioniert auf Windows und Linux Systemen