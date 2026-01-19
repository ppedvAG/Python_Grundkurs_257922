# Kommentar
# Raute am Anfang der Zeile; alles danach wird auskommentiert
print("Hello World")  # Kommentar am Ende einer Zeile

# Variablen
# Variablen haben per Definition keinen Typen -> der Inhalt bestimmt den Typen der Variable
# Eine Variable kann beliebige Werte enthalten
x = 5
print(x)

# int
# Ganze Zahl
# Kann beliebig große/kleine Zahlen enthalten
zahl = 218571923031824247594230147592035894021358932385876

# float
# Kommazahl
# Kann beliebig große/kleine Zahlen enthalten
komma = 128947124214912874912745913532678.31895712947132685971239654124812935648

# string
# Text
# Kann mit einzelnen Hochkomma oder doppelten Hochkomma definiert werden
text = "Hallo Welt"
text2 = 'Hallo Welt'

# bool
# Wahr-/Falschwert
f = False
t = True

# complex
# Komplexe Zahlen
c = 5 + 12j  # j -> mathematisches i

######################################################################

# Index
# Stellen von einer Liste angreifen
print(text[0])  # H

print(text[-1])  # t

print(text[0:5])  # Hallo (wichtig: Obergrenze exkludiert)

print(text[:5])  # Anfang bis 5
print(text[3:])  # 3 bis Ende

# count
# Zählt, wie oft ein Zeichen im String vorkommt
print(text.count("H"))  # 1

# lower, upper
# alles klein, ALLES GROß
print(text.lower())
print(text.upper())

# islower, isupper
# Prüft, ob der Text komplett lowercase oder UPPERCASE ist
# Wird oft mit dem Index kombiniert
print(text.islower())
print(text[0].islower())

# capitalize, title
# Der erste Buchstabe groß, alle Anfangsbuchstaben groß
print(text.capitalize())
print(text.title())

# len
# Gibt die Länge von einem beliebigen Listentypen zurück
print(len(text))

######################################################################

# Arithmetik
z1 = 5
z2 = 8

print(z1 + z2)  # Berechnet die Summe, aber verändert die Zahlen nicht
z1 += z2  # Addiert z2 auf z1 auf (13)

print(z1)

# Modulo
# Rest einer Division
print(z1 % z2)

# Potenz
print(z1 ** z2)  # 13^8

# Ganzzahldivision
print(8 / 5)  # 1.6

print(8 // 5)  # Schneidet die Kommastellen ab (1)

# Arithmetik mit Strings
hallo = "Hallo"
welt = "Welt"

print(hallo + welt)
hallo += " Welt"

print(hallo)

# Multiplikation
print(hallo * 10)  # Fehleranfällig