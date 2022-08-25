import argparse


def parse():
    parser = argparse.ArgumentParser(
        description='Download matrix')
    parser.add_argument('url')
    args = vars(parser.parse_args())
    return args
