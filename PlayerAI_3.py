from BaseAI_3 import BaseAI
# from Minimax import *
from alpha_beta_bruning import *
from helper import *
class PlayerAI(BaseAI):
    def getMove(self, grid):
        moves = grid.getAvailableMoves()
        Bestans = -2000000000
        Dir = -1
        for move in moves:
            new_grid = get_new_grid(grid=grid, dir=move)
            ret = solve(new_grid)
            if ret >= Bestans:
                Bestans = ret
                Dir = move
        return Dir
