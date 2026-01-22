# Fehlerbehandlung

# try-except
# Code ausführen, welcher abstürzen könnte, und die Abstürze verhinden
# Im try-Block kommt der Code hinein
# Im catch-Block können wir Fehlerbehandlungscode implementieren

try:
	x = int(input("Gib eine Zahl ein: "))
# Hier wird der Code definiert, bei einem Fehlerfall
except ValueError as e:  # ValueError, fängt Konvertierungsfehler
	print("Keine Zahl eingegeben")

	# Traceback: Nachverfolgung von dem Fehler (Genaue Schritte und Codezeilen)
	import traceback
	for x in traceback.format_exception(e):
		print(x)
except:  # Generische Except-Klausel, fängt alle Fehler
	print("Anderer Fehler")
else:  # else: Wird nur ausgeführt, wenn try ohne Fehler durchgelaufen ist
	print("Keine Fehler")
finally:  # finally: Wird immer ausgeführt (egal ob Fehler oder nicht)
	print("Ende des Blocks")

print("Ende des Programms")

########################################################################

# raise
# Fehler verursachen (Absturz)

# Warum?
# Manchmal können Fehler nicht vorhergesehen werden -> Absturz verursachen
# Wenn wir statt raise z.B. ein print verwenden, kann ein anderer User, der diesen Code verwendet,
# nicht frei entscheiden, wie die Fehlerbehandlung passieren soll
# print schreibt immer nur in die Konsole, aber der User möchte in vielleicht in ein Log schreiben (was mit print nicht möglich ist)
def eineMethode():
	raise SystemError("Das ist ein Beispielsfehler")  # Fehlermeldung eingeben

eineMethode()
try:
	eineMethode()
except SystemError as e:
	import traceback
	with open("Log.txt", "w") as f:
		f.writelines(traceback.format_exception(e))