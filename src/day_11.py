from typing import List, Tuple, Callable

from utils import read_lines

ParsedInput = List[List[str]]

directions: List[Tuple[int, int]] = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]


def parse_input(lines: List[str]) -> ParsedInput:
    lst: ParsedInput = []
    for line in lines:
        lst.append(list(line))
    return lst


def count_occupied_adjacent(seats: ParsedInput, x: int, y: int) -> int:
    height: int = len(seats)
    width: int = len(seats[0])
    count: int = 0
    for dir_x, dir_y in directions:
        pos_x: int = x + dir_x
        pos_y: int = y + dir_y
        if 0 <= pos_y < height and 0 <= pos_x < width and seats[pos_y][pos_x] == "#":
            count += 1
    return count


def count_occupied_adjacent_extended(seats: ParsedInput, x: int, y: int) -> int:
    height: int = len(seats)
    width: int = len(seats[0])
    count: int = 0
    for dir_x, dir_y in directions:
        shift: int = 1
        while True:
            pos_x: int = x + dir_x * shift
            pos_y: int = y + dir_y * shift
            if 0 <= pos_y < height and 0 <= pos_x < width:
                if seats[pos_y][pos_x] == "#":
                    count += 1
                    break
                elif seats[pos_y][pos_x] == "L":
                    break
            else:
                break
            shift += 1
    return count


def count_occupied(seats: ParsedInput) -> int:
    height: int = len(seats)
    width: int = len(seats[0])
    count: int = 0
    for y in range(height):
        for x in range(width):
            if seats[y][x] == "#":
                count += 1
    return count


def sit_round(seats: ParsedInput, seat_limit: int, func: Callable[[ParsedInput, int, int], int]) -> Tuple[ParsedInput, bool]:
    changed: bool = False
    height: int = len(seats)
    width: int = len(seats[0])
    new_seats: List[List[str]] = []
    for y in range(height):
        new_seats.append([])
        for x in range(width):
            if seats[y][x] == "L" and func(seats, x, y) == 0:
                new_seats[y].append("#")
                changed = True
            elif seats[y][x] == "#" and func(seats, x, y) > seat_limit:
                new_seats[y].append("L")
                changed = True
            else:
                new_seats[y].append(seats[y][x])
    return new_seats, changed


def day_11_part01(seats: ParsedInput) -> int:
    while True:
        seats, changed = sit_round(seats, 3, count_occupied_adjacent)
        if not changed:
            return count_occupied(seats)


def day_11_part02(seats: ParsedInput) -> int:
    while True:
        seats, changed = sit_round(seats, 4, count_occupied_adjacent_extended)
        if not changed:
            return count_occupied(seats)


if __name__ == "__main__":
    parsed_input: ParsedInput = parse_input(read_lines())
    print(day_11_part01(parsed_input))
    print(day_11_part02(parsed_input))
