#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SCRIPT = BASE_DIR / "chess.py"
TESTS_DIR = BASE_DIR / "tests"

class TestChess(unittest.TestCase):
    def test_no_moves(self):
        self.run_file("001-no-moves.test")

    def test_simple_error(self):
        self.run_file("011-simple-error.test")

    def test_simple(self):
        self.run_file("012-simple-move.test")

    def test_color_rotation_correct(self):
        self.run_file("014-color-rotation-correct.test")

    def test_pawn_moves_one_square_vertically(self):
        self.run_file("021-pawn-moves-one-square-vertically.test")

    def test_pawn_can_move_two_squares_on_first_move(self):
        self.run_file("022-pawn-can-move-two-squares-on-first-move.test")

    def test_pawn_can_not_move_diagonally(self):
        self.run_file("023-pawn-can-not-move-diagonally.test")

    def test_pawn_captures_diagonally(self):
        self.run_file("024-pawn-captures-diagonally.test")

    def test_pawn_can_not_capture_vertically(self):
        self.run_file("025-pawn-can-not-capture-vertically.test")

    def test_pawn_can_not_move_farther_one_square(self):
        self.run_file("026-pawn-can-not-move-farther-one-square.test")

    def test_pawn_can_not_move_across_figure(self):
        self.run_file("027-pawn-can-not-move-across-figure.test")

    """
    Test file structure
    line 1: moves as arguments to chess.php
    line 2: 'correct' if all moves are correct, 'error' if there are incorrect moves
    Other lines: output of chess.php (final chess board) if all moves are correct
    """

    def run_file(self, filename: str):
        test_path = (TESTS_DIR / filename).resolve()
        self.assertTrue(test_path.exists(), f"Test file not found: {test_path}")

        lines = test_path.read_text(encoding="utf-8").splitlines()
        if not lines:
            self.fail(f"Test file is empty: {test_path}")

        moves_line = (lines[0].strip() if len(lines) >= 1 else "")
        moves_desc = moves_line or "(no moves)"

        is_correct = (len(lines) >= 2 and lines[1].strip() != "error")

        red = "\033[31m" if sys.stdout.isatty() else ""
        off = "\033[m" if sys.stdout.isatty() else ""

        args = moves_line.split() if moves_line else []
        cmd = [sys.executable, str(SCRIPT), *args]

        proc = subprocess.run(cmd, cwd=BASE_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if is_correct:
            self.assertEqual(
                0, proc.returncode,
                f"{red}Moves are correct, but chess.py thinks there is an error:\n{moves_desc}{off}\n"
                f"stdout:\n{proc.stdout}\n"
                f"stderr:\n{proc.stderr}\n"
            )
        else:
            self.assertNotEqual(
                0, proc.returncode,
                f"{red}Moves are invalid, but chess.py does not detect that:\n{moves_desc}{off}\n"
                f"stdout:\n{proc.stdout}\n"
                f"stderr:\n{proc.stderr}\n"
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
