import keyboard
import time
import numpy as np
import pandas as pd
keys = []  # 入力キーリスト
lags = []  # タイムラグリスト
counts = []
lag_reacts = []
i = 1


#print('p')
#display=time.perf_counter()
press = time.perf_counter()
key = keyboard.read_key()
release = time.perf_counter()
#reac=time.perf_counter()
#reaction=reac-display
#lag_reacts.append(reaction)
#print(lag_reacts)
rel_lag = release-press
lags.append(rel_lag)


print(lags)
keyboard.wait('esc')
