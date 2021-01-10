"""
Day 4: Secure Container
"""

from utils import get_lines


def valid_pw(pw):
    pw = str(pw)
    repeated = False
    prev = pw[0]
    for char in pw[1:]:
        if char == prev:
            repeated = True
        if char < prev:
            # digits never decrease. Note lexicographic compare.
            return False
        prev = char

    return repeated


def valid_pw_2(pw):
    pw = str(pw)
    repeated = False
    rep_count = 0
    prev = pw[0]
    for char in pw[1:]:
        if char == prev:
            rep_count += 1
        else:
            # Only if exactly one repeat is this OK.
            if rep_count == 1:
                repeated = True
            rep_count = 0

        if char < prev:
            # digits never decrease. Note lexicographic compare.
            return False
        prev = char

    # Catch a repetition at the end of all things
    if rep_count == 1:
        repeated = True

    return repeated


def puzzle1():
    pw_range = get_lines('day4')[0]  # only one line today
    pw_min, pw_max = map(int, pw_range.split('-'))

    print(len([pw for pw in range(pw_min, pw_max + 1) if valid_pw(pw)]))


def puzzle2():
    pw_range = get_lines('day4')[0]  # only one line today
    pw_min, pw_max = map(int, pw_range.split('-'))

    print(len([pw for pw in range(pw_min, pw_max + 1) if valid_pw_2(pw)]))


if __name__ == '__main__':
    puzzle1()
    puzzle2()
