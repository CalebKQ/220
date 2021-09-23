"""
Name: Caleb Quattlebaum
mean.py

Problem: this program calculates the RMS Average, Harmonic Mean, and Geometric Mean of
         a set of numbers input by the user.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from math import sqrt

# ask for user to input number of values that will be entered to be calculated
# ask for user to input that many numbers
# evaluate inputs and plug them into equations for RMS Avg, Harmonic Mean, & Geometric Mean
# print the answer for each calculation as it finishes in order (1: RMS, 2: Harmonic, 3: Geometric)

def main():
    # ask user for number of terms to be calculated
    terms = eval(input("How many terms will be calculated? "))
    # create accumulators for each equation
    # Geo Mean acc is 1 because equation requires product rather than sum
    rms_acc = 0
    harm_acc = 0
    geo_acc = 1
    # ask user to input n number of terms
    for num in range(terms):
        num = eval(input("Enter a value: "))
        # for RMS Avg, calc sum of xi**2 and store value
        rms_acc = rms_acc + num ** 2
        # find the square root of the sum / 2
        rms_avg = sqrt(rms_acc / terms)
        # for Harmonic Mean, calc sum of 1 / xi and store value
        harm_acc = harm_acc + 1 / num
        # divide n / sum
        harm_mean = terms / harm_acc
        # for Geometric Mean, calc product of xi and store value
        geo_acc = geo_acc * num
        # calculate nth root by setting product to 1 / n power
        geo_mean = geo_acc ** (1 / terms)

    # print results for all three equations
    print(round(rms_avg, 3))
    print(round(harm_mean, 3))
    print(round(geo_mean, 3))

if __name__ == "__main__":
    main()
