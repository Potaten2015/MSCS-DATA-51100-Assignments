# Group 3 - Ben Haws, Ashwini Rao, Taten Knight
# K-Means Clustering
# Programming Assignment 2
# DATA51100 Fall 2021

def floatable(s):
    """Determine if an object can be converted to type float"""
    try:
        float(s)
    except ValueError:
        return False
    return True


# MEAN
def mean(x):
    """Compute arithmetic mean of an iterable"""
    return sum(x) / len(x)


# DIST
def dist(p, q):
    """return 1 dimensional Euclidean distance"""
    return abs(p - q)


# ASSIGN CLUSTERS
def assign_clusters(data, clusters, centroids, point_assignments):
    """Assign each data point to the cluster with the nearest centroid, updating point assignments and clusters"""

    # iterate through all items in 'data', finding the nearest centroid to each
    for index1, value1 in enumerate(data):
        min_distance = 1000  # initialize minDistance to a large number to make we don't skip the if statement

        # iterate through all centroids and find the one closest to data point at index1 using dist()
        for index2, value2 in enumerate(centroids):
            if min_distance > dist(data[index1], centroids[index2]):
                min_distance = dist(data[index1], centroids[index2])
                closest_index = index2

        point_assignments[data[index1]] = closest_index

        clusters[closest_index].append(data[index1])


# UPDATE CENTROIDS
def update_centroids(clusters, centroids):
    """Update centroid values to the arithmetic mean of the values in each cluster"""

    for index, value in enumerate(clusters):
        centroids[index] = mean(clusters[index])


def main(max_iter=1000):
    intro = 'DATA-51100, Spring 2021 \nNAMES: Ben Haws, Ashwini Rao, Taten Knight \nPROGRAMMING ASSIGNMENT #2\n'
    print(intro)

    # get data from import file
    with open('prog2-input-data.txt') as infile:
        data = [float(x.rstrip()) for x in infile if floatable(x)]

    k = input('Enter the number of clusters: ')
    # user inputs cluster number k, program exits if non-integer is entered
    try:
        k = int(k)
    except ValueError:
        print(k + ' is not a valid input')
        return
    if k > len(data):
        print('Error: k cannot exceed the number of data points')
        return
    if k < 0:
        print('Error: k must be greater than 0')
        return

    # set centroids--note that centroids are the first k elements of input.txt, not random assignment
    centroids = dict(zip(range(k), data[0:k]))

    # initialize dict for clusters: one empty list per value fro 0-k
    clusters = dict(zip(range(k), [[] for x in range(k)]))

    # initialize dict for point assignments: floats from 'data' are keys and value is cluster (initially 0)
    point_assignments = dict(zip([x for x in data], [0 for x in data]))
    old_point_assignments = dict(zip([x for x in data], [1 for x in data]))

    # Core loop for performing the K-Means algorithm
    iteration = 1
    while point_assignments != old_point_assignments and iteration < max_iter:

        old_point_assignments = point_assignments.copy()

        assign_clusters(data, clusters, centroids, point_assignments)
        update_centroids(clusters, centroids)

        print('Iteration ' + str(iteration))
        for key, value in clusters.items():
            print(key, ' : ', value)
        print('\n')

        clusters = dict(zip(range(k), [[] for x in range(k)]))
        iteration += 1

    # Output point assignments
    for key, value in point_assignments.items():
        print('Point ', key, ' in cluster ', value)

    return


if __name__ == '__main__':
    main()
