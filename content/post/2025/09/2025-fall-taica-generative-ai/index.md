---
title: "2025 Fall Taica Generative AI 文字與圖像生成的原理與實務 筆記（持續更新中）"
date: 2025-09-14T22:30:12+08:00
draft: false
build:
    list: never
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

# 神經網路

## softmax 

目標是把任意的 a, b, c 三個數字, 轉化為 p1, p2, p3, 而且保持大小關係不變，而且所有數字加起來等於 1。
```python
p1 + p2 + p3 = 1
```

接著，很自然地會想到用指數函數來做轉換，因為指數函數是單調遞增的函數。

```python
Let S = e^a + e^b + e^c

Then we can define:
a b c -> e^a e^b e^c -> e^a/S e^b/S e^c/S
每個數字經過指數函數轉換，再來按比例計算，這就是 softmax 的定義。
```

## 神經元

「神經元」是「神經網路」的基本運算單位，建立一個個隱藏層（hidden layer），每個隱藏層包含多個神經元。每個神經元會接收來自前一層的輸入，進行加權和（weighted sum）運算，然後藉由一個非線性活化函數（或稱作激發函數）（activation function）來產生輸出。

- DNN: Deep Neural Network 深度神經網路 標準全連結，全面考慮型
- CNN: Convolutional Neural Network 卷積神經網路 圖形辨識能力很強
- RNN: Recurrent Neural Network 循環神經網路 適合處理序列資料 有記憶的結構
- Transformer: 變壓器架構 目前最流行的架構

> 流程：計算總刺激 -> 加上偏值 -> 活化函數轉換

### 計算總刺激

這很像是線性迴歸的計算方式，假設有 n 個輸入 x1, x2, ..., xn，對應的權重為 w1, w2, ..., wn，則總刺激 z 的計算公式如下：

```python
z = w1*x1 + w2*x2 + ... + wn*xn
```

### 加上偏值

在計算總刺激後，會加上一個偏值（bias） b，這個偏值可以幫助模型更靈活地調整輸出。加上偏值後的公式變為：

```python
z = (sigma(wi*xi) from i=1 to n) + b
```

### 活化函數（激發函數）轉換

最後，將總刺激 z 放入一個非線性活化函數 fi φ 來產生神經元的輸出 y：

```python
h = fi(z) # φ(Sigma(wi*xi) + b)
```

- ReLU 函數: f(x) = max(0, x) # 目前最流行
- Sigmoid 函數: f(x) = 1 / (1 + exp(-x)) # 最接近人類神經元的函數
- Tanh 函數: f(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x)) # 雙曲正切函數
- Gaussian 函數: f(x) = exp(-x^2) # 高斯函數，已經是舊時代的產物了

### 要學習的參數

theta = {wi, b}

## 開始打造神經網路，函數學習機

Example: 2 個輸入 x1, x2，1 個輸出 y1 的模型，以全連結神經網路為例，製作一個函數學習機。

DNN 一層只需要決定有幾個神經元，例如準備 3 個神經元（三個蘿蔔坑），而前一層有 2 個輸入（兩個蘿蔔），分別會一一對應到這三個坑裡，1 -> 1, 1 -> 2, 1 -> 3, 2 -> 1, 2 -> 2, 2 -> 3。再下一層時，隨意指定要幾個神經元後，也會依序對應， 1 -> 1, 1 -> 2, 1 -> 3, 2 -> 1, 2 -> 2, 2 -> 3, 3 -> 1, 3 -> 2, 3 -> 3。

這就是訓練的過程，過程中會決定每個神經元的權重 w1, w2, ..., wn 和偏值 b，合併起來就是模型的參數 theta θ。
{ w1, w2, ..., wn, b1, b2, ..., bm }

## Loss function 損失函數

損失函數是用來衡量模型預測結果與真實結果之間差異的函數。常見的損失函數有均方誤差（Mean Squared Error, MSE）和交叉熵損失（Cross-Entropy Loss）。

就是 **Mean Squared Error (MSE)** 啦！突然就回到機率課的回憶了（死去的記憶正在攻擊我），之前沒什麼方向在學，所以沒學好那門課。

$$L(\theta) = \frac{1}{2k} \sum_{i=1}^k ||y_i - f_\theta(\mathbf{x}_i)||^2$$

其中：
- $\theta$ 表示模型參數
- $k$ 是樣本數量
- $y_i$ 是真實值
- $f_\theta(\mathbf{x}_i)$ 是模型預測值
- $||.||^2$ 表示歐幾里得距離的平方

所謂訓練，就是想辦法讓 loss 越來越小。 L(θ1) > L(θ2) > L(θ3) > ... > L(θn)，也就是梯度下降法 (Gradient Descent)的過程。

## 參數調整

假裝現在只有一個 w 參數，對於參數 w 來說，調整的方向是讓損失函數 L 變小，也就是讓 L 對 w 的偏微分（partial derivative）變小。

-η * (∂L / ∂w)

- η 是學習率（learning rate），決定每次調整的幅度。
- ∂L / ∂w 是損失函數對參數 w 的偏微分，表示損失函數對 w 的變化率。
這個過程會重複進行，直到損失函數 L 收斂到一個較小的值，或者達到預定的迭代次數為止。
如果遇到斜率產生逆變化，代表可能已經到達局部極小值，這時候就要調整學習率 η，讓它變小一點，避免跳過極小值。這有點像我們在求一個圖形的最低點時，人眼可以很明顯地看到最低點在哪裡，但電腦計算得透過微分來判斷斜率的變化與比較，來得知最低點的位置。

在 w=a 點的切線斜率符號長這樣：

```python
L'(a)
```

對任意點 w 來說，我們寫成函數形式長這樣：

```python   
L'(w) = ∂L / ∂w
```

在 w=a 中，我們可以調整成新的 w 值：

```python
a - L\'(a)
```

對任意 w 來說，使用這樣的公式來調整 w 值：

```python
w - dL/dw
```

## 偏微分

∂L / ∂w 是偏微分的符號，表示損失函數 L 對參數 w 的偏微分。

> 偏微分是指在多變數函數中，對其中一個變數求導數，其他變數保持不變。

∂L / ∂w = dL_w1 / dw_1，意思是把 w1 調整成 w1 - η * (∂L / ∂w1)

[w1, w2, w3, ..., wn] <- [w1, w2, w3, ..., wn] - η * [∂L/∂w1, ∂L/∂w2, ∂L/∂w3, ..., ∂L/∂wn]
= Gradient Descent = [w1, w2, w3, ..., wn] - η * ∇L （梯度 gradient）