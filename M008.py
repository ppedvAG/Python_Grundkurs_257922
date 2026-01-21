# Module
# Effektiv andere Python Skripte
# Können mit import oder from import hier eingebunden werden

# import
# Importiert alle Member aus einem anderen Skript
# WICHTIG: Führt das gesamte Skript aus
import M007
M007.hallo("Max")

import M007 as M  # as <Name>: Alias vergeben (für kürzere Namen)
M.hallo("Max")

# from import
# Importiert nur bestimmte Member aus dem anderen Skript
# WICHTIG: Führt das gesamte Skript aus
from M007 import hallo, halloWelt, addieren
hallo("Max")
halloWelt()
addieren(1, 2, 3)  # Keine Prefixes notwendig

from M007 import *  # Alle Member hier einbinden

#########################################################

# Modul Suchpfade
# Die Pfade, die beim Import durchsucht werden, nach den entsprechenden Skripten
import sys

for p in sys.path:
	print(p)

# Eigenen Pfad hinzufügen
sys.path.append("C:\\Users\\lk3\\Desktop")
import xyz

#########################################################

# Externe Pakete installieren

# 2 Optionen:
# - Python Packages
# - Über das Terminal (pip)

import numpy
print(numpy.sin(3))

#########################################################

# Die Main-Methode
# Code der nur ausgeführt wird, wenn das Skript direkt gestartet wird (nicht beim import)

# __name__
# Immer verfügbar, Name des Skriptes selbst beim Import, __main__ bei direkter Ausführung

if __name__ == "__main__":
	print("...")

	import M008b.Test  # Skript aus einem Ordner importieren