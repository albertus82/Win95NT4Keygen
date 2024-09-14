# XXXX-XXXXXXX
import random


def eleven_cd_keygen_first_segment():
    first_segment = str(random.randint(0, 9991)).zfill(4)
    last_digit = int(first_segment[2]) + random.randint(1, 2)

    if last_digit == 10:
        first_segment = str(first_segment[0] + first_segment[1] + first_segment[2] + "0")
    elif last_digit == 11:
        first_segment = str(first_segment[0] + first_segment[1] + first_segment[2] + "1")
    else:
        first_segment = str(first_segment[0] + first_segment[1] + first_segment[2] + str(last_digit))

    return first_segment


def keygen_seven_digit():
    six_digits = str(random.randint(0, 999999))
    seventh_digit = random.randint(0, 9)
    while seventh_digit == 0 or seventh_digit >= 8:
        seventh_digit = random.randint(0, 9)
    seven_digits = (six_digits + str(seventh_digit)).zfill(7)

    tsum = 0
    for x in seven_digits:
        tsum += int(x)

    return seven_digits, tsum


def check_seven_digit():
    seven_digits, tsum = keygen_seven_digit()
    while tsum % 7 != 0:
        seven_digits, tsum = keygen_seven_digit()

    return seven_digits
