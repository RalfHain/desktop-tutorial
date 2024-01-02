import math

# Sieb des Eratosthenes.
# Einmal ermittelte Primzahlen werden gespeichert und
# werden beim nächsten Durchlauf zur Optimierung benutzt:
# e = Eratosthenes()
# e.Sieb(10).Ausgabe()
# # Pause oder andere Aufgaben.
# e.Sieb(100).Ausgabe()  # benutzt das Ergebis aus .Sieb(10)
class Eratosthenes:
    def __init__(self):
        self.primes = []
        self.vz_vorrunde = 2 # vorgegebene Zahl

    def Sieb(self, vz: int) -> None :  # vorgegebene Zahl

        noprimes = [True for n in range(vz + 1)]
        # TODO: Speicheroptimierung fehlt noch

        # Vorrunde: primes aus dem letzten Durchlauf verwenden.
        # (Laufzeitoptimierung)
        for i in self.primes:
            for j in range(i * 2, vz, i):
                noprimes[j] = False  # "Markiert"

        # Hauptrunde:
        for i in range(self.vz_vorrunde, math.floor(math.sqrt(vz)) + 1):
            for j in range(i * 2, vz, i):
                noprimes[j] = False  # "Markiert"

        # Primes ermitteln und in Membervariablen abspeichern.
        # Aber nur jene aus der neuen Hauptrunde.
        for x in range(self.vz_vorrunde, vz):
            if noprimes[x] == True:
                self.primes.append(x)
        self.vz_vorrunde = vz
        return self

    def Ausgabe(self):
        print(self.primes) # optimieren
        return

e = Eratosthenes()
e.Sieb(10).Ausgabe()
e.Sieb(100).Ausgabe()
e.Sieb(120).Ausgabe()
