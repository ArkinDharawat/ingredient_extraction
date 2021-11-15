import numpy as np


def sample_testcases(gen_list, n_samples):
    gen_list = np.asarray(gen_list)
    np.random.shuffle(gen_list)
    gen_list_indx = np.random.choice(len(gen_list), n_samples, replace=True)
    return gen_list[gen_list_indx]

