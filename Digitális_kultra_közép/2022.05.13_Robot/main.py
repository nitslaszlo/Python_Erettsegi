def IrányDarab(irány: str, parancs: str) -> int:
    db: int = 0
    for aktuális_irány in parancs:
        if aktuális_irány == irány:
            db += 1
    return db


def IrányStatKiír(irányok: str, parancs: str) -> None:
    for irány in irányok:
        print(f"{irány} betűk száma: {IrányDarab(irány, parancs)}")


def Egyszerüsít(parancs: str) -> str:
    deltaX: int = IrányDarab("K", parancs) - IrányDarab("N", parancs)
    deltaY: int = IrányDarab("E", parancs) - IrányDarab("D", parancs)

    # egyszerű: str = ""
    # if deltaX >= 0:
    #     for _ in range(deltaX):
    #         egyszerű += "K"
    # else:
    #     for _ in range(-deltaX):
    #         egyszerű += "N"

    # if deltaY >= 0:
    #     for _ in range(deltaY):
    #         egyszerű += "E"
    # else:
    #     for _ in range(-deltaY):
    #         egyszerű += "D"
    # return egyszerű

    irányX: str = "K" if deltaX > 0 else "N"
    irányY: str = "E" if deltaX > 0 else "D"

    return f"{irányX * abs(deltaX)}{irányY * abs(deltaY)}"


def main() -> None:
    print("Robot feladat")

    parancs: str = input("Kérem a robot parancsait: ")

    IrányStatKiír("EDKN", parancs)

    print(f"Egy legrövidebb út parancsszava: {Egyszerüsít(parancs)}")

    print("alma" * 3)


if __name__ == "__main__":
    main()
