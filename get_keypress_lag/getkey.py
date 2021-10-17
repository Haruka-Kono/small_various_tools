# -*- coding: utf-8 -*-
import keyboard
import time
import datetime
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

now = datetime.datetime.now()
print(now)

print('画面の指示に従ってp, q, o, wを打ってください。各15回、計60回。多いけど頑張りましょう。p, qは小指、o, wは薬指を使ってください。')
time.sleep(1)
print(p)
display = time.perf_counter()

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

        print(COUNTS)
        print(KEYS)
        print(RELEASE_LAGS)
        print(REACT_LAGS)

    if i == 15:
        req_char = 'q'
        message = q
        print('-----次はqです-----')
        time.sleep(1)
    if i == 30:
        req_char = 'o'
        message = o
        print('-----次はoです-----')
        time.sleep(1)
    if i == 45:
        req_char = 'w'
        message = w
        print('-----次はwです-----')
        time.sleep(1)

    time.sleep(0.5)
    print(message)
    display = time.perf_counter()
    if i == 60:
        break

# keys_array = np.array(KEYS)
# lags_array = np.array(RELEASE_LAGS)
# lag_reacts_array = np.array(REACT_LAGS)
if i > 30:
    data = np.stack([COUNTS, KEYS, RELEASE_LAGS, REACT_LAGS])
    print(data)
    df = pd.DataFrame(data)
    df = df.T
    df.columns = ['回数', '入力キー', '押下時間', '反応時間']
    now_prefix = now.strftime('%Y-%m-%d_%Hh%Mm')
    #print(now_prefix)
    #print(now_prefix+'_test')
    df.to_csv(now_prefix+'_typedata.csv', index=None,)
    print(df)
