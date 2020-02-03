import math

# Replace position 1 with value 12, position 2 with value 2

puzzle_input = [1, 38, 92, 3,
                1, 1, 2, 3,
                1, 3, 4, 3,
                1, 5, 0, 3,
                2, 13, 1, 19,
                1, 19, 10, 23,
                1, 23, 13, 27,
                1, 6, 27, 31,
                1, 9, 31, 35,
                2, 10, 35, 39,
                1, 39, 6, 43,
                1, 6, 43, 47,
                2, 13, 47, 51,
                1, 51, 6, 55,
                2, 6, 55, 59,
                2, 59, 6, 63,
                2, 63, 13, 67,
                1, 5, 67, 71,
                2, 9, 71, 75,
                1, 5, 75, 79,
                1, 5, 79, 83,
                1, 83, 6, 87,
                1, 87, 6, 91,
                1, 91, 5, 95,
                2, 10, 95, 99,
                1, 5, 99, 103,
                1, 10, 103, 107,
                1, 107, 9, 111,
                2, 111, 10, 115,
                1, 115, 9, 119,
                1, 13, 119, 123,
                1, 123, 9, 127,
                1, 5, 127, 131,
                2, 13, 131, 135,
                1, 9, 135, 139,
                1, 2, 139, 143,
                1, 13, 143, 0,
                99, 2, 0, 14,
                0]


def evaluate_intcode(original_code_list):

    code_list = original_code_list.copy()
    for position in range(0, len(code_list), 4):

        if code_list[position] == 1:
            # Add values at code_list[position+1] & code_list[position+2] and save at code_list[position+3]
            value1 = code_list[code_list[position + 1]]
            value2 = code_list[code_list[position + 2]]
            save_position = code_list[position + 3]
            value = value1 + value2
            code_list[save_position] = value
            continue

        if code_list[position] == 2:
            # Multiply values at code_list[position+1] & code_list[position+2] and save at code_list[position+3]
            value = code_list[code_list[position + 1]] * code_list[code_list[position + 2]]
            save_position = code_list[position + 3]
            code_list[save_position] = value
            continue

        if code_list[position] == 99:
            continue

    return code_list


target = 19690720
print(evaluate_intcode(puzzle_input)[0])

