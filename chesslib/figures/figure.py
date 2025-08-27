from dataclasses import dataclass

@dataclass(frozen=True)
class Figure:
    is_black: bool

    def __str__(self) -> str:
        raise NotImplementedError("Not implemented")
