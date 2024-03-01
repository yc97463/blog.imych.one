---
title: "利用 C++ 實作雙重 Sigma"
date: 2020-08-17T00:00:00+08:00
slug: double-sigma-in-c
draft: false
categories: ["Coding"]
---

# **Σ 小簡介**

在108課綱，「Σ」在高一會暫時由繁雜的公式取代，到高二才會再拿回來用，但 Σ 真的可以將式子簡化很多，而且計算也較繁雜公式簡單許多，就決定寫成 C++ 了。

<!--more-->

Σ 原先是取代 “a 1+a 2+⋯+a n” 的 “⋯”，根據 [尼斯的靈魂](https://frankliou.wordpress.com/2011/12/02/%E4%BA%8C%E9%A0%85%E5%BC%8F%E5%AE%9A%E7%90%86%E8%88%87%E5%A4%9A%E9%A0%85%E5%BC%8F/) 介紹，”⋯” 的語意是非常不清楚的，於是就引進了 Sigma(Σ) 符號概念，也就是求和符號。

# **Σ 服用方式**

1. 為了解決 “⋯” 意義不清的困擾，就以下圖來表示 “a1+a2+⋯+an”。

![a1+a2+⋯+an](../images/double-sigma-in-c/Untitled.png)

a1+a2+⋯+an

1. 雙重 Σ 的運作模式也很神奇，由外而內理解會比較順，而計算由內而外拆解會比較順。

既然已經知道單層及雙層 Σ 的運作原理，接下來就要來挑戰雙重 Σ 運算。

# **雙重 Σ 運算**

假設我們以這組雙重 Σ 為例。

![Untitled](../images/double-sigma-in-c/Untitled%201.png)

## **理解 由外→內**

原式 →

![Untitled](../images/double-sigma-in-c/Untitled%202.png)

由外面向內拆解，會發現到內層

![Untitled](../images/double-sigma-in-c/Untitled%203.png)

會向外列式計算（ i 逐漸增加），最終列式結果會像這樣。

## **實作 由內→外**

而實做由內而外拆解，全部拆解完會如下方這樣的倒三角形。

![Untitled](../images/double-sigma-in-c/Untitled%204.png)

# **利用 C++ 實作雙重 Σ**

但這樣手算很累，而且很如意就會計算錯誤，因此我將計算部分帶入 C++ 實作。

在這裡（以 CodeBlocks 為例）定義完變數 i、j 後，基本上只需要了解 for 或 while 迴圈，就可以照著解 Σ 的邏輯寫出程式。你可能會發現到最後一行 “9×10+” 最後面居然多出了一個 “+”，沒錯只因為我懶，這個 “+” 可以再透過 if 判斷是否為最後一組，進而不輸出 “+” 字符。

![Untitled](../images/double-sigma-in-c/Untitled%205.png)