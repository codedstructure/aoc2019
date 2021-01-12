"""
Day 6: Universal Orbit Map
"""

from utils import get_lines


def distance(orbit_map, item):
    if item == 'COM':
        return 0
    else:
        return 1 + distance(orbit_map, orbit_map[item])


def orbit_path(orbit_map, item1):
    if item1 == 'COM':
        return []
    else:
        return orbit_path(orbit_map, orbit_map[item1]) + [item1]


def puzzle1():
    orbits = get_lines('day6')
    orbits_map = {}
    objects = set()
    for line in orbits:
        orbitee, orbiter = line.split(')')
        objects.add(orbiter)
        orbits_map[orbiter] = orbitee

    count = 0
    for item in objects:
        count += distance(orbits_map, item)

    print(count)


def puzzle2():
    orbits = get_lines('day6')
    orbits_map = {}
    objects = set()
    for line in orbits:
        orbitee, orbiter = line.split(')')
        objects.add(orbiter)
        orbits_map[orbiter] = orbitee

    you_path = orbit_path(orbits_map, 'YOU')
    san_path = orbit_path(orbits_map, 'SAN')
    # determine length of common prefix
    for idx, (i1, i2) in enumerate(zip(you_path, san_path)):
        if i1 != i2:
            common_path_len = idx
            break
    else:
        raise RuntimeError("No common path")

    # Don't care about the starting node
    you_path.pop()
    san_path.pop()

    print(len(you_path) + len(san_path) - 2 * common_path_len)


if __name__ == '__main__':
    puzzle1()
    puzzle2()
