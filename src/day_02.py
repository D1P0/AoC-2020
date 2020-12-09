import re
from typing import List, Tuple, AnyStr, Pattern

from utils import read_lines

pattern: Pattern[AnyStr] = re.compile("(?P<low>[0-9]+)-(?P<top>[0-9]+) (?P<letter>.): (?P<password>.*)")


def parse_input(x: List[str]) -> List[Tuple[int, int, str, str]]:
    lst = []
    for line in x:
        m = re.match(pattern, line)
        lst.append((int(m.group("low")), int(m.group("top")), m.group("letter"), m.group("password")))
    return lst


def day_02_part01(x: List[Tuple[int, int, str, str]]) -> int:
    valid: int = 0
    for policy in x:
        low, top, letter, pas = policy
        count: int = pas.count(letter)
        if low <= count <= top:
            valid += 1
    return valid


def day_02_part02(x: List[Tuple[int, int, str, str]]) -> int:
    valid: int = 0
    for policy in x:
        low, top, letter, pas = policy
        low -= 1
        top -= 1
        if pas[low] != pas[top] and (pas[low] == letter or pas[top] == letter):
            valid += 1
    return valid


if __name__ == "__main__":
    input_list: List[Tuple[int, int, str, str]] = parse_input(read_lines())
    print(day_02_part01(input_list))
    print(day_02_part02(input_list))
