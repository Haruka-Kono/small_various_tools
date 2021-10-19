# -*- coding: utf-8 -*-
import keyboard
import time
import datetime
import numpy as np
import pandas as pd

## リスト一群
COUNTS = []
KEYS = []  # 入力キーリスト
RELEASE_LAGS = []  # タイムラグリスト
REACT_LAGS = []
CHAR = []
DLEVEL_PRE = []
DLEVEL_POST = []
i = 1
req_char = 'p'  # 入力要求文字初期値

## 入力要求メッセージ用変数
p = 'press "p"'
semic = 'press ";"'

q = 'press "q"'
a = 'press "a"'

o = 'press "o"'
l = 'press "l"'

w = 'press "w"'
s = 'press "s"'

message = p  # 入力要求メッセージ初期値

now_init = datetime.datetime.now()
now_display = now_init.strftime('%Y-%m-%d %H:%M')
print('現在時刻: '+now_display)
print('画面の指示に従ってキーを打ってください。計80回。多いけど頑張りましょう。p/;, q/aは小指、o/l, w/sは薬指を使ってください。')
time.sleep((1))
print('これから打つのはp/;です。右手小指で打ってください。現在の右手小指の疲労感はどれくらいですか？\
1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。')
damage = input()
# print(damage)
CHAR.append('p/;')
DLEVEL_PRE.append(damage)

print('-----約1秒後にp開始です-----')
time.sleep(1)
print(p)
display = time.perf_counter()

# while i<21:
## esc押すまでwhileブロック内の処理実行。その分なんかしら押さないと始まらない
while keyboard.read_key() != 'esc':

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
        print(i)
        print(key)
        # print(COUNTS)
        # print(KEYS)
        # print(RELEASE_LAGS)
        # print(REACT_LAGS)
        i += 1

    ## 入力要求文字分岐 (iの初期値が諸事情で1なので(i-1)回目になる事に注意)
    if 1 < i < 21 and i % 2 != 0:
        req_char = 'p'
        message = p
    if 1 < i < 21 and i % 2 == 0:
        req_char = ';'
        message = semic

    if 21 < i < 41 and i % 2 != 0:
        req_char = 'q'
        message = q
    if 21 < i < 41 and i % 2 == 0:
        req_char = 'a'
        message = a

    if 41 < i < 61 and i % 2 != 0:
        req_char = 'o'
        message = o
    if 41 < i < 61 and i % 2 == 0:
        req_char = 'l'
        message = l

    if 61 < i < 81 and i % 2 != 0:
        req_char = 'w'
        message = w
    if 61 < i < 81 and i % 2 == 0:
        req_char = 's'
        message = s

    ## 各指入力終了時の処理
    if i == 21:
        print('p/;は終了です。現在の疲労感はどれくらいですか？\
1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。※途中から別の指で打った場合は0を選んでください。')
        damage = input()
        # print(damage)
        # CHAR.append('p')
        DLEVEL_POST.append(damage)
        req_char = 'q'
        message = q
        print('-----次はq/aです。左手小指で打ってください-----')
        print('現在の左手小指の疲労感はどれくらいですか？\
1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。')
        damage = input()
        # print(damage)
        CHAR.append('q/;')
        DLEVEL_PRE.append(damage)
        print('-----約1秒後にq開始です-----')
        time.sleep(1)

    if i == 41:
        print('q/aは終了です。現在の疲労感はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。※途中から別の指で打った場合は0を選んでください。')
        damage = input()
        # print(damage)
        # CHAR.append('q')
        DLEVEL_POST.append(damage)
        req_char = 'o'
        message = o
        print('-----次はo/lです。右手薬指で打ってください。-----')
        print('現在の右手薬指の疲労感はどれくらいですか？ \
1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。')
        damage = input()
        # print(damage)
        CHAR.append('o/a')
        DLEVEL_PRE.append(damage)
        print('-----約1秒後にo開始です-----')
        time.sleep(1)

    if i == 61:
        print('o/lは終了です。現在の疲労感はどれくらいですか？\
1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。※途中から別の指で打った場合は0を選んでください。')
        damage = input()
        # print(damage)
        # CHAR.append('o')
        DLEVEL_POST.append(damage)
        req_char = 'w'
        message = w
        print('-----次はw/sです。左手薬指で打ってください。-----')
        print('現在の左手薬指の疲労感はどれくらいですか？ \
1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。')
        damage = input()
        # print(damage)
        CHAR.append('w/s')
        DLEVEL_PRE.append(damage)
        print('-----約1秒後にw開始です-----')
        time.sleep(1)

    ## 入力文字表示、反応時間測定開始（原則的に最後部）
    time.sleep(0.5)
    print(message)
    display = time.perf_counter()

    if i == 81:
        print('w/s終了です。現在の疲労感はどれくらいですか？\
1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。※途中から別の指で打った場合は0を選んでください。')
        damage = input()
        # print(damage)
        # CHAR.append('w')
        DLEVEL_POST.append(damage)
        break

# keys_array = np.array(KEYS)
# lags_array = np.array(RELEASE_LAGS)
# lag_reacts_array = np.array(REACT_LAGS)
if i > 41:
    data = np.stack([COUNTS, KEYS, RELEASE_LAGS, REACT_LAGS])
    # print(data)
    df = pd.DataFrame(data)
    df = df.T
    df.columns = ['回数', '入力キー', '押下時間', '反応時間']
    now_prefix = now_init.strftime('%Y-%m-%d_%Hh%Mm')
    #print(now_prefix)
    #print(now_prefix+'_test')
    df.to_csv(now_prefix+'_typedata.csv', index=None)
    print(df)

    damage_data = np.stack([CHAR, DLEVEL_PRE, DLEVEL_POST])
    df_d = pd.DataFrame(damage_data)
    df_d = df_d.T
    df_d.columns = ['文字', '開始前疲労', '終了後疲労']
    df_d.to_csv(now_prefix+'_damage.csv', index=None)
    print(df_d)
