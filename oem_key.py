# XXXXX-OEM-XXXXXXX-XXXXX
import random


def oem_first_segment():
    years = ["95", "96", "97", "98", "99", "00", "01", "02", "03"]
    two_digits = random.choice(years)
    three_digits = random.randint(1, 366 if two_digits in ["96", "00"] else 365)
    return str(three_digits).zfill(3) + str(two_digits)


def oem_second_segment():
    middle_digits = random.randint(0, 99999)
    last_digit = random.randint(0, 9)
    while last_digit == 0 or last_digit >= 8:
        last_digit = random.randint(0, 9)

    second_segment = ("0" + str(middle_digits) + str(last_digit)).zfill(7)

    tsum = 0
    for x in second_segment:
        tsum += int(x)

    return second_segment, tsum


def check_second_digit():
    seven_digits, tsum = oem_second_segment()
    while tsum % 7 != 0:
        seven_digits, tsum = oem_second_segment()
    return seven_digits


def oem_third_segment():
    third_segment = random.randint(0, 99999)
    return str(third_segment).zfill(5)
