#!/usr/bin/env python3

# Created by : Venika Sem
# Created on : Dec 2022
# This program finds perimeter of heptagon


import math


def calculate_heptagon_perimeter(side: int) -> float:
    # Calculates a heptagon perimeter

    if side < 0:
        return -1
    else:
        perimeter = 7 * side
        return perimeter


def main():
    # Gets input and calculate perimeter of heptagon
    try:
        side_as_int = input("Enter side of a heptagon (cm): ")
        side = float(side_as_int)
        heptagon_perimeter = calculate_heptagon_perimeter(side)
        print("\nThis heptagon's perimeter is {} cm".format(heptagon_perimeter))
    except ValueError:
        print("\nInvalid Input.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
