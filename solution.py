import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 157443210  # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    t_mean = np.mean(x)
    s = np.sqrt(np.mean((2/t_mean - x / np.square(t_mean)) ** 2))
    a = 2 / np.square(t_mean)
    return a - norm.ppf(1 - alpha / 2) * (s / np.sqrt(len(x))), \
           a + norm.ppf(1 - alpha / 2) * (s / np.sqrt(len(x)))    




    
