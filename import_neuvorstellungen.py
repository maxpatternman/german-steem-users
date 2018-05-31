#!/usr/bin/env python3

from beem.account import Account


def ListeResteemsSchreiben(nutzer_resteem):
    """Schreibt german-steem-users.txt aus der finalen Menge"""
    nutzer_resteem = list(nutzer_resteem)
    nutzer_resteem.sort()
    with open('./users/neuvorstellung_resteems',
              encoding='utf-8',
              mode='w') as datei:
        for nutzer in nutzer_resteem:
            datei.write(nutzer + "\n")


def main():
    a = Account('neuvorstellungen')
    menge_nutzer_resteem = set()
    for nutzer in a.get_blog_account():
        menge_nutzer_resteem.add(nutzer[0])
    ListeResteemsSchreiben(menge_nutzer_resteem)


if __name__ == '__main__':
    main()
