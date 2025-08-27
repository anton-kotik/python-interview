from .figure import Figure

class Pawn(Figure):
    def __str__(self) -> str:
        return "♟" if self.is_black else "♙"
