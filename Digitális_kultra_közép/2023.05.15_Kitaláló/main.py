import random


def beolvas_szavak(állomány_neve: str) -> list[str]:
    szavak: list[str] = []
    with open(állomány_neve, "r", encoding="utf-8") as file:
        for szó in file.read().split(", "):
            szavak.append(szó.replace('"', ""))
    return szavak


def rejtett_szó_generátor(szavak: list[str]) -> str:
    utolsó_index: int = len(szavak) - 1
    vél_index: int = random.randint(0, utolsó_index)
    return szavak[vél_index]


def eredményt_kódol(rejtett_szó: str, tipp: str) -> str:
    eredmény: str = ""
    for i in range(0, len(rejtett_szó)):
        if rejtett_szó[i] == tipp[i]:
            eredmény += tipp[i]
        else:
            eredmény += "."
    return eredmény

def játék_vége(eredmény: str) -> bool:
    return eredmény.find(".") == -1


def játék_ciklus(rejtett_szó: str) -> None:
    tipp: str = ""
    tippek_száma: int = 0

    while tipp != "stop":
        tipp = input("Kérem a tippet: ")
        if tipp != "stop":
            tippek_száma += 1
            eredmény: str = eredményt_kódol(rejtett_szó, tipp)
            print(eredmény)
            if játék_vége(eredmény):
                tipp = "stop"
                print(f"{tippek_száma} tippeléssel sikerült kitalálni.")


def main() -> None:
    # hivatalos megoldás:
    # szavak: list[str] = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"]
    # választott megoldás
    szavak: list[str] = beolvas_szavak("szavak.txt")

    rejtett_szó: str = rejtett_szó_generátor(szavak)

    játék_ciklus(rejtett_szó)


if __name__ == "__main__":
    main()
