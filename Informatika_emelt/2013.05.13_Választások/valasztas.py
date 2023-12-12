from Megoldas import Megoldas


def main() -> None:
    m: Megoldas = Megoldas('szavazatok.txt')
    print(f'2. feladat:\nA helyhatósági választáson {m.jelöltek_száma} képviselőjelölt indult.')

    print('\n3. feladat:')
    képviselő_neve: str = input('Adja meg a képviselő nevét! ')
    print(m.képviselő_keresése(képviselő_neve))

    print(f'\n4. feladat:\nA választáson {m.szavazatok_száma} állampolgár, a jogosultak {m.szavazott_százalék}-a vett részt.')

    print(f'\n5. feladat:\n{m.szavazat_stat}')

    print(f'\n6. feladat\n{m.győztes_képviselők}')

    # 7. feladat:
    m.állományt_ír('kepviselok.txt')


if __name__ == "__main__":
    main()
