from Megoldás import Megoldás


def main() -> None:
    m: Megoldás = Megoldás('autok.txt')

    print(f'2. feladat\n{m.utolsó_kivitel.nap}. nap rendszám: {m.utolsó_kivitel.rendszám}')


if __name__ == "__main__":
    main()
