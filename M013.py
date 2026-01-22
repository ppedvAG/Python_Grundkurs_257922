# Unit Tests
# Testet Teile des Programms
# WICHTIG: Regelmäßig ausführen (täglich, wöchentlich)

from unittest import TestCase, main
from M013b import Rechner

# class RechnerTests(TestCase):
# 	def testeAddiere(self):
# 		# AAA-Prinzip: Arrange, Act, Assert
#
# 		# Arrange (Vorbereitungsphase)
# 		r = Rechner()
#
# 		# Act (Ausführung)
# 		summe = r.addiere(3, 4)
#
# 		# Assert (Auswerten)
# 		self.assertEqual(summe, 7, "Summe ist nicht 7!")
#
# 	def testeSubtrahiere(self):
# 		# AAA
# 		r = Rechner()
#
# 		diff = r.subtrahiere(8, 3)
#
# 		self.assertEqual(diff, 5, "Differenz ist nicht 5! (8 - 3  = 5)")

# Mit ChatGPT generiert
class TestRechner(TestCase):
	def test_addiere_positive_zahlen(self):
		# Arrange
		rechner = Rechner()
		x = 3
		y = 4

		# Act
		ergebnis = rechner.addiere(x, y)

		# Assert
		self.assertEqual(ergebnis, 7)

	def test_addiere_negative_zahlen(self):
		# Arrange
		rechner = Rechner()
		x = -2
		y = -5

		# Act
		ergebnis = rechner.addiere(x, y)

		# Assert
		self.assertEqual(ergebnis, -7)

	def test_addiere_mit_null(self):
		# Arrange
		rechner = Rechner()
		x = 0
		y = 5

		# Act
		ergebnis = rechner.addiere(x, y)

		# Assert
		self.assertEqual(ergebnis, 5)

	def test_subtrahiere_positive_zahlen(self):
		# Arrange
		rechner = Rechner()
		x = 10
		y = 3

		# Act
		ergebnis = rechner.subtrahiere(x, y)

		# Assert
		self.assertEqual(ergebnis, 7)

	def test_subtrahiere_negative_zahlen(self):
		# Arrange
		rechner = Rechner()
		x = -5
		y = -3

		# Act
		ergebnis = rechner.subtrahiere(x, y)

		# Assert
		self.assertEqual(ergebnis, -2)

	def test_subtrahiere_mit_null(self):
		# Arrange
		rechner = Rechner()
		x = 5
		y = 0

		# Act
		ergebnis = rechner.subtrahiere(x, y)

		# Assert
		self.assertEqual(ergebnis, 5)

if __name__ == "__main__":
	main()