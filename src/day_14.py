import re
from typing import List, Pattern, AnyStr, Union, Match, Dict

from utils import read_lines


class MemWrite:
    def __init__(self, address: int, value: int):
        self.address: int = address
        self.value: int = value


ParsedInput = List[Union[str, MemWrite]]

mask_pattern: Pattern[AnyStr] = re.compile("^mask = (?P<mask>[01X]{36})$")
mem_pattern: Pattern[AnyStr] = re.compile("^mem\\[(?P<address>[0-9]+)] = (?P<value>[0-9]+)$")


def parse_input(lines: List[str]) -> ParsedInput:
    res: ParsedInput = []
    for line in lines:
        match: Match = re.match(mem_pattern, line)
        if match:
            res.append(MemWrite(int(match.group("address")), int(match.group("value"))))
        else:
            match = re.match(mask_pattern, line)
            res.append(match.group("mask"))
    return res


def memory_sum(memory: Dict[int, int]) -> int:
    res: int = 0
    for address in memory.keys():
        res += memory[address]
    return res


def apply_mask(mask: str, value: int) -> int:
    new_value: int = 0
    for bit in range(36):
        if mask[35 - bit] == "X":
            new_value += value & (1 << bit)
        else:
            new_value += int(mask[35 - bit]) * (2 ** bit)
    return new_value


def apply_address_mask(mask: str, address: int) -> List[int]:
    addresses: List[int] = [0]
    for bit in range(36):
        if mask[35 - bit] == "0":
            addresses = list(map(lambda x: x + (address & (1 << bit)), addresses))
        elif mask[35 - bit] == "1":
            addresses = list(map(lambda x: x + 2 ** bit, addresses))
        else:
            for i in range(len(addresses)):
                addresses.append(addresses[i] + 2 ** bit)
    return addresses


def day_14_part01(instructions: ParsedInput) -> int:
    memory: Dict[int, int] = dict()
    mask: str = ""
    for inst in instructions:
        if isinstance(inst, str):
            mask = inst
        else:
            memory[inst.address] = apply_mask(mask, inst.value)
    return memory_sum(memory)


def day_14_part02(instructions: ParsedInput) -> int:
    memory: Dict[int, int] = dict()
    mask: str = ""
    for inst in instructions:
        if isinstance(inst, str):
            mask = inst
        else:
            for address in apply_address_mask(mask, inst.address):
                memory[address] = inst.value
    return memory_sum(memory)


if __name__ == "__main__":
    parsed_input: ParsedInput = parse_input(read_lines())
    print(day_14_part01(parsed_input))
    print(day_14_part02(parsed_input))
