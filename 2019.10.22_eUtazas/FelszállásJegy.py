from Felszállás import Felszállás


class FelszállásJegy(Felszállás):
    _érvényes_alkalom: int

    def __init__(self, sor: str) -> None:
        super().__init__(sor)
        érvényes_alkalom: str = sor.split(' ')[4]
        self._érvényes_alkalom = int(érvényes_alkalom)

    @property
    def érvényes_felszállás(self) -> bool:
        return self._érvényes_alkalom > 0
