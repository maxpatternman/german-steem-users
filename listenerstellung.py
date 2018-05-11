#!/usr/bin/env python3

import os

def listeAuslesen(listePfad):
    """Liest Nutzer aus einer Datei und gibt sie als Menge zurück"""
    mengeNutzer = set()
    with open(listePfad) as datei:
        for nutzer in datei:
            mengeNutzer.add(nutzer.rstrip())
    return mengeNutzer


def listenverzeichnisOeffnen(pfad):
    """Durchläuft alle Listen des Verzeichnisses unter 'pfad'"""
    mengeNutzer = set()
    for dateiname in os.listdir(pfad):
        users = listeAuslesen(pfad + '/' + dateiname)
        if users:
            mengeNutzer = mengeNutzer.union(users)
    return(mengeNutzer)


def finaleListeSchreiben(listeFinal):
    """Schreibt german-steem-users.txt aus der finalen Menge"""
    listeFinal = list(listeFinal)
    listeFinal.sort()
    with open('german-steem-users.txt', 'w') as datei:
        for nutzer in listeFinal:
            datei.write(nutzer + "\n")


def bericht(users_int, blacklist_int, usersFinal_int):
    """Gibt einen kleinen Bericht aus"""
    print('')
    print('Gesamt:', str(usersFinal_int),
          'von', str(users_int))
    print('Gefiltert:', str(users_int - usersFinal_int),
          'von', str(blacklist_int))


def main():
    verzeichnisseNutzer = ['users']
    verzeichnisseBlacklists = ['blacklists']
    # Nutzer
    for verzeichnis in verzeichnisseNutzer:
        users = listenverzeichnisOeffnen(verzeichnis)
    # Blacklist
    for verzeichnis in verzeichnisseBlacklists:
        blacklist = listenverzeichnisOeffnen(verzeichnis)
    # Entfernt Blacklist Nutzer
    usersFinal = users.difference(blacklist)
    # Finale Liste schreiben
    finaleListeSchreiben(usersFinal)
    # Ende und Bericht
    bericht(len(users), len(blacklist), len(usersFinal))


if __name__ == '__main__':
    main()
