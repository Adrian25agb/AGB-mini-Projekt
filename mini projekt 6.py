import random
spieler = random.randint(1,6)
computer = random.randint(1,6)
print("spieler: " + str(spieler))
print("computer: " + str(computer))
if computer > spieler:
    print("computer wins")
if computer < spieler:
    print("spieler wins")
    while computer == 6:
        computer = computer + random.randint(1,6)
if computer == spieler:
    print("gleiche zahl")
    spieler = random.randint(1,6)
    computer = random.randint(1,6)
    
        