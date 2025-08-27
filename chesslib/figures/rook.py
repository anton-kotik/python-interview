from .figure import Figure

class Rook(Figure):
    def __str__(self) -> str:
        return "♜" if self.is_black else "♖"
