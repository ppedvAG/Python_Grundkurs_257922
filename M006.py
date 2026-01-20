# List Comprehension
# Kurzschreibweise, zur Erstellung von Listen
from selectors import SelectSelector

zahlen = []
for x in range(10):
	zahlen.append(x)
print(zahlen)

zahlenLC = [x for x in range(10)]  # Schleife schreiben, danach x an den Anfang setzen
print(zahlenLC)

# if-Anweisungen
# Anzahl der Ausdrücke einschränken
zahlenDurch2 = []
for x in range(100):
	if x % 2 == 0:
		zahlenDurch2.append(x)
print(zahlenDurch2)

# Generell werden hier weniger Elemente in die Liste gespeichert, als die Schleife hergibt
zahlenDurch2LC = [x for x in range(100) if x % 2 == 0]
print(zahlenDurch2LC)

# Linke Seite verändern
# Anstatt Zahlen zu übernehmen, werden hier andere Typen übernommen
# -> Transformation
zahlenHoch2 = []
for x in range(1, 11):
	zahlenHoch2.append(f"{x}^2={x ** 2}")
print(zahlenHoch2)

zahlenHoch2LC = [f"{x}^2={x ** 2}" for x in range(1, 11)]
print(zahlenHoch2LC)

# Verschachtelte Schleifen
# Einfach aneinander hängen
zahlenMult = []
for x in range(1, 11):
	for y in range(1, 11):
		zahlenMult.append(x * y)
print(zahlenMult)

zahlenMultLC = [x for x in range(1, 11) for y in range(1, 11) for z in range(1, 11)]
print(zahlenMultLC)

# Ternary Operator
for x in range(1, 100):
	if x % 3 == 0 and x % 5 == 0:
		print("FizzBuzz")
	elif x % 3 == 0:
		print("Fizz")
	elif x % 5 == 0:
		print("Buzz")
	else:
		print(x)

print(["FizzBuzz" if x % 3 == 0 and x % 5 == 0 else \
	   "Fizz" if x % 3 == 0 else \
	   "Buzz" if x % 5 == 0 else \
	   x for x in range(1, 100)])