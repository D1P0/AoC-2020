from typing import List

from utils import read_lines

ParsedInput = str


def parse_input(lst: List[str]) -> List[ParsedInput]:
    return lst


def get_seat_id(pos: str, low_row: int, top_row: int, low_col: int, top_col: int) -> int:
    if pos == "":
        return low_row * 8 + low_col
    elif pos[0] == "F":
        return get_seat_id(pos[1:], low_row, (top_row - low_row) // 2 + low_row, low_col, top_col)
    elif pos[0] == "B":
        return get_seat_id(pos[1:], (top_row - low_row) // 2 + low_row + 1, top_row, low_col, top_col)
    elif pos[0] == "R":
        return get_seat_id(pos[1:], low_row, top_row, (top_col - low_col) // 2 + low_col + 1, top_col)
    elif pos[0] == "L":
        return get_seat_id(pos[1:], low_row, top_row, low_col, (top_col - low_col) // 2 + low_col)


def day_05_part01(lst: List[ParsedInput]) -> int:
    max_id: int = 0
    for pos in lst:
        seat_id: int = get_seat_id(pos, 0, 127, 0, 7)
        if seat_id > max_id:
            max_id = seat_id
    return max_id


def day_05_part02(lst: List[ParsedInput]) -> int:
    tickets: List[int] = [i for i in range(128 * 8)]
    for ticket in lst:
        seat_id: int = get_seat_id(ticket, 0, 127, 0, 7)
        tickets.remove(seat_id)
    for i in range(1, len(tickets) - 1):
        my_seat: int = tickets[i]
        if my_seat - 1 != tickets[i - 1] and my_seat + 1 != tickets[i + 1]:
            return my_seat
    return -1


if __name__ == "__main__":
    input_list: List[ParsedInput] = parse_input(read_lines())
    print(day_05_part01(input_list))
    print(day_05_part02(input_list))
