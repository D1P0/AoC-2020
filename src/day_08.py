from typing import List, Tuple

from utils import read_lines


class Instruction:
    def __init__(self, inst: str, arg: int):
        self.inst: str = inst
        self.arg: int = arg


ParsedInput = List[Instruction]


def parse_input(lines: List[str]) -> ParsedInput:
    instructions: ParsedInput = []
    for line in lines:
        inst, arg = line.split(" ")
        instructions.append(Instruction(inst, int(arg)))
    return instructions


def run(instructions: ParsedInput) -> Tuple[int, bool]:
    seen: List[bool] = [False for _ in instructions]
    acc: int = 0
    ip: int = 0
    while ip < len(instructions):
        if seen[ip]:
            return acc, False
        seen[ip] = True
        if instructions[ip].inst == "acc":
            acc += instructions[ip].arg
            ip += 1
        elif instructions[ip].inst == "jmp":
            ip += instructions[ip].arg
        elif instructions[ip].inst == "nop":
            ip += 1
        else:
            print("Unknown instruction!")
            return -1, False
    return acc, True


def day_08_part01(x: ParsedInput) -> int:
    return run(x)[0]


def find_problem(x: ParsedInput) -> int:
    acc: int = 0
    ip: int = 0
    while ip < len(x):
        if x[ip][2] > 0:
            return ip
        x[ip] = (x[ip][0], x[ip][1], x[ip][2] + 1)
        if x[ip][0] == "acc":
            acc += int(x[ip][1])
            ip += 1
        elif x[ip][0] == "jmp":
            ip += int(x[ip][1])
        elif x[ip][0] == "nop":
            ip += 1
        else:
            print("RIP")
    return ip


def day_08_part02(x: ParsedInput) -> int:
    for ip in range(len(x)):
        if x[ip].inst == "acc":
            continue
        x[ip].inst = "nop" if x[ip].inst == "jmp" else "jmp"
        acc, finished = run(x)
        if finished:
            return acc
        x[ip].inst = "nop" if x[ip].inst == "jmp" else "jmp"


if __name__ == "__main__":
    parsed_input: ParsedInput = parse_input(read_lines())
    print(day_08_part01(parsed_input))
    print(day_08_part02(parsed_input))
