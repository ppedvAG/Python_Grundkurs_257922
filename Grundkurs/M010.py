# Klassen und Objekte
# Klassen stellen den Aufbau dar
# Objekte sind konkrete Instanzen, die auch Werte bekommen
# Klassen enthalten keine konkreten Werte (nur Felder, die im Anschluss Werte bekommen)
# Wenn die Objekte erzeugt werden, werden diese mit konkreten Werten befüllt (verschiedene Werte pro Objekt)
from io import TextIOWrapper

# Datentypen
# int: ganze Zahl
# float: Kommazahl
# str: Zeichenfolge
# bool: True/False
# Person: ? (komplex)

# Unterscheidung Datenklassen und Funktionsklassen
# Datenklassen: Halten Daten, haben generell fast ausschließlich Felder und kaum/keine Funktionen
# Funktionsklassen: Haben Funktionen, speichern generell kaum/keine Daten, machen etwas bestimmtes

# person = ["Max", "Mustermann", 33, "Zuhause"]  # Nicht Aussagekräftig
# Eigene Klasse muss her

class Person:
	def __init__(self):
		"""
		Die __init__ Funktion ist der Startcode des Objektes

		Wenn das Objekt erstellt wird, wird diese Funktion ausgeführt

		Hier werden die Felder (Variablen) erzeugt
		"""
		self.vorname = ""
		self.nachname = ""
		self.alter = 0
		self.adresse = ""

	def sprechen(self, text):
		print(f"{self.vorname} sagt: {text}")

p = Person()  # Objekt erzeugen mit <Klassenname>() -> Instanz
# Hier können jetzt konkrete Werte in das Objekt geschrieben werden
p.vorname = "Max"
p.nachname = "Mustermann"
p.alter = 30
p.adresse = "Zuhause"
p.sprechen("Hallo")  # Durch p.sprechen weiß die Funktion, auf welches Objekt wir uns beziehen (für self.vorname)

personen = [Person(), Person(), Person(), ...]  # Realität
# print(personen)

#####################################################################

# Verbesserung Person Klasse
class PersonBesser:
	def __init__(self, vorname = "", nachname = "", alter = 0, adresse = ""):
		"""
		Hier werden konkrete Startwerte verlangt

		Jeder dieser Parameter kann auch optional sein, wenn diese Werte nicht konkret benötigt werden
		:param vorname:
		:param nachname:
		:param alter:
		:param adresse:
		"""
		self.vorname = vorname
		self.nachname = nachname
		self.alter = alter
		self.adresse = adresse

	def sprechen(self, text):
		print(f"{self.vorname} sagt: {text}")

pb = PersonBesser("Max", "Mustermann", 30, "Zuhause")
pb.sprechen("Hallo")

# Typen
print(type(pb))  # Typ einer Variable holen

if type(pb) == PersonBesser:
	print("pb ist eine PersonBesser")

if pb is PersonBesser:
	print("pb ist eine PersonBesser")