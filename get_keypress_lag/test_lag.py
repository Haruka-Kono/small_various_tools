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
## esc押すまでwhileブロック内の処理実行。その分なんかしら押さないと始まらない
while keyboard.read_key() != 'esc':
    # print('p')
    #    if key == req_char and i == 0:
    #        i += 1
    #        continue
    ## 入力キー取得、押下終了時間取得
    press = time.perf_counter()
    key = keyboard.read_key()
    release = time.perf_counter()

    ## 入力キー正誤判定及びリスト追加（and i > 0はいらないか？）、表示
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

    ## 入力要求文字分岐 (iの初期値が諸事情で1なので(i-1)回目になる事に注意)
    if 1 < i < 21 and i % 2 != 0:
        req_char = 'p'
        message = p
    if 1 < i < 20 and i % 2 == 0:
        req_char = ';'
        message = semic

    if 21 < i 41 and i % 2 != 0:
        req_char = 'q'
        message = q
    if 21 < i 41 and i % 2 == 0:
        req_char = 'a'
        message = a

    ## 各指入力終了時の処理
    if i == 21:
        print('p/;は終了です。現在の疲労感はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。※途中から別の指で打った場合は0を選んでください。')
        damage = input()
    # print(damage)
    # CHAR.append('p')
        DLEVEL_POST.append(damage)
        req_char = 'q'
        message = q
        print('-----次はq/aです。左手小指で打ってください-----')
        print('現在の左手小指の疲労感（≒今日のPC作業量）はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。')
        damage = input()
        # print(damage)
        CHAR.append('q')
        DLEVEL_PRE.append(damage)
        print('-----まもなくq開始です-----')
        time.sleep(1)

    ## 入力文字表示、反応時間測定開始（原則的に最後部）
    time.sleep(0.5)
    print(message)
    display = time.perf_counter()
