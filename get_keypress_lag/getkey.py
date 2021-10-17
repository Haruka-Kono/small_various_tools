# -*- coding: utf-8 -*-
import keyboard
import time
import numpy as np
import pandas as pd

KEYS = []  # 入力キーリスト
RELEASE_LAGS = []  # タイムラグリスト
COUNTS = []
REACT_LAGS = []

i = 0
req_char = 'p'  # 入力要求文字
p = 'press "p"'
q = 'press "q"'
o = 'press "o"'
w = 'press "w"'
message = p  # 入力キー初期値

print('指示に従ってキーを入力してください')
time.sleep(1)
print('press enter')
# display = time.perf_counter()

# while i<21:
while keyboard.read_key() != 'esc':  # esc押すまでwhileブロック内の処理実行。その分なんかしら押さないと始まらない
    # print('p')
    press = time.perf_counter()
    key = keyboard.read_key()
    release = time.perf_counter()

    if key == req_char:
        i += 1
        release_lag = release-press
        react_lag = press-display
        KEYS.append(key)
        COUNTS.append(i)
        RELEASE_LAGS.append(release_lag)
        REACT_LAGS.append(react_lag)

    if i == 10:
        req_char = 'q'
        message = q
        # print('-----次はqです-----')
        time.sleep(1)
    if i == 20:
        req_char = 'o'
        message = o
        # print('-----次はoです-----')
        time.sleep(1)
    if i == 30:
        req_char = 'w'
        message = w
        # print('-----次はwです-----')
        time.sleep(1)

    print(COUNTS)
    print(KEYS)
    print(RELEASE_LAGS)
    print(REACT_LAGS)
    time.sleep(0.5)
    print(message)
    display = time.perf_counter()
    if i > 40:
        break

# keys_array = np.array(KEYS)
# lags_array = np.array(RELEASE_LAGS)
# lag_reacts_array = np.array(REACT_LAGS)
data = np.stack([COUNTS, KEYS, RELEASE_LAGS, REACT_LAGS])
print(data)
df = pd.DataFrame(data)
df = df.T
df.columns = ['回数', '入力キー', '押下時間', '反応時間']
df.to_csv('typedata.csv', index=None)
print(df)
