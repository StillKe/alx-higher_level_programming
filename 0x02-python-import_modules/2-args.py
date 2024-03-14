#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1
    args_list = sys.argv[1:]

    print("{} argument{}:".format(num_args, 's' if num_args != 1 else ''), end='')
    print('.' if num_args == 0 else '')

    for i, arg in enumerate(args_list):
        print("{}: {}".format(i + 1, arg))

