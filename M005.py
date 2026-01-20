# while-Schleife
# Schleife, die solange ausgeführt wird, wie eine bestimmte Bedingung gegeben ist

a = 0
b = 10
while a < b:
	print("a ist kleiner als b")
	a += 1  # kein ++ in Python

print("Nach der Schleife")

# Endlosschleife
while True:  # while 1:
	print("Endlos")
	break

# break und continue

# break
# Springe bei Ausführung von break aus der Schleife heraus
# Break wird immer mit einer if-Anweisung kombiniert
a = 0
b = 10
while a < b:
	print("a ist kleiner als b")
	a += 1
	if a == 5:
		break

# Bis-Schleife
a = 0
max = 20
while True:
	print("a ist kleiner als b")
	a += 1
	if a == max:
		break

# continue
# Überspringt den Code, nach dem Keyword selbst
# Springt an den Schleifenkopf zurück
# Continue wird immer mit einer if-Anweisung kombiniert

# Codedesign: Fehler zuerst abhandeln, danach Erfolg
# while True:
# 	if Fehleranweisung:
# 		...
# 		continue
#
# 	if Fehleranweisung 2:
# 		...
# 		continue
#
# 	...
#
# 	Erfolgscode

a = 0
b = 10
while a < b:
	a += 1
	if a % 3 == 0:
		continue  # Überspringt 3, 6, 9
	print("a: " + str(a))

# else
# Führt Code nur dann aus, wenn die Schleife ohne break vollständig fertig gelaufen ist
a = 0
b = 10
while a < b:
	print("a: " + str(a))
	a += 1
	if a == 5:
		break
else:
	print("Schleife ohne break fertig")

####################################################################

# for-Schleife
# Schleife, welche immer über eine Liste iteriert
# break, continue und else funktioniert hier identisch wie bei while
l = [8, 3, 1, 2, 1, 4, 9, 6]
for x in l:  # Die Laufvariable x enthält hier immer das jetztige Element
	print(x)

# Gleiches Beispiel mit while-Schleife
z = 0
while z < len(l):  # Umständlich und Fehleranfällig
	print(l[z])
	z += 1

# for-Schleife in Kombination mit Range
for x in range(10):  # for (int i = 0; i < 10; i++)
	print(x)

# Verschachtelte Schleife
# Schleife innerhalb einer anderen Schleife
# Wird hauptsächlich verwendet, um Tabellen zu iterieren
# -> Äußere Schleife für die Zeilen, innere Schleife für die einzelnen Werte (Spalten)
t = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix (3x3)
for row in t:  # Zeilen iterieren
	print(row)

for row in t:  # Zeilen iterieren
	for col in row:  # Werte iterieren
		print(col)

####################################################################

# Formatted String (fstring)
# Code in Strings einbetten
# f vor dem String, { } innerhalb des Strings verwenden
zahl = 21
print("Die Zahl ist: " + str(zahl))
print(f"Die Zahl ist: {zahl}")

for i in range(1, 11):
	print("Die Zahl ist: " + str(i))
	print("Die Zahl^2 ist: " + str(i ** 2))
	print(str(i) + "^2=" + str(i ** 2))

for i in range(1, 11):
	print(f"Die Zahl ist: {i}")
	print(f"Die Zahl^2 ist: {i ** 2}")
	print(f"{i}^2={i ** 2}")