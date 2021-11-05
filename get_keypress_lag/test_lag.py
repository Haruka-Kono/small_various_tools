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

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
key = ['p', ';', 'p', ';', 'p', ';', 'p', ';', 'p', ';', 'p', ';', 'p', ';', 'p', ';', 'p', ';', 'p', ';']
data = np.stack([list, key])
df = pd.DataFrame(data)
df = df.T
df.columns = ['count', 'key']
# print(df)

damage = [1.5, 2.5, 3.5, 4.5]
gap = [1, 2, 3, 4]
data_2 = np.stack([damage, gap])
df_2 = pd.DataFrame(data_2)
df_2 = df_2.T
df_2.columns = ['damage', 'gap']
# print(df_2)
df_bind = pd.concat([df, df_2], axis=0, join='outer')
print(df_bind)
