# Vererbung
# Basisklassen definieren; diese Vererben ihre Inhalte (Funktionen, Felder) an die Unterklassen weiter
# Alle Klassen in Python erben von der object Klasse
# Diese vererbt sehr viele Funktionen (u.a. __init__, __str__)

# Lebewesen, Mensch
class Lebewesen:
	def __init__(self, alter):
		self.alter = alter

	def __str__(self):
		return f"Lebewesen: {self.alter}"

	def bewegen(self, distanz):
		print(f"Das Lebewesen bewegt sich um {distanz}m.")


class Mensch(Lebewesen):  # Vererbung anlegen (Oberklasse in Klammer)
	"""
	Fehlende Eigenschaften: name, sprechen
	"""
	def __init__(self, alter, name):
		super().__init__(alter)  # super(): Führt Code aus der Klasse direkt darüber aus
		self.name = name  # name wird nicht weitergegeben

	def sprechen(self, text):
		print(f"{self.name} sagt: {text}")

	def bewegen(self, distanz):
		"""
		Überschreibung

		Hier wird die bewegen Methode aus Lebewesen komplett ignoriert (Eigene Implementation pro Unterklasse)
		"""
		print(f"{self.name} bewegt sich um {distanz}m.")


# m hat alter und bewegen, obwohl diese garnicht definiert wurden
m = Mensch(33, "Max")
m.bewegen(10)
m.sprechen("Hallo")

l = Lebewesen(22)
# l.sprechen("Hallo")  # Nicht möglich

################################################################################

# __str__: Wandelt das Objekt in eine Stringrepräsentation um
print(m)  # <__main__.Mensch object at 0x000002BB9DF37CB0>
print(m)  # Nach Überschreibung: Lebewesen: 33

x = 123
print(x)

z = [1, 2, 3]
print(z)