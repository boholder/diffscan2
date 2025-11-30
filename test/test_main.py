import sys

import nmap_cmd_gen


def test_add_nmap_if_not_in_input():
    arg = "localhost"
    sys.argv = ["", arg]
    assert nmap_cmd_gen.main() == "nmap " + arg


def test_output_xml_in_tmp():
    sys.argv = [""] + "--oX-in-tmp pre nmap localhost".split()
    r = nmap_cmd_gen.main()
    assert r.startswith("nmap")
    assert "-oX /tmp/pre" in r
    assert "localhost" in r

    sys.argv = [""] + "--oX-in-tmp -- nmap localhost".split()
    r = nmap_cmd_gen.main()
    # default prefix is "tmp"
    assert "-oX /tmp/tmp" in r
