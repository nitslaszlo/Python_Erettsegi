from Megoldás import Megoldás


def main() -> None:
    # 1. feladat:
    m: Megoldás = Megoldás('ajto.txt')

    print(f'2. feladat\nAz első belépő: {m.első_belépő}\nAz utolsó kilépő: {m.utolsó_kilépő}\n')

    # 3. feladat:
    m.statisztikát_ír('athaladas.txt')

    print(f'4. feladat\nA végén a társalgóban voltak: {m.társalgóban_maradtak}\n')

    print(f'5. feladat\nPéldául {m.legtöbben_a_társalgóban.strftime("%H:%M")}-kor voltak legtöbben a társalgóban.\n')

    input_azon: str = input('6. feladat\nAdja meg a személy azonosítóját! ')

    print(f'7. feladat\n{m.mettől_meddig(input_azon)}')

    print(f'\n8. feladat\nA(z) {input_azon}. személy összesen {m.eltöltött_idő_perc(input_azon)} percet volt bent, a megfigyelés végén ', end='')
    print(f'{"a társalgóban volt." if m.társalgóban_maradt(input_azon) else "nem volt a társalgóban."}')


if __name__ == "__main__":
    main()
