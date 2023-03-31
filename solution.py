import pandas as pd
import numpy as np

from scipy.stats import t


chat_id = 157443210  # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    scale = x.std(ddof=1) / np.sqrt(len(x))
    return loc - scale * t.ppf(1 - alpha / 2, df = len(x) - 1), \
           loc + scale * t.ppf(1 - alpha / 2, df = len(x) - 1)       
    
