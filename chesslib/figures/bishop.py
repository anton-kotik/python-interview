from .figure import Figure

class Bishop(Figure):
    def __str__(self) -> str:
        return "♝" if self.is_black else "♗"
