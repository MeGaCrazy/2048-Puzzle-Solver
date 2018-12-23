def get_new_grid(grid, dir):
    ret = grid.clone()
    ret.move(dir)
    return ret


def get_all_possible_grid(grid):
    grids = []
    for move in grid.getAvailableMoves():
        grids.append(get_new_grid(grid, move))

    return grids


def Done(grid):
    return not grid.canMove()


def heuristic(grid):
    if Done(grid):
        return -2000000000

    evaluate = [
        [[3, 2, 1, 0], [2, 1, 0, -1], [1, 0, -1, -2], [0, -1, -2, -3]],
        [[0, 1, 2, 3], [-1, 0, 1, 2], [-2, -1, 0, 1], [-3, -2, -1, -0]],
        [[0, -1, -2, -3], [1, 0, -1, -2], [2, 1, 0, -1], [3, 2, 1, 0]],
        [[-3, -2, -1, 0], [-2, -1, 0, 1], [-1, 0, 1, 2], [0, 1, 2, 3]]
    ]

    ret = [0, 0, 0, 0]

    for i in range(4):
        for x in range(4):
            for y in range(4):
                ret[i] += evaluate[i][x][y] * grid.map[x][y]

    return max(ret)
