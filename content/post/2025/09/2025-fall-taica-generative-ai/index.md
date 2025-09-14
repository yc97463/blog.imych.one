---
title: "2025 Fall Taica Generative AI 文字與圖像生成的原理與實務 筆記（持續更新中）"
date: 2025-09-14T22:30:12+08:00
draft: false
categories: ["Coding"]
tags: ["修課紀錄"]
---

# 指令彙整

## `%` Jupyter Notebook 魔術指令

- `%matplotlib inline` 圖表直接顯示在頁面裡
- `%save filename.py 1-5` 儲存第 1 到 5 行程式碼到 filename.py
- `%run filename.py` 執行 filename.py
- `%timeit code` 測量 code 執行時間

## `import` 標準引入套件

- import numpy as np
- import pandas as pd
- import matplotlib.pyplot as plt

## `!` 執行系統指令

- `!ls` 列出目錄內容
- `!pip install package` 安裝 Python 套件
- `!pwd` 顯示目前工作目錄

## plot example

```python
# 從標準常態分佈隨機抽樣
plt.plot(np.random.randn(100)) # 由標準常態分布隨機取 100 個數。

# 畫圖王牌指令: plt.plot
plt.plot([3,-5,7,2]) # 畫出 (0,3), (1, -5), (2,7),  (3,2) 四個點並連線
plt.plot(x, y) # 點的 x 座標 list, y 座標 list
plt.plot([0.8, 1.2, 2.1, 2.8], [2, -5, 3.2, 5])

# 點的表示法
points = [(0.8, 2), (1.2, -5), (2.1, 3.2), (2.8, 5)]
x = [0.8, 1.2, 2.1, 2.8]
y = [2, -5, 3.2, 5]
plt.plot(x, y, 'o') # 用圓圈表示點
plt.plot(x, y, 'ro') # 用紅色圓圈表示點
plt.plot(x, y, 'g^') # 用綠色三角形表示
```

## 互動模式


```python
from ipywidgets import interact # 讀入 interact 函式，進入互動模式
def move(x=1):
  print(" "*x + "oooo")
interact(move, n=(1,50))
```

視覺畫圖表
```python
x = np.linspace(-5, 5, 1000)

def draw(n=1):
    y = np.sinc(n*x)
    plt.plot(x,y, lw=3)
```