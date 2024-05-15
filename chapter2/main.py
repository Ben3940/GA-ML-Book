import pickle
import collections
import math

with open("./data/data_spirangle", "rb") as file:
    path = pickle.load(file)


def entropy(data):
    frequency = collections.Counter([item[-1] for item in data])

    def item_entropy(category):
        ratio = float(category) / len(data)
        return -1 * ratio * math.log(ratio, 2)

    return sum(item_entropy(c) for c in frequency.values())
