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
l = 'press "l"'

w = 'press "w"'
s = 'press "s"'
message = p  # 入力キー初期値

now_init = datetime.datetime.now()
# print(now)

print('画面の指示に従ってキーを打ってください。計80回。多いけど頑張りましょう。p/;, q/aは小指、o/l, w/sは薬指を使ってください。')
print('これから打つのはp/;です。右手小指で打ってください。現在の右手小指の疲労感（≒今日のPC作業量）はどれくらいですか？ 1 (ほとんど疲れていない) ～ 5 (非常に疲れている)の中から選んでください。')
damage = input()
# print(damage)
CHAR.append('p/;')
DLEVEL_PRE.append(damage)

now_prefix = now_init.strftime('%Y-%m-%d_%Hh%Mm')
#print(now_prefix)
#print(now_prefix+'_test')
data = ['1', '2']
df = pd.DataFrame(data)
df = df.T
filename_t = now_prefix+'test.csv'
df.to_csv('./data/'+now_prefix+'test.csv', index=None)
