from Megoldás import Megoldás


def main():
    m: Megoldás = Megoldás('lista.txt')
    print(f'2. feladat\nA listában {m.ismert_a_vetítés_dátuma_darab} db vetítési dátummal rendelkező epizód van.')
    print(f'3. feladat\nA listában lévő epizódok {m.megnézve_arány:.2%}-át látta.')
    print(f'4. feladat\nSorozatnézéssel {m.idő_nap} napot {m.idő_óra} órát és {m.idő_perc} percet töltött.')
    for e in m.nem_látta_még(input('5. feladat\nAdjon meg egy dátumot! Dátum= ')):
        print(e)
    for e in m.adott_napon_vetített(input('7. feladat\nAdja meg a hét egy napját (például cs)! Nap= ')):
        print(e)
    # 8. feladat:
    m.stat_ír('summa.txt')


if __name__ == "__main__":
    main()
