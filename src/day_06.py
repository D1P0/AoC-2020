from typing import List, Set

from utils import read_lines

ParsedInput = List[Set[str]]


def parse_input_01(lst: List[str]) -> List[ParsedInput]:
    result: List[ParsedInput] = []
    answers: ParsedInput = []
    for line in lst:
        if line == "":
            result.append(answers)
            answers = []
        else:
            answers.append(set(line))
    if answers:
        result.append(answers)
    return result


def day_06_part01(lst: List[ParsedInput]) -> int:
    res: int = 0
    for block in lst:
        unique_answers = block[0]
        for answers in block:
            unique_answers = unique_answers.union(answers)
        res += len(unique_answers)
    return res


def day_06_part02(lst: List[ParsedInput]) -> int:
    res: int = 0
    for block in lst:
        unique_answers = block[0]
        for answers in block:
            unique_answers = unique_answers.intersection(answers)
        res += len(unique_answers)
    return res


if __name__ == "__main__":
    input_list: List[ParsedInput] = parse_input_01(read_lines())
    print(day_06_part01(input_list))
    print(day_06_part02(input_list))
