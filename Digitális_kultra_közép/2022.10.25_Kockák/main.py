import random

anni_nyert_db: int = 0
panni_nyert_db: int = 0

def feldob(kockák_száma: int) -> list[int]:
    dobások: list[int] = []
    for _ in range(kockák_száma):
        dobások.append(random.randint(1, 6))
    return dobások


def dobások_összege(dobások: list[int]) -> int:
    összeg: int = 0
    for dobás in dobások:
        összeg += dobás
    return összeg


def nyertes_neve(pontszám: int) -> str:
    if pontszám < 10:
        return "Anni"
    else:
        return "Panni"

def nyertes_stat(pontszám: int) -> None:
    global anni_nyert_db
    global panni_nyert_db
    if pontszám < 10:
        anni_nyert_db += 1
    else:
        panni_nyert_db += 1

def kör_string(kockák_száma: int) -> str:
    dobás: list[int] = feldob(kockák_száma)
    dobás_összeg: int = dobások_összege(dobás)
    sor: str = f"Dobás: {dobás[0]}"
    for d in dobás[1:]:
        sor += f" + {d}"
    sor += f" = {dobás_összeg}\tNyert: {nyertes_neve(dobás_összeg)}"
    nyertes_stat(dobás_összeg)
    return sor


def köröket_ír(dobások_száma: int, kockák_száma: int) -> None:
    for _ in range(dobások_száma):
        print(kör_string(kockák_száma))


def main() -> None:
    # HF: Feladatok megoldása a fogyokúra szellemében
    # 1. feladat: Bekérés - dobások száma
    dobások_száma: int = int(input("Hány alkalommal legyen feldobás?"))

    köröket_ír(dobások_száma, 3)

    print(f"A játék során {anni_nyert_db} alkalommal Anni, {panni_nyert_db} alkalommal Panni nyert.")


if __name__ == "__main__":
    main()
