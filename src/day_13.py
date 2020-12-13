from typing import List, Optional

from congruents import CongruentSystem, CongruentExpression
from utils import read_lines


class Departures:
    def __init__(self) -> None:
        self.my_departure: int = 0
        self.timestamps: List[Optional[int]] = []


ParsedInput = Departures


def parse_input(lines: List[str]) -> ParsedInput:
    dep: Departures = Departures()
    dep.my_departure = int(lines[0])
    for timestamp in lines[1].split(","):
        if timestamp == "x":
            dep.timestamps.append(None)
        else:
            dep.timestamps.append(int(timestamp))
    return dep


def day_xx_part01(x: ParsedInput) -> int:
    min_depart: int = (x.my_departure // x.timestamps[0]) * x.timestamps[0] + x.timestamps[0]
    driver_id: int = x.timestamps[0]
    for timestamp in x.timestamps:
        if timestamp is None:
            continue
        diff: int = x.my_departure % timestamp
        if diff > 0:
            time: int = (x.my_departure // timestamp) * timestamp + timestamp
            if time < min_depart:
                min_depart = time
                driver_id = timestamp
    return (min_depart - x.my_departure) * driver_id


def day_xx_part02(x: ParsedInput) -> int:
    system: CongruentSystem = CongruentSystem()
    for i, timestamp in enumerate(x.timestamps):
        if timestamp is not None:
            system.add(CongruentExpression(-i, timestamp))
    return system.solve().res


if __name__ == "__main__":
    parsed_input: ParsedInput = parse_input(read_lines())
    print(day_xx_part01(parsed_input))
    print(day_xx_part02(parsed_input))
