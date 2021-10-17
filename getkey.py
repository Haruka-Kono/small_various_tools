# -*- coding: utf-8 -*-
import keyboard
import time
import numpy as np
import pandas as pd
keys=[] ## 入力キーリスト
lags=[] ## タイムラグリスト
counts=[]
lag_reacts=[]
i=0
#keyboard.wait('esc')
print('press any keysと出たら任意のキーをなるべく早く押してください')
display=time.perf_counter()
#print('p')
#while i<21:
while keyboard.read_key()!='esc': ## esc押すまでwhileブロック内の処理実行。その分なんかしら押さないと始まらない
    #print('p')
    i+=1
    if i > 20:
        break
    counts.append(i)
    press=time.perf_counter()
    key=keyboard.read_key()
    #reac=time.perf_counter()
    release=time.perf_counter()
    print(counts)
    keys.append(key)
    print(keys)
    rel_lag=release-press
    lags.append(rel_lag)
    reaction=press-display
    lag_reacts.append(reaction)
    print(lags)
    print(lag_reacts)
    time.sleep(1)
    print('press any keys')
    display=time.perf_counter()

keys_array=np.array(keys)
lags_array=np.array(lags)
lag_reacts=np.array(lag_reacts)
data=np.stack([counts,keys,lags,lag_reacts])
print(data)
df=pd.DataFrame(data)
df=df.T
df.columns=['回数','入力キー','押下時間','反応時間']
df.to_csv('typedata.csv',index=None)
print(df)
