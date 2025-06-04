plz_gefahrliste = {
    "10115": 3,
    "10243": 8,
    "10437": 2,
    "10555": 7,
    "10999": 9
}

buerger_bewertungen = {
    "10115": [],
    "10243": [],
    "10437": [],
    "10555": [],
    "10999": []
}

def ist_zahl(text):
    return text.isdigit()

def buerger_bewertung_eingeben():
    plz = input("PLZ eingeben: ")
    if plz not in buerger_bewertungen:
        print("Unbekannte Postleitzahl.")
        return
    bewertung_text = input("Wie sicher fühlen Sie sich? (1 = unsicher ; 10 = sehr sicher): ")
    if not ist_zahl(bewertung_text):
        print("Bitte eine Zahl eingeben.")
        return
    bewertung = int(bewertung_text)
    if 1 <= bewertung <= 10:
        buerger_bewertungen[plz].append(bewertung)
        print("Danke für Ihre Bewertung!")
    else:
        print("Die Bewertung muss zwischen 1 und 10 liegen.")

def berechne_gefahrscore(plz):
    bewertung = buerger_bewertungen[plz]
    anzahl = len(bewertung)
    if anzahl == 0:
        durchschnitt = 5  # neutraler Mittelwert
    else:
        durchschnitt = sum(bewertung) / anzahl.                      #sum von chatgpt  
    unsicherheitswert = (1 - durchschnitt / 10)
    bewertungsfaktor = min(anzahl / 10, 1)                           #chatgpt
    score = unsicherheitswert * (0.9 + 0.1 * (1 - bewertungsfaktor))
    return round(score, 2)

def neue_einstufung(score):
    if score > 0.7:
        return "Hohe Gefahr"
    elif score > 0.4:
        return "Mittlere Gefahr"
    else:
        return "Geringe Gefahr"

def alle_auswerten():
    for plz in buerger_bewertungen:
        bewertungen = buerger_bewertungen[plz]
        if len(bewertungen) > 0:
            score = berechne_gefahrscore(plz)
            einstufung = neue_einstufung(score)
            print("PLZ: " + str(plz) + " Bewertungen: " + str(bewertungen) + 
                  " Score: " + str(score) + " Einstufung: " + str(einstufung))
        else:
            print("PLZ: " + str(plz) + " Keine Bewertungen")

# Wiederholungsschleife
auswahl = 0
while auswahl != 3:
    print("\nWas möchten Sie tun?")
    print("1 - Neue Bewertung eingeben")
    print("2 - Alle Auswertungen anzeigen")
    print("3 - Programm beenden")

    auswahl = input("Ihre Auswahl: ")

    if auswahl == "1":
        buerger_bewertung_eingeben()
    elif auswahl == "2":
        alle_auswerten()
    elif auswahl == "3":
        print("Programm beendet. Auf Wiedersehen!")
        break                                          #internet https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3-de
    else:
        print("Ungültige Eingabe. Bitte 1, 2 oder 3 wählen.")
