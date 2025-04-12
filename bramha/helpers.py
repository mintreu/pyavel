import json
import pprint

def load_helpers(root_dir):
    """
    Loads global helper functions. In the future, additional helpers can be registered here.
    """
    print("[*] Global helper functions loaded!")

def dump(*args):
    pp = pprint.PrettyPrinter(indent=2)
    for arg in args:
        print("→")
        pp.pprint(arg)



def dd(*args):
    pp = pprint.PrettyPrinter(indent=2)
    for arg in args:
        print("→")
        pp.pprint(arg)
    exit()