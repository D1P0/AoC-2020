from typing import List

from utils import read_lines

ParsedInput = str


def parse_input(x: List[str]) -> List[ParsedInput]:
    return x


def day_03_part01(lst: List[ParsedInput], u: int, v: int) -> int:
    y: int = 0
    x: int = 0
    count: int = 0
    length: int = len(lst[0])
    while y < len(lst):
        if lst[y][x] == "#":
            count += 1
        x = (x + u) % length
        y += v
    return count


def day_03_part02(lst: List[ParsedInput]) -> int:
    count: int = day_03_part01(lst, 1, 1)
    count *= day_03_part01(lst, 3, 1)
    count *= day_03_part01(lst, 5, 1)
    count *= day_03_part01(lst, 7, 1)
    count *= day_03_part01(lst, 1, 2)
    return count


if __name__ == "__main__":
    input_list: List[ParsedInput] = parse_input(read_lines())
    print(day_03_part01(input_list, 3, 1))
    print(day_03_part02(input_list))
