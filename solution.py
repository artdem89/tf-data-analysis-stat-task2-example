import pandas as pd
import numpy as np


chat_id = 157443210  # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 38
    alpha = 1 - p
    min = (-x).min()
    z = -np.log(1-p)/len(x)
    
    return 2*(z-min-1/2)/(t**2), 2*(-min-1/2)/(t**2)        
