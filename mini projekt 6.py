import random

runde = 1
bestOfFive = 0

while runde <= 5:  # Es sollen maximal 5 Runden gespielt werden
    print("\nRunde " + str(runde) + "\n")
    
    spieler = random.randint(1, 6)
    computer = random.randint(1, 6)
    
    print("Spieler: " + str(spieler))
    print("Computer: " + str(computer))
    
    # Wenn der Spieler eine 6 würfelt, bekommt er eine zusätzliche Zahl
    if spieler == 6:
        spieler += random.randint(1, 6)
        print("Spieler würfelt eine 6 und bekommt eine zusätzliche Zahl: " + str(spieler))
    
    # Wenn der Computer eine 6 würfelt, bekommt er eine zusätzliche Zahl
    if computer == 6:
        computer += random.randint(1, 6)
        print("Computer würfelt eine 6 und bekommt eine zusätzliche Zahl: " + str(computer))
    
    # Bestimmen des Siegers
    if computer > spieler:
        print("Computer gewinnt diese Runde")
        bestOfFive += 1
    elif computer < spieler:
        print("Spieler gewinnt diese Runde")
        bestOfFive += 1
    else:
        print("Unentschieden! Beide haben die gleiche Zahl geworfen.")
    
    runde += 1

# Ausgabe nach den 5 Runden
print("\nDas Spiel ist vorbei! Nach 5 Runden war der Stand:")
print("Computer-Siege: " + str(bestOfFive))
