#!/usr/bin/env python3
"""Perform fixed-rate mortgage calculations."""

from argparse import ArgumentParser
import math
import sys

# replace this comment with your implementation of get_min_payment(),
# interest_due(), remaining_payments(), and main()
def get_min_payment(principal, rate, term = 30, number = 12):
    """
    Takes in total amount of mortgage, annual interest rate, term of the
    mortgage in years, number of payments per year respectively. Term 
    is set to a default of 30 and number set to 12.
    It returns the minimum mortgage payment, rounded up
    """
    r = rate/number
    n = term*number
    amount = (principal * r * ((1 + r) ** n)) / ((( 1 + r )** n) -1)
    return math.ceil(amount)
    
def interest_due(balance, rate, number = 12):
    """
    Accepts balance of the mortgage, annual interest rate, number of
    payments per year. Number is set to default value of 12. It 
    returns the interset due.
    """
    r = rate / number
    i = balance * r
    return i
    
def remaining_payments(balance, rate, target, number = 12):
    """
    Accepts balance of the mortgage, annual interest rate, target payment,
    number of payments per year which is set to a default value of 12. It 
    returns maximum number of remainng payments assuming that all the 
    payments are equal.
    """
    counter = 0
    while balance > 0:
        i = interest_due(balance, rate, number)
        paid = target - i
        balance -= paid
        counter += 1
        
    return counter
    
def main(principal, rate, term, number, target):
    """
    Main. print minimum payment, and check no of payments if target is above minimum payment.
    """
    min_payment = get_min_payment(principal, rate, term, number)
    print("Minimum payment " + str(min_payment))
    
    if not target:
        target = min_payment
    
    if (target < min_payment):
        print("Your target payment is less than the minimum payment for this mortgage")
    else:
        no_of_payments = remaining_payments(principal, rate, target, number)
        print("If you make payments of $" + str(target) + ", you will pay off the mortgage in " + str(no_of_payments) + " payments.")
    
def parse_args(arglist):
    """Parse and validate command-line arguments.

    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)

    Raises:
        ValueError: encountered an invalid argument.
    """
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                             " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                        " (default: the minimum payment)")
    # parse and validate arguments
    args = parser.parse_args()
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")

    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
         args.num_annual_payments, args.target_payment)

