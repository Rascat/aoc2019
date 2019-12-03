

def update_path(grid, pos, label):
    if pos in grid:
        mark = grid[pos]
        if mark == label:
            pass
        else:
            grid.update({pos: 'X'})
            print('crossing at ({}, {})'.format(pos[0], pos[1]))
    else:
        grid.update({pos: label})


def move(instructions, grid, label):
    pos = (0,0)
    
    for i in instructions:
        direction = i[0:1]
        length = int(i[1:])

        if direction == 'U':
            for s in range(length):
                x = pos[0]
                y = pos[1]
                y += 1
                pos = (x, y)
                update_path(grid, pos, label)
        elif direction == 'R':
            for s in range(length):
                x = pos[0]
                y = pos[1]
                x += 1
                pos = (x, y)
                update_path(grid, pos, label)
        elif direction == 'D':
            for s in range(length):
                x = pos[0]
                y = pos[1]
                y -= 1
                pos = (x, y)
                update_path(grid, pos, label)
        elif direction == 'L':
            for s in range(length):
                x = pos[0]
                y = pos[1]
                x -= 1
                pos = (x, y)
                update_path(grid, pos, label)
        else:
            raise Exception('Unknown direction {}'.format(direction))
    return grid


# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83
p1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
p2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

q1 = ['R8','U5','L5','D3']
q2 = ['U7','R6','D4','L4']

i = open("input.txt").read().splitlines()
i1 = i[0].split(',')
i2 = i[1].split(',')

grid = {}
move(i1, grid, 'A')
move(i2, grid, 'B')

crossings = []
for key in grid.keys():
    if grid[key] == 'X':
        crossings.append(key)

crossings = [abs(t[0]) + abs(t[1]) for t in crossings]
print(min(crossings))


