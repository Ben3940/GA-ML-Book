import pickle
import collections
import operator
import math

with open("./data/data_spirangle", "rb") as file:
    path = pickle.load(file)


# Compute entropy: how "homogenous" a dataset is
def entropy(data):
    # Last column of data is "frequency" of each category
    frequency = collections.Counter([item[-1] for item in data])

    def item_entropy(category):
        ratio = float(category) / len(data)
        return -1 * ratio * math.log(ratio, 2)

    return sum(item_entropy(c) for c in frequency.values())


def best_feature_for_split(data):
    baseline = entropy(data)

    def feature_entropy(feat):
        def e(v):
            partitioned_data = [d for d in data if d[feat] == v]
            proportion = float(len(partitioned_data)) / float(len(data))
            return proportion * entropy(partitioned_data)

        return sum(e(v) for v in set([d[feat] for d in data]))

    features = len(data[0]) - 1
    information_gain = [baseline - feature_entropy(f) for f in range(features)]
    best_feature, best_gain = max(
        enumerate(information_gain), key=operator.itemgetter(1)
    )

    return best_feature


# Returns tuple of most common category with count of items in category.  If "most" (determine what this is) of data is in category, make a leaf node
def potential_leaf_node(data):
    # Count frequency of items in data, then return most_common frequency
    count = collections.Counter([i[-1] for i in data])
    return count.most_common(1)[0]


def create_tree(data, label):
    category, count = potential_leaf_node(data)

    # All data is in one category, return category
    if count == len(data):
        return category

    node = {}

    # Find feature with best split
    feature = best_feature_for_split(data)
    feature_label = label[feature]

    # Create subtree for feature, represented as Python dict
    node[feature_label] = {}

    # Get all distinct classes based on feature from data
    classes = set([d[feature] for d in data])

    for c in classes:
        # Partition data based on feature
        partitioned_data = [d for d in data if d[feature == c]]
        node[feature_label][c] = create_tree(partitioned_data, label)
    return node
