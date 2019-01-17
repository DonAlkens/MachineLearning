import numpy as np
from warnings import warn
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
# from math import sqrt
import pandas as pd

style.use("fivethirtyeight")

# plot1 = [1, 3]; plot2 = [2, 5]
# euclidean_distance = sqrt( (plot1[0] - plot2[0])**2 + (plot1[1] - plot2[1])**2 )
# print(euclidean_distance)


datasets = {"k":[[1, 2], [2, 3], [3, 1]], "r":[[6, 5], [7, 7], [8, 6]]}
new_features = [5, 7]


def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warn("K is set to values less than total voting groups")
    distances = []

    for group in data:
        for features in data[group]:
            euclidean_distances = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distances, group])
 
    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1] / k

    return vote_result, confidence


result, confidence = k_nearest_neighbors(datasets, new_features, k=5)
print(result, confidence)
