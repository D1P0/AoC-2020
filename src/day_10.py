from typing import List, Dict

from utils import read_lines

ParsedInput = List[int]


def parse_input(lines: List[str]) -> ParsedInput:
    return list(map(int, lines))


def day_10_part01(x: ParsedInput) -> int:
    x.sort()
    differences: List[int] = [0, 0, 0, 0]
    output: int = 0
    for charger in x:
        differences[charger - output] += 1
        output = charger
    differences[3] += 1
    return differences[1] * differences[3]


def day_10_part02(x: ParsedInput) -> int:
    x.sort()
    variations: Dict[int, int] = {0: 1}
    for adapter in x:
        variations[adapter] = variations.get(adapter - 1, 0) + variations.get(adapter - 2, 0) + variations.get(adapter - 3, 0)

    return variations[x[-1]]


if __name__ == "__main__":
    parsed_input: ParsedInput = parse_input(read_lines())
    print(day_10_part01(parsed_input))
    print(day_10_part02(parsed_input))
