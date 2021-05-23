#!/usr/local/bin/python3
# ------------------------------------------------------------------------------
#        name : main.py
#      author : alan claughan
#     version : 1.0.0
#        date : 23-05-2021
# description : will find every prime < MAX_PRIME
#
# ==============================================================================
#

import logging

logging.basicConfig(level=logging.INFO, filename="app.log")

MAX_PRIME = 1000000

def main():
    sieve = [True] * MAX_PRIME
    count = 1

    for i in range(2, MAX_PRIME):
        if sieve[i]:
            print(f"{count:04} {i:<}")
            count += 1
            for j in range(i * i, MAX_PRIME, i):
                sieve[j] = False


if __name__ == '__main__':
    main()

# logging.debug(stuff)
