"""
Taten H. Knight
2021.09.04
Statistical Programming
Fall 2021
Programming Assignment 1 - Online Descriptive Statistics
"""


def online_stats():
    user_value = float(input('Enter a number: '))   # Takes initial user input
    n = 0       # Initial iteration
    xnm = 0     # Initial mean of n-1
    snm = 0     # Initial variance of n-1
    sn = 0      # Initial variance of n

    while user_value >= 0:      # Loop that runs until a negative number is entered
        n = n + 1       # Increase iteration number

        xn = xnm + ((user_value - xnm) / n)     # Update mean with most recent user input

        if n > 1:       # Variance formula is only valid for n>1
            sn = (((n-2) / (n-1)) * snm) + (((user_value - xnm)**2) / n)        # Update variance

        xnm = xn        # Update previous values for next iteration
        snm = sn

        print('Mean is ', xn, ' variance is ', sn)      # Output updated values for the user
        print('')
        user_value = float(input('Enter a number: '))       # Ask the user for another value


print('DATA-51100, Fall 2021')
print('NAME: Taten H. Knight')
print('PROGRAMMING ASSIGNMENT #1')
print('')
online_stats()      # Run online_stats
