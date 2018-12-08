#!/usr/bin/python3

from random import uniform
import math

def euclidianDistance(p1, p2):
    return math.sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )


def giveOwnership(distances):
    label = list()
    for dist in distances:
        min_dist = min(dist)
        label.append(dist.index(min_dist))

    return label

def calculateAllDistances(positions, centroids, distFunction=euclidianDistance):
    distances = list()
    for pos in positions:
        list_per_cent = list()
        for index, cent in enumerate(centroids):
            list_per_cent.append(distFunction(cent, pos))

        distances.append(list_per_cent)

    return distances

def generateCentroids(list_x, list_y, k):
    (min_x, min_y) = (min(list_x)-(min(list_x)*0.2),\
                      min(list_y)-(min(list_y)*0.2))
    (max_x, max_y) = (max(list_x)+(max(list_x)*0.2),\
                      max(list_y)+(max(list_y)*0.2))

    return [(uniform(min_x, max_x), uniform(min_y, max_y))\
        for i in range(0, k)]

def updateCentroids(positions, labels, k):
    new_centroids = list()
    for i in range(k+1):
        qtd = len([x for x in labels if x == i])
        point = [0, 0]
        for j, pos in enumerate(positions):
            if labels[j] == i:
                point[0] += pos[0]
                point[1] += pos[1]

        point[0] /= qtd + 0.000000000001
        point[1] /= qtd + 0.000000000001
        new_centroids.append((point[0], point[1]))

    return new_centroids


def kmeans(list_x, list_y, k=1, iter_times=100000, distFunction=euclidianDistance, debug=False):
    positions = list(zip(list_x, list_y))

    centroids = generateCentroids(list_x, list_y, k)

    distances = calculateAllDistances(positions, centroids, distFunction)

    labels = giveOwnership(distances)

    if debug:
        print(f"Positions: {positions}\n\nLabels: {labels}\n\nCentroids: {centroids}\n\nDistancias: {distances}\n\n")

    iter = 0
    has_changed = True

    while has_changed and iter <= iter_times:
        centroids = updateCentroids(positions, labels, k)

        distances = calculateAllDistances(positions, centroids, distFunction)

        labels = giveOwnership(distances)

        if debug:
            print(f"Positions: {positions}\n\nLabels: {labels}\n\nCentroids: {centroids}\n\nDistancias: {distances}\n\n")

        iter += 1

    return labels, centroids


vecx = [1, 2, 2, 1, 3, 4, 4, 5, 6]
vecy = [1, 1, 2, 3, 5, 3, 4, 3, 3]
kmeans(vecx, vecy, k=3, iter_times=4)
