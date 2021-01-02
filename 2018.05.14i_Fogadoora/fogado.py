from Megoldás import Megoldás


def main() -> None:
    m: Megoldás = Megoldás('fogado.txt')

    print(f'2. feladat\nFoglalások száma: {m.foglalások_száma}\n')

    input_név: str = input('3. feladat\nAdjon meg egy nevet: ')
    időpontfoglalások_száma: int = m.időpontfoglalások_száma(input_név)
    if időpontfoglalások_száma != 0:
        print(f'{input_név} néven {időpontfoglalások_száma} időpontfoglalás van.\n')
    else:
        print('A megadott néven nincs időpontfoglalás.\n')

    input_időpont: str = input('4. feladat\nAdjon meg egy érvényes időpontot: (pl. 17:10): ')
    print(m.foglalt_tanárok(input_időpont))

    print(f'\n5. feladat\n{m.első_foglalás}\n')

    print(f'6. feladat\n{m.tanár_szabad("Barna Eszter")}\n')
    print(f'Barna Eszter legkorábban távozhat: {m.tanár_legkorábban_távozhat("Barna Eszter")}')


if __name__ == "__main__":
    main()
