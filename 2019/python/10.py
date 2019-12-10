import math

f = open("../input/10", "r")
data = [line.rstrip('\n') for line in f]
f.close()

def process_data(data):
    all_positions = {}
    asteroids = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '#':
                all_positions[(col, row)] = True
            else:
                all_positions[(col, row)] = False

    for pos in all_positions:
        if all_positions[pos]:
            asteroids.append(pos)

    return all_positions, set(asteroids)


def x(pos):
    return pos[0]


def y(pos):
    return pos[1]


def in_sight(grid, source, destination):
    dx = x(destination) - x(source)
    dy = y(destination) - y(source)
    x_step, y_step = 0, 0
    gcd = abs(math.gcd(dy, dx))

    if dy == 0:
        x_step = dx // abs(dx)
        n = abs(dx)
    elif dx == 0:
        y_step = dy // abs(dy)
        n = abs(dy)
    else:
        y_step = dy // gcd
        x_step = dx // gcd
        n = gcd

    for i in range(1, n):
        new_pos = (x(source) + x_step*i, y(source) + y_step*i)
        if grid[new_pos]:
          return False
    return True


def count_seeing(asteroids, grid):
    all_seeing = {}
    for source in asteroids:
        seeing = 0
        for destination in asteroids:
            if source != destination:
                if in_sight(grid, source, destination):
                    seeing += 1
        all_seeing[source] = seeing
    return all_seeing


def get_best_asteroid(asteroids):
    best_position = ()
    best_seeing = 0
    for asteroid in asteroids:
        if asteroids[asteroid] > best_seeing:
            best_seeing = asteroids[asteroid]
            best_position = asteroid
    return best_seeing, best_position


def destroy_asteroids(grid, asteroids, source):
    dead = []
    # as long as there are any asteroids alive
    while any(grid[asteroid] for asteroid in grid if asteroid != source):
        angles = []
        for destination in asteroids:
            if source != destination:
                if in_sight(grid, source, destination):
                    dx = x(destination) - x(source)
                    dy = y(destination) - y(source)
                    angle = math.atan2(dx, dy)
                    angles.append((angle, destination))
        # sort and reverse
        angles = sorted(angles)[::-1]
        for angle in angles:
            destination = angle[1]
            dead.append(destination)
            grid[destination] = False
    return dead


def solve_part_one():
    grid, asteroids = process_data(data)
    can_see_count = count_seeing(asteroids, grid)
    most_detected, _ = get_best_asteroid(can_see_count)

    print("p1:", most_detected)


def solve_part_two():
    grid, asteroids = process_data(data)
    can_see_count = count_seeing(asteroids, grid)
    _, best_asteroid = get_best_asteroid(can_see_count)
    destroyed_asteroids = destroy_asteroids(grid, asteroids, best_asteroid)
    asteroid_200 = destroyed_asteroids[199]

    print("p2:", x(asteroid_200) * 100 + y(asteroid_200))


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()

