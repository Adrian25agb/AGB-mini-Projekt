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
        durchschnitt = sum(bewertung) / anzahl
    unsicherheitswert = (1 - durchschnitt / 10)
    bewertungsfaktor = min(anzahl / 10, 1)
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
            print("PLZ: " + str(plz) + " Bewertungen: " + str(bewertungen) + " Score: " + str(score) + " Einstufung: " + str(einstufung))
        else:
            print("PLZ: " + str(plz) + "Keine Bewertungen")
