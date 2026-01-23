# List
# Effektiv ein Array, aber mit einer unbegrenzten Größe
# Hat einen Index
# Kann Typen mischen
# Kann Duplikate enthalten
l = [1, 2, 3, 4]  # Liste erstellen mit Standardwerten
l2 = list()

print(l)  # Stringrepräsentation ist die Liste selbst

# Index
print(l[0])
print(l[-1])
print(l[0:2])

# Funktionen

# append
# Element hinzufügen
l.append(10)
print(l)

# remove
# Sucht das Element und entfernt es (von links)
l.remove(1)
print(l)

# pop
# Entfernt einen Wert anhand eines Indizes
l.pop(2)
print(l)

# sort
# Sortiert die Liste
l.append(1)
print(l)

l.sort()
print(l)

l.sort(reverse=True)  # Absteigend sortieren
print(l)

# extend
# Nimmt eine zweite Liste, und fügt die Elemente in die erste Liste
l.append([1, 2, 3])  # Liste mit einer anderen Liste (unpraktisch)
print(l)

l.pop(-1)
l.extend([1, 2, 3])
print(l)

print(l + [1, 2 ,3])  # Listen können auch addiert werden (selber Effekt wie extend)

########################################################

# Tupel
# Ähnlich wie List, kann aber nicht verändert werden
# Wird generell für Ergebnisse (Rückgabewerte) verwendet
t = (1, 2, 3)
print(t)

print(type(t))

# Tupel über Umweg verändern
t = list(t)  # Konvertierung
t.append(4)
t = tuple(t)
print(t)

########################################################

# range
# Zahlengenerator von X bis Y
r = range(10)  # 0-9
print(r)  # WICHTIG: Range selbst ist nur ein Generator (kein Leistungsverbrauch)

print(list(r))  # Hier werden tatsächlich Daten erzeugt

print(list(range(0, 100, 5)))  # Range mit Schrittgröße

x = range(100_000_000)
print(x)

# y = list(x)  # Hier werden tatsächlich Daten erzeugt

########################################################

# set
# Einzigartige Liste (jedes Element muss einzigartig sein)
s = {1, 2, 3}
print(s)

s.add(4)
print(s)

s.add(4)  # Kein Effekt
print(s)

########################################################

# dict
# Ein Set, bei dem jeder Inhalt einen Schlüssel (= Namen) hat
d = {
	"Vorname": "Max",
	"Nachname": "Mustermann",
	"Alter": 33
}

print(d["Alter"])  # Hier ein Stringbasierter Index

d["Alter"] += 1  # Bestehenden Wert verändern

d["Adresse"] = "Zuhause"  # Achtung: Wenn der Wert bereits existiert, wird er überschrieben

print(d)

d.setdefault("Adresse", "Wien")  # Wird nur geschrieben, wenn der Wert noch nicht existiert

print(d.items())
print(d.keys())
print(d.values())

########################################################

# Konvertierung
# Umwandlung von Werten
# Syntax: Zieltyp(Wert)

z = 123.45
print(int(z))  # Wandelt den float zum int um

print(bool(z))  # Alles was nicht 0 ist, ist True

n = [1, 2, 3]
print(tuple(n))
print(set(n))