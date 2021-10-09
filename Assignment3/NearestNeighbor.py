"""
Taten H. Knight
2021.09.19
Statistical Programming
Fall 2021
Programming Assignment 3 - Nearest Neighbor Classification
"""


import numpy as np


def read_csv(path):
    split_file = []
    with open(path) as f:
        for line in f:
            split_file.append(line.replace('\n', '').split(','))
    return split_file


def dist_closure(x_vals):
    def dist(y_vals):
        difs = np.subtract(x_vals, y_vals)
        squares = np.square(difs)
        sums = np.sum(squares, axis=1)
        roots = sums ** .5
        return roots
    return dist


def nearest_neighbor(train_data, train_labels, test_data, test_labels):
    i = 0
    neighbors = np.array([['#', ' True, ', ' Predicted']])
    for data in test_data:
        i = i + 1
        current_distance_function = dist_closure(data)
        distances = current_distance_function(train_data)
        index = np.argmin(distances)
        label = train_labels[index]
        result = np.array([[i, test_labels[i - 1][0], label[0]]])
        neighbors = np.concatenate((neighbors, result))
    return neighbors


def main():
    parsed_testing = np.array(read_csv('iris-testing-data.csv'))
    parsed_test_data = parsed_testing[:, 0:4].astype(float)
    parsed_test_labels = parsed_testing[:, 4:]

    parsed_training = np.array(read_csv('iris-training-data.csv'))
    parsed_train_data = parsed_training[:, 0:4].astype(float)
    parsed_train_labels = parsed_training[:, 4:]

    results = nearest_neighbor(parsed_train_data, parsed_train_labels, parsed_test_data, parsed_test_labels)
    accuracy = np.count_nonzero(parsed_test_labels[:, 0] == results[1::, 2]) / len(parsed_test_labels)

    print('DATA-51100, Fall 2021')
    print('NAME: TATEN H. KNIGHT')
    print('PROGRAMMING ASSIGNMENT 3')
    print()

    for i, result in enumerate(results):
        print(f'{result[0]},{result[1]},{result[2]}')

    print(f'Accuracy: {round(accuracy * 100, 2)}%')



main()




