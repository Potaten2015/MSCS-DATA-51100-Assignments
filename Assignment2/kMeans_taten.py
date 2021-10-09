"""
Taten H. Knight
2021.09.07
Statistical Programming
Fall 2021
Programming Assignment 2 - k-Means Clustering
"""
from time import  time

time1 = time()
file = open('prog2-input-data.txt')


values = [float(value) for value in file]
k = int(input('Enter the number of clusters: '))
while k > len(values) or k < 1:
    if k > len(values):
        k = input('Number of clusters is greater than number of points. Please choose another value: ')
    if k < 1:
        k = input('Number of clusters is less than 1. Please choose another value: ')

clusters = {}
for i in range(k):
    clusters[i] = {}
    clusters[i]['values'] = []
    clusters[i]['mean'] = values[i]
clusters[0]['values'] = values


changes = 1
iteration = 0


def my_deep_copy(dictionary):
    return_thing = {}
    if type(dictionary) is dict:
        for key in dictionary:
            return_thing[key] = my_deep_copy(dictionary[key])
    elif type(dictionary) is list:
        return_thing = []
        for item in dictionary:
            return_thing.append(my_deep_copy(item))
    else:
        return dictionary

    return return_thing

while changes > 0:
    changes = 0
    iteration = iteration + 1
    clusters_copy = my_deep_copy(clusters)
    for cluster in clusters_copy:
        for value in clusters_copy[cluster]['values']:
            nearest_mean = clusters_copy[cluster]['mean']
            nearest_dist = abs(nearest_mean - value)
            nearest_cluster = cluster
            for check_cluster in clusters_copy:
                check_mean = clusters_copy[check_cluster]['mean']
                check_dist = abs(check_mean - value)
                if check_dist < nearest_dist:
                    nearest_cluster = check_cluster
                    nearest_mean = check_mean
                    nearest_dist = check_dist
            if nearest_cluster != cluster:
                changes = changes + 1
                clusters[nearest_cluster]['values'].append(value)
                del clusters[cluster]['values'][clusters[cluster]['values'].index(value)]
    if changes > 0:
        for cluster in clusters:
            key_sum = sum(clusters[cluster]['values'])
            key_len = len(clusters[cluster]['values'])
            new_mean = key_sum / key_len
            clusters[cluster]['mean'] = new_mean

    print('Iteration', iteration)
    for cluster in clusters.keys():
        print(cluster, clusters[cluster]['values'])
    print()

for cluster in clusters.keys():
    for value in clusters[cluster]['values']:
        print('Point', value, 'in cluster', cluster)

print(final_time)