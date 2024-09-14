import argparse
import time
import cd_key
import oem_key
import eleven_cd_key


def error_msg():
    return "Looks like you've started script with invalid arguments\n" \
           "Use 'python generator.py -c' to generate a single CD key\n" \
           "Use 'python generator.py -o -n 1' to generate a single OEM key\n" \
           "Use 'python generator.py -e -n 3' to generate three 11-digit CD keys\n" \

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Use python generator.py <arg(s)> to generate CD, OEM or 11-digit key')
    parser.add_argument('-c', '--cdkey',
                        action='store_true',
                        help='Generate CD keys')
    parser.add_argument('-o', '--oemkey',
                        action='store_true',
                        help='Generate OEM keys')
    parser.add_argument('-e', '--elevencdkey',
                        action='store_true',
                        help='Generate 11-digit CD keys')
    parser.add_argument('-n', '--number',
                        help='Number of keys to generate (default: 1)')
    args = parser.parse_args()

    if args.cdkey is True or args.oemkey is True or args.elevencdkey is True:
        number = int(args.number) if args.number != None and args.number.isdecimal() else 1 
        now = int(time.time())
        for _ in range(number):
            if args.cdkey is True:
                generated = cd_key.cd_keygen_first_segment() + '-' + cd_key.check_seven_digit()
            elif args.oemkey is True:
                generated = oem_key.oem_first_segment() + '-OEM-' + oem_key.check_second_digit() + '-' + oem_key.oem_third_segment()
            elif args.elevencdkey is True:
                generated = eleven_cd_key.eleven_cd_keygen_first_segment() + '-' + eleven_cd_key.check_seven_digit()
            print(generated)
    else:
        print(error_msg())
