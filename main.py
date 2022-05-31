#  Copyright (c) 2022. Illia Popov.

decimal_to_hex_conversion_table = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}

hex_to_decimal_conversion_table = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}


def reverse_hex_string(hex_string: str):
    # FFAB -> ABFF

    hex_string_reversed = ""

    for i in range(len(hex_string) - 1, 0, -2):
        hex_string_reversed += hex_string[i - 1:i + 1]

    return hex_string_reversed


def int_to_hex(int_value: int):
    result = ""

    while int_value != 0:
        result += decimal_to_hex_conversion_table[int_value % 16]
        int_value = int_value // 16

    return result[::-1]


def hex_to_little_endian(hex_string: str):
    result = 0
    hex_string = reverse_hex_string(hex_string)

    for i in range(len(hex_string)):
        result += (hex_to_decimal_conversion_table[hex_string[i]]) * (16 ** (len(hex_string) - 1 - i))

    return result


def hex_to_big_endian(hex_string: str):
    result = 0

    for i in range(len(hex_string)):
        result += (hex_to_decimal_conversion_table[hex_string[i]]) * (16 ** (len(hex_string) - 1 - i))

    return result


def little_endian_to_hex(little_endian: int, num_of_bytes: int):
    result = reverse_hex_string(int_to_hex(little_endian))
    result += "".join(['00' for _ in range(num_of_bytes - len(result) // 2)])
    return result


def big_endian_to_hex(big_endian: int):
    return int_to_hex(big_endian)


if __name__ == '__main__':
    value = input("0x").lower()

    number_of_bytes = len(value) // 2
    print(f'Number of bytes: {number_of_bytes}')

    little_endian_value = hex_to_little_endian(value)
    print(f'Little-endian: {little_endian_value}')

    big_endian_value = hex_to_big_endian(value)
    print(f'Big-endian: {big_endian_value}')

    print(f'Little-endian to hex: {little_endian_to_hex(int(little_endian_value), number_of_bytes)}')

    print(f'Big-endian to hex: {big_endian_to_hex(int(big_endian_value))}')
