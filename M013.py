# Unit Tests
# Testet Teile des Programms
# WICHTIG: Regelmäßig ausführen (täglich, wöchentlich)

from unittest import TestCase, main
from M013b import Rechner

class RechnerTests(TestCase):
	def testeAddiere(self):
		# AAA-Prinzip: Arrange, Act, Assert

		# Arrange (Vorbereitungsphase)
		r = Rechner()

		# Act (Ausführung)
		summe = r.addiere(3, 4)

		# Assert (Auswerten)
		self.assertEqual(summe, 7, "Summe ist nicht 7!")

	def testeSubtrahiere(self):
		# AAA
		r = Rechner()

		diff = r.subtrahiere(8, 3)

		self.assertEqual(diff, 5, "Differenz ist nicht 5! (8 - 3  = 5)")

if __name__ == "__main__":
	main()