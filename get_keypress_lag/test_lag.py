# -*- coding: utf-8 -*-
import keyboard
import time
import datetime
import numpy as np
import pandas as pd

COUNTS = []
KEYS = []  # 入力キーリスト
RELEASE_LAGS = []  # タイムラグリスト
REACT_LAGS = []
CHAR = []
DLEVEL_PRE = []
DLEVEL_POST = []
i = 1
req_char = 'p'  # 入力要求文字

p = 'press "p"'
semic = 'press ";"'

q = 'press "q"'
a = 'press "a"'

o = 'press "o"'
el = 'press "l"'

w = 'press "w"'
s = 'press "s"'
message = p  # 入力キー初期値

now = datetime.datetime.now()
print(now)

print('画面の指示に従ってキーを打ってください。計80回。多いけど頑張りましょう。p/;, q/aは小指、o/l, w/sは薬指を使ってください。')

print('これから打つのはp/;です。右手小指で打ってください。現在の右手小指の疲労感（≒今日のPC作業量）はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。')
damage = input()
# print(damage)
CHAR.append('p')
DLEVEL_PRE.append(damage)

print('-----まもなくp開始です-----')
time.sleep(1)
print(p)
display = time.perf_counter()

# while i<21:
while keyboard.read_key() != 'esc':  # esc押すまでwhileブロック内の処理実行。その分なんかしら押さないと始まらない
    # print('p')
    #    if key == req_char and i == 0:
    #        i += 1
    #        continue

    press = time.perf_counter()
    key = keyboard.read_key()
    release = time.perf_counter()

    if key == req_char and i > 0:
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
        i += 1

    if 1 < i < 21 and i % 2 != 0:
        req_char = 'p'
        message = p

    if 1 < i < 21 and i % 2 == 0:
        req_char = ';'
        message = semic

    time.sleep(0.5)
    print(message)
    display = time.perf_counter()

    if i == 21:
        print('pは終了です。現在の疲労感はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。※途中から別の指で打った場合は0を選んでください。')
        damage = input()
    # print(damage)
    # CHAR.append('p')
        DLEVEL_POST.append(damage)
