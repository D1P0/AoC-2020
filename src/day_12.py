from typing import List, Tuple

from utils import read_lines


class Instruction:
    def __init__(self, inst: str, arg: int) -> None:
        self.inst: str = inst
        self.arg: int = arg


ParsedInput = List[Instruction]


def parse_input(lines: List[str]) -> ParsedInput:
    lst: ParsedInput = []
    for line in lines:
        lst.append(Instruction(line[0], int(line[1:])))
    return lst


def rotate(x: int, y: int, angle: int) -> Tuple[int, int]:
    if angle == 0:
        return x, y
    elif angle == 90:
        return -y, x
    elif angle == 180:
        return -x, -y
    else:
        return y, -x


def day_12_part01(instructions: ParsedInput) -> int:
    x: int = 0
    y: int = 0
    rotation: int = 0
    for instruction in instructions:
        if instruction.inst == "N":
            y += instruction.arg
        elif instruction.inst == "S":
            y -= instruction.arg
        elif instruction.inst == "E":
            x += instruction.arg
        elif instruction.inst == "W":
            x -= instruction.arg
        elif instruction.inst == "L":
            rotation = (rotation + instruction.arg) % 360
        elif instruction.inst == "R":
            rotation = (rotation - instruction.arg) % 360
        else:
            if rotation == 0:
                x += instruction.arg
            elif rotation == 90:
                y += instruction.arg
            elif rotation == 180:
                x -= instruction.arg
            else:
                y -= instruction.arg
    return int(abs(x) + abs(y))


def day_12_part02(instructions: ParsedInput) -> int:
    x: int = 0
    y: int = 0
    wp_x: int = 10
    wp_y: int = 1
    for instruction in instructions:
        if instruction.inst == "N":
            wp_y += instruction.arg
        elif instruction.inst == "S":
            wp_y -= instruction.arg
        elif instruction.inst == "E":
            wp_x += instruction.arg
        elif instruction.inst == "W":
            wp_x -= instruction.arg
        elif instruction.inst == "L":
            wp_x, wp_y = rotate(wp_x, wp_y, instruction.arg)
        elif instruction.inst == "R":
            wp_x, wp_y = rotate(wp_x, wp_y, -instruction.arg % 360)
        else:
            x += instruction.arg * wp_x
            y += instruction.arg * wp_y
    return int(abs(x) + abs(y))


if __name__ == "__main__":
    parsed_input: ParsedInput = parse_input(read_lines())
    print(day_12_part01(parsed_input))
    print(day_12_part02(parsed_input))
