"""
Taten H. Knight
2021.09.25
Statistical Programming
Fall 2021
Programming Assignment 4 – Estimating Probabilities
"""


import pandas as pd


def p(occurences, total):
    return occurences / total


def main():

    print("DATA-51100, FALL 2021")
    print("NAME: TATEN H. KNIGHT")
    print("PROGRAMMING ASSIGNMENT #4")
    print()

    cars = pd.read_csv('cars.csv')
    aspiration_types = pd.unique(cars['aspiration'])
    makes = pd.unique(cars['make'])
    total_cars = cars.shape[0]
    make_probabilities = []

    for make in makes:
        make_vector = cars['make'] == make
        make_number = len(make_vector.to_numpy().nonzero()[0])
        for aspiration_type in aspiration_types:
            aspiration_vector = cars['aspiration'] == aspiration_type
            match_vector = aspiration_vector.multiply(make_vector)
            conditional_aspiration_probability = p(len(match_vector.to_numpy().nonzero()[0]), make_number) * 100
            print(f'Prob(aspiration={aspiration_type}|make={make}) = {"%.2f" % conditional_aspiration_probability}%')

        make_probability = p(make_number, total_cars) * 100
        make_probabilities.append([make, make_probability])

    print('')
    for values in make_probabilities:
        print(f'Prob(make={values[0]}) = {"%.2f" % values[1]}%')


main()
