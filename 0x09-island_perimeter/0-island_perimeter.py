#!:usr:bin:python3
def island_perimeter(g):
    """ calculate perimeter of island in grid

    Args:
    grid  (list of list of int):  the 2d grid represantation of island

    Returns:
       int: the perimeter of island
    """
    p = 0
    rows = len(g)
    cols = len(g[0]) if rows > 0 else 0

    for a in range(rows):
        for b in range(cols):
            if g[a][b] == 1:  # landcell
                # startwith 4 potential edges
                perimeter += 4
                # check topneihhbor
                if a > 0 and g[a - 1][b] == 1:
                    perimeter -= 2
                    # check leftneighbor
                    if b > 0 and g[a][b - 1] == 1:
                        perimeter -= 2
    return perimeter
