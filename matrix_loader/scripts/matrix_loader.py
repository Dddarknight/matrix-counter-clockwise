#!/usr/bin/env python

from matrix_loader.page import get_matrix
from matrix_loader.cli import parse
import asyncio


def main():
    args = parse()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_matrix(args['url']))


if __name__ == '__main__':
    main()
