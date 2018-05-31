#!/usr/bin/env python3

from beem.account import Account


def ListeResteemsSchreiben(nutzer_resteem):
    """Schreibt eine Liste der Resteems von Neuvorstellungen"""
    nutzer_resteem = list(nutzer_resteem)
    nutzer_resteem.sort()
    with open('./users/neuvorstellungen_resteems',
              encoding='utf-8',
              mode='w') as datei:
        for nutzer in nutzer_resteem:
            datei.write(nutzer + "\n")


def ListeKommentareSchreiben(nutzer_kommentare):
    """Schreibt eine Liste der Kommentare von Neuvorstellungen"""
    nutzer_kommentare = list(nutzer_kommentare)
    nutzer_kommentare.sort()
    with open('./users/neuvorstellungen_kommentare',
              encoding='utf-8',
              mode='w') as datei:
        for nutzer in nutzer_kommentare:
            datei.write(nutzer + "\n")


def main():
    a = Account('neuvorstellungen')
    # Resteems
    menge_nutzer_resteems = set()
    for nutzer in a.get_blog_account():
        menge_nutzer_resteems.add(nutzer[0])
    ListeResteemsSchreiben(menge_nutzer_resteems)
    # Kommentare
    menge_nutzer_kommentare = set()
    for op in a.history_reverse():
        if 'parent_author' in op and op['parent_author'] != 'neuvorstellungen':
            if op['parent_author'] != '':
                menge_nutzer_kommentare.add(op['parent_author'])
    ListeKommentareSchreiben(menge_nutzer_kommentare)


if __name__ == '__main__':
    main()
