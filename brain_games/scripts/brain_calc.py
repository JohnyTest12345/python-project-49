#!/usr/bin/env python3

from ..games.calc_logic import get_task, issue
from ..games.logic_games import logic


def main():
    ans = issue()
    logic(ans, get_task)


if __name__ == '__main__':
    main()
