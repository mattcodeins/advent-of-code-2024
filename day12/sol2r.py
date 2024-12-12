from utils import *

inp = readlines('day12/input.txt')
grid = M(inp)

def fill(plot, crop, seen=set()):
    if plot in seen:
        return set(), seen
    seen.add(plot)
    region = {plot}
    for nextplot in plot.steps():
        if grid[nextplot] == crop:
            r, seen = fill(nextplot, crop, seen)
            region |= r
    return region, seen

regions = []
seen = set()
for i, v in grid:
    if i in seen:
        continue
    region, seen = fill(i,v)
    regions.append(region)

def check_side(region, plot, d, is_last_side, sides):
    is_side = plot + d not in region
    if is_side and not is_last_side:
        return is_side, sides+1
    return is_side, sides

def count_sides(region, row, directions):
    sides = 0
    for d in directions:
        is_side = False
        for plot in row:
            if plot in region:
                is_side, sides = check_side(region, plot, d, is_side, sides)
            else:
                is_side = False
    return sides

cost = 0
for region in regions:
    sides = 0
    istart, iend = min([i[0] for i in region]), max([i[0] for i in region])+1
    jstart, jend = min([i[1] for i in region]), max([i[1] for i in region])+1

    for i in range(istart, iend):
       sides += count_sides(region, [V(i,j) for j in range(jstart, jend)], [V(1,0),V(-1,0)])

    for j in range(jstart, jend):
       sides += count_sides(region, [V(i,j) for i in range(istart, iend)], [V(0,1),V(0,-1)])

    cost += sides*len(region)

print(cost)