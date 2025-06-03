# Gefahrenstufen fuer PLZ
plz_gefahrliste = {
    "10115": 3,
    "10243": 8,
    "10437": 2,
    "10555": 7,
    "10999": 9
}

# Buergerbewertungen nach PLZ
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
    bewertung_text = input("Wie sicher fühlen sie sich? (1 = unsicher ; 10 sehr sicher): ")
    if not ist_zahl(bewertung_text):
        print("Bitte zahl eingeben: ")
        return
    bewertung = int(bewertung_text):
        if 1 <= bewertung <= 10:
            buerger_bewertungen[plz].append(bewertung)
