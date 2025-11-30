#!/usr/bin/python

import argparse
import random
import string


def random_string(length: int = 8) -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(length, length + 5)))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(epilog='See: https://github.com/boholder/diffscan2')
    parser.add_argument('--oX-in-tmp', nargs='?', type=str, metavar="PREFIX", const="tmp",
                        help='add "-oX /tmp/PREFIX<random-string>" option, for hiding output from working directory')
    parser.add_argument('nmap_cmd', nargs='+', help='nmap command')
    return parser


def main() -> str:
    args = build_parser().parse_args()
    generated_opts = []

    if args.oX_in_tmp:
        output_path_in_tmp = args.oX_in_tmp + random_string()
        generated_opts.append(f'-oX /tmp/{output_path_in_tmp}')

    if "nmap" in args.nmap_cmd:
        args.nmap_cmd.remove("nmap")
    return "nmap " + " ".join(generated_opts + args.nmap_cmd)


if __name__ == "__main__":
    main()
