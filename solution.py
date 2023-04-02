import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 157443210  # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    scale = np.var(x, ddof=1) + 0.5
    return loc - norm.ppf(1 - alpha / 2) * np.sqrt(scale / len(x)), \
           loc + norm.ppf(1 - alpha / 2) * np.sqrt(scale / len(x))    
    

    
