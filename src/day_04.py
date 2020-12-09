import re
from typing import List, Dict, Pattern, AnyStr

from utils import read_lines

hcl_pattern: Pattern[AnyStr] = re.compile("^#[0-9a-f]{6}$")
pid_pattern: Pattern[AnyStr] = re.compile("^[0-9]{9}$")


ParsedInput = Dict[str, str]


required_fields: List[str] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
allowed_ecl: List[str] = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def parse_input(lst: List[str]) -> List[ParsedInput]:
    result: List['ParsedInput'] = []
    passport: ParsedInput = {}
    for line in lst:
        if line == "":
            result.append(passport)
            passport = {}
        else:
            items: List[str] = line.split(" ")
            for item in items:
                key, value = item.split(":", 1)
                passport[key] = value
    if passport:
        result.append(passport)
    return result


def has_required_fields(x: ParsedInput) -> bool:
    for field in required_fields:
        if field not in x:
            return False
    return True


def check_int(x: str, low: int, top: int) -> bool:
    a: int = int(x)
    return low <= a <= top


def check_byr(x: str) -> bool:
    return check_int(x, 1920, 2002)


def check_iyr(x: str) -> bool:
    return check_int(x, 2010, 2020)


def check_eyr(x: str) -> bool:
    return check_int(x, 2020, 2030)


def check_hgt(x: str) -> bool:
    if x[-2:] == "cm":
        return check_int(x[:-2], 150, 193)
    elif x[-2:] == "in":
        return check_int(x[:-2], 59, 76)
    return False


def check_hcl(x: str) -> bool:
    return re.search(hcl_pattern, x) is not None


def check_ecl(x: str) -> bool:
    return x in allowed_ecl


def check_pid(x: str) -> bool:
    return re.search(pid_pattern, x) is not None


def day_04_part01(lst: List[ParsedInput]) -> int:
    count: int = 0
    for passport in lst:
        if has_required_fields(passport):
            count += 1
    return count


def day_04_part02(lst: List[ParsedInput]) -> int:
    count: int = 0
    for passport in lst:
        if has_required_fields(passport) and check_byr(passport["byr"]) and check_iyr(passport["iyr"]) and\
                check_eyr(passport["eyr"]) and check_hgt(passport["hgt"]) and check_hcl(passport["hcl"]) and\
                check_ecl(passport["ecl"]) and check_pid(passport["pid"]):
            count += 1
    return count


if __name__ == "__main__":
    input_list: List[ParsedInput] = parse_input(read_lines())
    print(day_04_part01(input_list))
    print(day_04_part02(input_list))
