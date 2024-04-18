import webbrowser
import AppOpener

import speech_recognition as sr

rec_vocale = sr.Recognizer()
mic = sr.Microphone()

run = True

def openInChrome(site):
    webbrowser.Chrome()
    webbrowser.open(site, new=2)

def openApp(string):
    AppOpener.open(string, match_closest= True)

with mic as src:
    rec_vocale.adjust_for_ambient_noise(src)  # Ajuster au bruit ambiant

    while run:
        try:
            audio = rec_vocale.listen(src)  # Ecoutez le microphone
            texte = rec_vocale.recognize_google(audio, language="fr-FR", with_confidence=0)  # Utiliser la reconnaissance vocale
            print("[RECONNAISSANCE DE PHRASE] -", texte)
            response = str.lower(texte)
            # ARRET
            if response in ['arrête-toi', 'stop', 'arrête']:
                run = False

            # YOUTUBE
            if response == "youtube":
                openInChrome("https://www.youtube.com")

            # GOOGLE
            if response == "google":
                openInChrome("https://www.google.com")

            # OPGG
            if response == "opgg":
                openInChrome("op.gg")

            # RECHERCHE
            if response.startswith("recherche"):
                string = response.replace("recherche", "")
                openInChrome(f"https://www.google.com/search?q={string}")

            # OUVERTURE APP
            if response.startswith("ouvre") or response.startswith("lance"):
                string = response.replace("ouvre", "").replace("lance","")
                openApp(string)


        except:
            print("[ERREUR]")
    print('Bye bye :)')
