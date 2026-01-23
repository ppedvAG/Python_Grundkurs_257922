# Funktionen
# Code wiederverwenden -> In Funktionen ablegen und diese Funktionen nach belieben ausführen
def halloWelt():
	print("Hallo Welt")

# Ab hier kann die Funktion verwenden werden
halloWelt()
halloWelt()
halloWelt()

# Funktionen mit Parametern (Daten)
def hallo(name):
	print(f"Hallo {name}!")

hallo("Jan")
hallo("Lukas")
hallo(123)
hallo([1, 2, 3])  # Parameter in Python können beliebige Daten empfangen (nicht immer optimal)

##########################################################

# Typempfehlungen
# User darauf hinweisen, welche Daten diese Funktion konsumieren soll
def hallo2(name: str):  # Generell gute Idee, eine Empfehlung zu machen
	print(f"Hallo2 {name}!")

hallo2("Jan")
hallo2("Lukas")
hallo2(123)
hallo2([1, 2, 3])  # Kein Zwang, Funktion läuft trotzdem ohne Probleme

# Wenn die korrekten Typen wirklich wichtig sind, kann ein Typvergleich per if gemacht werden
def hallo3(name: str):
	if type(name) == str:
		print(f"Hallo3 {name}!")
	else:
		print(f"name muss ein String sein! ({name})")
		# raise TypeError("name muss ein String sein!")  # Warum Absturz verursachen? Fortgeschrittenes Konzept, siehe M011

hallo3("Jan")
hallo3("Lukas")
hallo3(123)
hallo3([1, 2, 3])

##########################################################

# Rückgabewerte
# Funktionen können ein Ergebnis haben, dieses kann in weiterer Folge in eine Variable gespeichert werden
def addiere(x: int, y: int):
	return x + y

summe = addiere(3, 4)  # Ergebnis auffangen in einer Variable
print(summe)

print(addiere(3, 4))  # Ergebnis direkt weiterverarbeiten

def addiere2(x: int | float, y: int | float):  # Mehrere Empfehlungen pro Parameter
	return x + y

addiere2(3, 4)
addiere2(3.5, 4.5)
addiere2(3, 2.3)

def addiere3(x: int | float, y: int | float) -> int:  # Rückgabewerthinweis
	return int(x + y)
	print("Fertig")  # return muss das letzte Statement sein

##########################################################

# Default Parameter
# Standardwert für einen Parameter definieren
# Kann überschrieben werden, wenn notwendig
def addiere4(x, y = 0):
	return x + y

addiere4(2, 3)
addiere4(8)  # y = 0

# Praktisches Beispiel
# Funktionen "konfigurierbar" machen
# pandas.read_csv
# pandas.read_csv(filepath_or_buffer, *, sep=<no_default>, delimiter=None, header='infer', names=<no_default>, index_col=None, usecols=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=<no_default>, skip_blank_lines=True, parse_dates=None, infer_datetime_format=<no_default>, keep_date_col=<no_default>, date_parser=<no_default>, date_format=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, on_bad_lines='error', delim_whitespace=<no_default>, low_memory=True, memory_map=False, float_precision=None, storage_options=None, dtype_backend=<no_default>)
# Hier gibt der User nur die Parameter ein, die auch wirklich benötigt werden
# -> pandas.read_csv("Path", delimiter=";", thousands=",", decimal=".")

def printPerson(vorname: str = "", nachname: str = "", alter: int = 0, adresse: str = ""):
	print("...")

printPerson(vorname="Max", nachname="Mustermann")
printPerson(vorname="Max", alter=30)
printPerson(adresse="Zuhause")
printPerson()  # Nur die Parameter verwenden, die auch wirklich notwendig sind

##########################################################

# Arbitrary Arguments
# Beliebig viele Werte, bei einem Parameter eingeben
def addieren(*zahlen: int):
	summe = 0
	for x in zahlen:  # zahlen ist hier ein Tupel
		summe += x
	return summe

addieren(1, 2, 3, 4)
addieren(2, 3)
addieren(8)
addieren()

# Arbitrary Keyword Arguments
# Beliebig viele BENANNTE Werte, bei einem Parameter eingeben
# Jeder Wert hat einen Key
def printKurs(**tn):
	for key, value in tn.items():
		print(f"{key}: {value}")

printKurs(Trainer="Lukas", TN1="Jan")

##########################################################

# Unpacking Operator
# * oder ** Operator
# Zerlegt eine Collection in ihre Einzelteile

# print(addieren([1, 2, 3]))  # Nicht möglich
print(addieren(*[1, 2, 3], *[4, 5, 6]))

dict = {
	"Trainer": "Lukas",
	"TN1": "Jan"
}
# printKurs(dict)  # Nicht möglich
printKurs(**dict)

# Unpacking einer Liste in einzelne Variablen
a = 0
b = 0
c = 0
a, b, c = (1, 2, 3)