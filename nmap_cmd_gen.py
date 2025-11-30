#!/usr/bin/python

import argparse
import os
import random
import string
import subprocess
import sys


def random_string(length: int = 8) -> str:
    return ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(length, length + 5)))


def execute(cmd: str):
    # in case forget to add "-w"
    if os.name == 'nt':
        cmd = cmd.replace("/tmp", "%localappdata%\\Temp")
    print(f"Executing: {cmd}")
    subprocess.run(cmd, shell=True, check=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(epilog='See: https://github.com/boholder/diffscan2')
    parser.add_argument('--oX-in-tmp', nargs='?', type=str, metavar="PREFIX", const="tmp",
                        help='add "-oX /tmp/PREFIX<random-string>" option, for hiding output from working directory. Default PREFIX="tmp"')
    parser.add_argument('-e', action='store_true', help="execute command")
    parser.add_argument('-w', action='store_true', help="will execute on windows")
    parser.add_argument('nmap_cmd', nargs='+', help='nmap command')
    return parser


def main() -> str:
    args = build_parser().parse_args()
    generated_opts = []

    if args.oX_in_tmp:
        output_path_in_tmp = args.oX_in_tmp + random_string()
        if args.w:
            tmp_dir = "%localappdata%\\Temp"
        else:
            tmp_dir = "/tmp"
        generated_opts.append(f'-oX {tmp_dir}/{output_path_in_tmp}')

    if "nmap" in args.nmap_cmd:
        args.nmap_cmd.remove("nmap")
    _cmd = "nmap " + " ".join(generated_opts + args.nmap_cmd)

    if args.e:
        execute(_cmd)
        sys.exit(0)

    return _cmd


if __name__ == "__main__":
    print(main())
