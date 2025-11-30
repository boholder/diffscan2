import getopt
import sys


def usage():
    print("usage: ...")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], '')
    except getopt.GetoptError:
        usage()
        return

    if len(args) < 1:
        usage()
        return


if __name__ == "__main__":
    main()
