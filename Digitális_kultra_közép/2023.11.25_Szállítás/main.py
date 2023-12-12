def beolvas_tárgyak_súlyát(állomány_neve: str) -> list[int]:
    tárgyak: list[int] = []
    with open(állomány_neve, "r", encoding="utf-8") as file:
        for súly in file.read().split(", "):
            tárgyak.append(int(súly))
    return tárgyak


def tárgyak_össztömege(tárgyak: list[int]) -> int:
    return sum(tárgyak)


def tárgyakat_dobozol(tárgyak: list[int]) -> list[int]:
    dobozok: list[int] = [tárgyak[0]]  # első tárgy dobozolása
    doboz_index: int = 0
    for tárgy in tárgyak[1:]:
        if dobozok[doboz_index] + tárgy > 20:  # ha nem fér bele a köv.
            doboz_index += 1
            dobozok.append(tárgy)
        else:
            dobozok[doboz_index] += tárgy  # ha még bele fér
    return dobozok


def main() -> None:
    # tárgyak: list[int] = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]
    tárgyak: list[int] = beolvas_tárgyak_súlyát("tomeg.txt")

    print(f"2. feladat\nA tárgyak tömegének összege: {tárgyak_össztömege(tárgyak)} kg")

    dobozok: list[int] = tárgyakat_dobozol(tárgyak)
    print("\n3. feladat:\nA dobozok tartalmának tömege (kg): ", end="")
    print(*dobozok, sep=" ")

    print(f"A szükséges dobozok száma: {len(dobozok)}")


if __name__ == "__main__":
    main()
