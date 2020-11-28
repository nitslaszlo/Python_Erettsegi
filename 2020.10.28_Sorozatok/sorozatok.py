from megoldas import Megoldas


def main():
    m: Megoldas = Megoldas('lista.txt')
    print(f'2. feladat\nA listában {m.ismert_a_vetites_datuma_darab} db vetítési dátummal rendelkező epizód van.')
    print(f'3. feladat\nA listában lévő epizódok {m.megnezve_arany:.2%}-át látta.')
    print(f'4. feladat\nSorozatnézéssel {m.ido_nap} napot {m.ido_ora} órát és {m.ido_perc} percet töltött.')
    for e in m.nem_latta_meg(input('5. feladat\nAdjon meg egy dátumot! Dátum= ')):
        print(e)
    for e in m.adott_napon_vetitett(input('7. feladat\nAAdja meg a hét egy napját (például cs)! Nap= ')):
        print(e)
    # 8. feladat:
    m.write_stat('summa.txt')


if __name__ == "__main__":
    main()
