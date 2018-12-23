import time

from helper import *


def Minimax(grid, depth, start, alpha, beta):
    if Done(grid) or depth == 0 or (time.clock() - start) > 0.04:
        return heuristic(grid)

    ret = 2000000000
    emptycells = grid.getAvailableCells()
    newgrids = []
    for pos in emptycells:
        newgrid2 = grid.clone()
        newgrid4 = grid.clone()
        newgrid2.insertTile(pos, 2)
        newgrid4.insertTile(pos, 4)
        newgrids.append(newgrid2)
        newgrids.append(newgrid4)
    for newgrid in newgrids:
        ret = min(ret, Maxmini(grid=newgrid, depth=depth - 1, start=start, alpha=alpha, beta=beta))
        if ret <= alpha:
            break
        beta = min(ret, beta)
    return ret


def Maxmini(grid, depth, start, alpha, beta):
    if Done(grid) or depth == 0 or (time.clock() - start) > 0.04:
        return heuristic(grid)

    ret = -2000000000
    for newgrid in get_all_possible_grid(grid):
        ret = max(ret, Minimax(grid=newgrid, depth=depth - 1, start=start, alpha=alpha, beta=beta))
        if ret >= beta:
            break
        alpha = max(ret, alpha)
    return ret


def solve(grid):
    dep = 4
    st = time.clock()
    return Minimax(grid=grid, alpha=-2000000000, beta=2000000000, depth=dep, start=st)
