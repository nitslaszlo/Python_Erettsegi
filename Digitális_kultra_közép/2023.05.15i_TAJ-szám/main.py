def ellenőrző_jegy(taj: str) -> str:
    if len(taj) != 9 or (not taj.isdigit()):
        raise SyntaxError(
            "A TAJ-szám nem 10 jegyű, vagy érvénytelen karaktereket tartalmaz!"
        )
    return taj[-1]


def szorzat_összeg(taj: str) -> int:
    if len(taj) != 9 or (not taj.isdigit()):
        raise SyntaxError(
            "A TAJ-szám nem 10 jegyű, vagy érvénytelen karaktereket tartalmaz!"
        )
    összeg: int = 0
    for i, e in enumerate(taj[:-1]):
        jegy: int = int(e)
        if i % 2 == 0:
            összeg += jegy * 3
        else:
            összeg += jegy * 7
    return összeg


def taj_ellenőrzés(taj: str) -> str:
    ell_jegy: int = int(ellenőrző_jegy(taj))
    szorzat_össz: int = szorzat_összeg(taj)
    return "Helyes" if ell_jegy == szorzat_össz % 10 else "Helytelen"


def main() -> None:
    try:
        taj: str = input("Kérem a TAJ-számot: ")
        # taj: str = "673457015"
        print(f"Az ellenőrző jegy: {ellenőrző_jegy(taj)}")
        print(f"A szorzatok összege: {szorzat_összeg(taj)}")
        print(f"{taj_ellenőrzés(taj)} a szám!")
    except SystemError as err:
        print(err)


if __name__ == "__main__":
    main()
