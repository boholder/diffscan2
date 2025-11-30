import sys

import nmap_cmd_gen


def test_add_nmap_if_not_in_input():
    arg = "localhost"
    sys.argv = ["", arg]
    assert nmap_cmd_gen.main() == "nmap " + arg
