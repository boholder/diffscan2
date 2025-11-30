#!/usr/bin/python

import getopt
import sys
from pathlib import Path


def usage():
    print(f"""
Usage: {Path(__file__).name} [OPTION] nmap-command
OPTION:
    -h, --help  show this help message and exit
""")
    sys.exit(0)


def main() -> str:
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.GetoptError:
        usage()
        return ''

    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()

    if len(args) < 1:
        usage()

    if args[0] == "nmap":
        nmap_cmd = " ".join(args)
    else:
        nmap_cmd = "nmap " + " ".join(args)
    return nmap_cmd


if __name__ == "__main__":
    main()
