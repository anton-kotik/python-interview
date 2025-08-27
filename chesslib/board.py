# -*- coding: utf-8 -*-
import re
from typing import Dict
from chesslib.figures import Pawn, Rook, Knight, Queen, Bishop, King

FILES = "abcdefgh"

class Board:
    def __init__(self) -> None:
        self.figures: Dict[str, Dict[int, object]] = {f: {} for f in FILES}
        self._setup_start_position()

    def _setup_start_position(self) -> None:
        self.figures["a"][1] = Rook(False)
        self.figures["b"][1] = Knight(False)
        self.figures["c"][1] = Bishop(False)
        self.figures["d"][1] = Queen(False)
        self.figures["e"][1] = King(False)
        self.figures["f"][1] = Bishop(False)
        self.figures["g"][1] = Knight(False)
        self.figures["h"][1] = Rook(False)

        self.figures["a"][8] = Rook(True)
        self.figures["b"][8] = Knight(True)
        self.figures["c"][8] = Bishop(True)
        self.figures["d"][8] = Queen(True)
        self.figures["e"][8] = King(True)
        self.figures["f"][8] = Bishop(True)
        self.figures["g"][8] = Knight(True)
        self.figures["h"][8] = Rook(True)

        for f in FILES:
            self.figures[f][2] = Pawn(False)
            self.figures[f][7] = Pawn(True)

    MOVE_RE = re.compile(r"^([a-h])([1-8])-([a-h])([1-8])$")

    def move(self, move_str: str) -> None:
        m = self.MOVE_RE.match(move_str)
        if not m:
            raise ValueError("Incorrect move")
        x_from, y_from_s, x_to, y_to_s = m.groups()
        y_from, y_to = int(y_from_s), int(y_to_s)

        if y_from in self.figures[x_from]:
            self.figures[x_to][y_to] = self.figures[x_from][y_from]
        self.figures[x_from].pop(y_from, None)

    def dump(self) -> None:
        for y in range(8, 0, -1):
            row = [str(y)]
            for x in FILES:
                fig = self.figures[x].get(y)
                row.append(str(fig) if fig else "-")
            print(" ".join(row))
        print("  a b c d e f g h")
