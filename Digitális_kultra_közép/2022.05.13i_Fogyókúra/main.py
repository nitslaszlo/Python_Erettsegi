def tömeget_bekér(hetek_száma: int) -> list[float]:
    tömegek: list[float] = []
    for i in range(0, hetek_száma):
        tömegek.append(float(input(f"{i + 1}. héten=")))
    return tömegek

def cél_elérve(tömegek: list[float], cél: float) -> int:
    # ha a visszatérési érték 0, akkor a célt nem érte el
    # for i in range(0, len(tömegek)):
    #     if tömegek[i] < cél:
    #         return i + 1
    for i, súly in enumerate(tömegek):
        if súly < cél:
            return i + 1
    return 0

def cél_elérve_output(tömegek: list[float], cél: float) -> None:
    cél_hét: int = cél_elérve(tömegek, cél)
    if cél_hét == 0:
        print("Sajnos Mari néni nem érte el a célját.")
    else:
        print(f"Mari néni a(z) {cél_hét}. héten érte el a célt.")

def súlyos_hetek_száma(tömegek: list[float]) -> int:
    hetek_száma: int = 0
    előző_hét_tömege: float = tömegek[0]
    for aktSúly in tömegek[1:]:
        if aktSúly > előző_hét_tömege:
            hetek_száma += 1
        előző_hét_tömege = aktSúly
    return hetek_száma

def súlyos_hetek_száma2(tömegek: list[float]) -> int:
    hetek_száma: int = 0
    for i in range(1, len(tömegek)):
        if tömegek[i] > tömegek[i - 1]:
            hetek_száma += 1
    return hetek_száma

def main() -> None:
    # 1. feladat:
    hetek_száma: int = int(input("Hetek száma="))
    cél_testtömeg: float = float(input("Elérni kívánt tettömeg (kg)="))
    # 2. feladat:
    tömegek: list[float] = tömeget_bekér(hetek_száma)
    # 3. feladat:
    cél_elérve_output(tömegek, cél_testtömeg)
    # 4. feladar:
    print(f"A tömege {súlyos_hetek_száma(tömegek)} esetben nőtt az egyik hétről a másikra.")
    print(f"A tömege {súlyos_hetek_száma2(tömegek)} esetben nőtt az egyik hétről a másikra.")



if __name__ == "__main__":
    main()
