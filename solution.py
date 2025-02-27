import pandas as pd
import numpy as np


chat_id = 157443210  # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 38
    alpha = 1 - p
    z = -np.log(alpha)/len(x)
    
    return (-min(-x) - 1/2) / (t**2 / 2), (z - min(-x) - 1/2) / (t**2 / 2)        

