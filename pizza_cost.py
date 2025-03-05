#!/usr/bin/env python3

# Created By: Luke
# Date: Feb 28, 2025
# Calculates the price of a pizza based on the diameter of your pizza

import math  # Math library import


def main():
    print(
        "Welcome to Luke's Pizza program, this program uses the diameter of your desired pizza and calculates a price!"
    )
    # Intro message
    diameter = float(input(("Enter the diameter in inches: ")))
    # Asks user for diameter input
    print()
    subtotal = 4.25 + (1.5 * diameter)
    # Calculates subtotal
    tax = 0.13 * subtotal
    total = subtotal + tax
    print("The total is: {:.2f}".format(total))
    # Displays total price


if __name__ == "__main__":
    main()
