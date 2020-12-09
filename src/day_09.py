from typing import List

from utils import read_lines

ParsedInput = List[int]


def parse_input(lines: List[str]) -> ParsedInput:
    return list(map(int, lines))


def is_valid(x: ParsedInput, i: int) -> bool:
    for j in range(i - 25, i):
        for k in range(i - 25, i):
            if (x[j] + x[k] == x[i]) and (x[j] != x[k]):
                return True
    return False


def contiguous_subset_sum(x: List[int], total: int) -> List[int]:
    for i in range(len(x) - 1):
        subset: List[int] = [x[i]]
        for j in range(i + 1, len(x)):
            subset.append(x[j])
            if sum(subset) == total:
                return subset


def day_09_part01(x: ParsedInput) -> int:
    for i in range(25, len(x)):
        if not is_valid(x, i):
            return x[i]
    return -1


def day_09_part02(x: ParsedInput) -> int:
    subset: List[int] = sorted(contiguous_subset_sum(x, day_09_part01(x)))
    return subset[0] + subset[-1]


if __name__ == "__main__":
    parsed_input: ParsedInput = parse_input(read_lines())
    print(day_09_part01(parsed_input))
    print(day_09_part02(parsed_input))
