#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from chesslib.board import Board

def main(argv: list[str]) -> int:
    try:
        board = Board()
        for move in argv[1:]:
            board.move(move)
        board.dump()
        return 0
    except Exception as e:
        print(str(e))
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
