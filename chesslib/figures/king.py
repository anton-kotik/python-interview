from .figure import Figure

class King(Figure):
    def __str__(self) -> str:
        return "♚" if self.is_black else "♔"
