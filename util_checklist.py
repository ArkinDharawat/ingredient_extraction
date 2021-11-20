import json

import numpy as np
from collections import Counter


def sample_testcases(gen_list, n_samples):
    gen_list = np.asarray(gen_list)
    np.random.shuffle(gen_list)
    gen_list_indx = np.random.choice(len(gen_list), n_samples, replace=True)
    return gen_list[gen_list_indx]


def read_json(path):
    with open(path, 'r') as fobj:
        return json.load(fobj)


def get_ingredient_set(train_path, test_path):
    dtrain = read_json(train_path)
    dtest = read_json(test_path)
    dtrain.extend(dtest)
    all_ingredients = []
    [all_ingredients.extend(x["ingredients"]) for x in dtrain]
    N = len(dtrain)
    ing_train = Counter(all_ingredients)
    print(N, (N * 0.1))
    sorted_ing_train = filter(lambda x: x[1] > (N * 0.01), ing_train.items())  # filter if less than 1% of docs

    return list(sorted_ing_train)


