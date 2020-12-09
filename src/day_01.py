from typing import List

from utils import read_lines


def parse_input(x: List[str]) -> List[int]:
    return list(map(int, x))


def day_01_part1(x: List[int]) -> int:
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] + x[j] == 2020:
                return x[i] * x[j]


def day_01_part2(x: List[int]) -> int:
    for i in range(len(x)):
        for j in range(len(x)):
            for k in range(len(x)):
                if x[i] + x[j] + x[k] == 2020:
                    return x[i] * x[j] * x[k]


if __name__ == "__main__":
    input_list: List[int] = parse_input(read_lines())
    print(day_01_part1(input_list))
    print(day_01_part2(input_list))
