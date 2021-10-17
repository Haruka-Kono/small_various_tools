# -*- coding: utf-8 -*-
import keyboard
import time
import numpy as np
import pandas as pd
keys = []  # 入力キーリスト
lags = []  # タイムラグリスト
counts = []
lag_reacts = []
i = 1

p = 'press "p"'
q = 'press "a"'
o = 'press "o"'
w = 'press "w"'
message = p  # 入力キー初期値
# keyboard.wait('esc')
print('指示に従ってキーを入力してください')
time.sleep(1)
print(message)
display = time.perf_counter()
# print('p')
# while i<21:
while keyboard.read_key() != 'esc':  # esc押すまでwhileブロック内の処理実行。その分なんかしら押さないと始まらない
    # print('p')
    counts.append(i)
    press = time.perf_counter()
    key = keyboard.read_key()
    # reac=time.perf_counter()
    release = time.perf_counter()
    if i > 10:
        message = q
    if i > 20:
        message = o
    if i > 30:
        message = w
    print(counts)
    keys.append(key)
    print(keys)
    rel_lag = release-press
    lags.append(rel_lag)
    reaction = press-display
    lag_reacts.append(reaction)
    print(lags)
    print(lag_reacts)
    time.sleep(1)
    print(message)
    display = time.perf_counter()
    i += 1
    if i > 40:
        break


keys_array = np.array(keys)
lags_array = np.array(lags)
lag_reacts = np.array(lag_reacts)
data = np.stack([counts, keys, lags, lag_reacts])
print(data)
df = pd.DataFrame(data)
df = df.T
df.columns = ['回数', '入力キー', '押下時間', '反応時間']
df.to_csv('typedata.csv', index=None)
print(df)
