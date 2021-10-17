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

print('これから打つのはpです。右手小指で打ってください。現在の右手小指の疲労感（≒今日のPC作業量）はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。')
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
        print('pは終了です。現在の疲労感はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。※途中から別の指で打った場合は0を選んでください。')
        damage = input()
        # print(damage)
        # CHAR.append('p')
        DLEVEL_POST.append(damage)

        print('-----次はqです。左手小指で打ってください-----')
        print('現在の左手小指の疲労感（≒今日のPC作業量）はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。')
        damage = input()
        # print(damage)
        CHAR.append('q')
        DLEVEL_PRE.append(damage)
        print('-----まもなくq開始です-----')
        time.sleep(1)

    if i == 30:
        req_char = 'o'
        message = o
        print(
            'qは終了です。現在の疲労感はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。※途中から別の指で打った場合は0を選んでください。')
        damage = input()
        # print(damage)
        # CHAR.append('q')
        DLEVEL_POST.append(damage)

        print('-----次はoです。右手薬指で打ってください。-----')
        print('現在の右手薬指の疲労感（≒今日のPC作業量）はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。')
        damage = input()
        # print(damage)
        CHAR.append('o')
        DLEVEL_PRE.append(damage)
        print('-----まもなくo開始です-----')
        time.sleep(1)
    if i == 45:
        req_char = 'w'
        message = w
        print(
            'oは終了です。現在の疲労感はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。※途中から別の指で打った場合は0を選んでください。')
        damage = input()
        # print(damage)
        # CHAR.append('o')
        DLEVEL_POST.append(damage)

        print('-----次はwです。左手薬指で打ってください。-----')
        print('現在の左手薬指の疲労感（≒今日のPC作業量）はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。')
        damage = input()
        # print(damage)
        CHAR.append('w')
        DLEVEL_PRE.append(damage)
        print('-----まもなくw開始です-----')
        time.sleep(1)

    time.sleep(0.5)
    print(message)
    display = time.perf_counter()

    if i == 60:
        print(
            'w終了です。現在の疲労感はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。※途中から別の指で打った場合は0を選んでください。')
        damage = input()
        # print(damage)
        # CHAR.append('w')
        DLEVEL_POST.append(damage)
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
    df.to_csv(now_prefix+'_typedata.csv', index=None)
    print(df)

    damage_data = np.stack([CHAR, DLEVEL_PRE, DLEVEL_POST])
    df_d = pd.DataFrame(damage_data)
    df_d = df_d.T
    df.columns = ['文字', '開始前疲労', '終了後疲労']
    df_d.to_csv(now_prefix+'_damage.csv', index=None)
    print(df_d)
