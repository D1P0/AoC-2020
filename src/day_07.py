import re
from typing import List, Dict, Set, AnyStr, Pattern, Match, Optional

from utils import read_lines

pattern: Pattern[AnyStr] = re.compile("(?P<bag>.+?(?= bags)) bags contain (?P<contents>[^.]*)")
content_pattern: Pattern[AnyStr] = re.compile("(?P<count>[0-9]+) (?P<bag>.+?(?= bags?))")


cache: Dict[str, int] = dict()


ParsedInput = Dict[str, Dict[str, int]]


def parse_input(lst: List[str]) -> ParsedInput:
    rules: ParsedInput = dict()
    for rule in lst:
        match: Match = re.match(pattern, rule)
        bag_content: Dict[str, int] = dict()
        bag: str = match.group("bag")
        contents: str = match.group("contents")

        if contents == "no other bags":
            rules[bag] = bag_content
            continue

        contents: List[str] = contents.split(", ")
        for content in contents:
            match = re.match(content_pattern, content)
            count: int = int(match.group("count"))
            inner_bag: str = match.group("bag")
            bag_content[inner_bag] = count
        rules[bag] = bag_content
    return rules


def get_parent_bags(lst: ParsedInput, bags: List[str]) -> Set[str]:
    result_set: Set[str] = set(bags)
    for rule in lst.keys():
        for bag in bags:
            if bag in lst[rule]:
                result_set.add(rule)
    return result_set


def day_07_part01(lst: ParsedInput) -> int:
    seen: Dict[str, bool] = {"shiny gold": True}
    stack: List[str] = ["shiny gold"]
    count: int = 0
    while stack:
        parent_bags: Set[str] = get_parent_bags(lst, stack)
        stack = []
        for parent_bag in parent_bags:
            if not seen.get(parent_bag, False):
                stack.append(parent_bag)
                seen[parent_bag] = True
                count += 1
    return count


def day_07_part02(lst: ParsedInput, bag: str = "shiny gold", bag_count: int = 1) -> int:
    cached_value: Optional[int] = cache.get(bag, None)
    if cached_value:
        return cached_value * bag_count

    if len(lst[bag]) == 0:
        return 0

    total: int = 0
    for inner_bag in lst[bag].keys():
        inner_count: int = lst[bag][inner_bag]
        total += day_07_part02(lst, inner_bag, inner_count) + inner_count
    cache[bag] = total
    return total * bag_count


if __name__ == "__main__":
    input_list: ParsedInput = parse_input(read_lines())
    print(day_07_part01(input_list))
    print(day_07_part02(input_list))
