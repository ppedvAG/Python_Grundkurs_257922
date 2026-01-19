# if-Anweisung
# Prüft eine Bedingung

a = 5
b = 8

if a > b:
	print("a größer als b")

# elif
# if mit Bedingung
# Muss immer mit if oder elif kombiniert werden
if a > b:
	print("a größer als b")
elif a == b:
	print("a gleich b")

# else
# Sonst
# Kommt immer nach if oder elif
if a > b:
	print("a größer als b")
elif a != b:
	print("a gleich b")
else:  # a < b
	print("a ist kleiner als b")

# Logische Operatoren
if a > b and a < 10:
	print("...")

if a > b & a < 10:  # kein &&
	print("...")

if a > b or a < 10:
	print("...")

if a > b | a < 10:  # kein ||
	print("...")

if not a > b:
	print("...")

if ~(a > b):  # statt ! -> ~
	print("...")

# in
# Prüft, ob ein Wert innerhalb einer Liste ist
l = [1, 2, 3, 4]
if 3 in l:
	print("l enthält die Zahl 3")

if 3 not in l:
	print("l enthält die Zahl 3")

# Ternary Operator
# Kurzschreibweise für if/elif/else Konstrukte
if a > b:
	print("a größer als b")
elif a != b:
	print("a gleich b")
else:  # a < b
	print("a ist kleiner als b")

print("a größer als b") if a > b else (
	print("a gleich b")) if a == b else (
	print("a ist kleiner als b"))

print("a größer als b" if a > b else "a gleich b" if a == b else "a ist kleiner als b")