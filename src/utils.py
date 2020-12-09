from typing import List


def read_input() -> str:
    with open("input.txt", "r") as f:
        return f.read()


def read_lines() -> List[str]:
    lines: List[str] = []
    with open("input.txt", "r") as f:
        for line in f:
            if line[-1] == "\n":
                lines.append(line[:-1])
            else:
                lines.append(line)
        return lines
