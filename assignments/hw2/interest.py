"""
Name: Caleb Quattlebaum
interest.py

Problem: this program calculates the monthly interest charge on a given account

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def main():
    # gather annual interest rate, days in billing cycle,
    # net balance, payment amount, and day of payment from user
    air = eval(input("What is the annual interest rate (in percentage)? "))
    bill_cycle = eval(input("How many days are in the billing cycle? "))
    net = eval(input("What is the current net balance? "))
    paid = eval(input("How much was the payment? "))
    dop = eval(input("What day of the billing cycle was the payment made on? "))
    # multiply net balance on statement by number of days in billing cycle
    net_cycle = net * bill_cycle
    # multiply net payment received by number of days payment was received before end of cycle
    # days before end of cycle = days in cycle - day of payment
    payment = paid * (bill_cycle - dop)
    # subtract result of calculation in step 2 from result of calculation in step 1
    total = net_cycle - payment
    # divide result of step 3 by number of days in billing cycle
    # resulting value is avg daily balance
    adb = total / bill_cycle
    # multiply avg daily balance by monthly interest rate (annual interest rate / 12)
    # multiply interest rate by .01 to convert from percentage to float
    monthly_interest = adb * ((air / 12) * .01)
    print(round(monthly_interest, 2))

if __name__ == "__main__":
    main()
