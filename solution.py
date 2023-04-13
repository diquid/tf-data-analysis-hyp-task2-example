import numpy as np
from scipy import stats

chat_id = 1234206085


def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.08
    test = stats.ks_2samp(x, y)
    p_val = test[1]
    if p_val < alpha:
        return True
    return False
