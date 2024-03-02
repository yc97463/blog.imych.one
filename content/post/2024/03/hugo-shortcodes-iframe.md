---
title: "在 Hugo Site 中插入 iframe 內嵌視窗"
date: 2024-03-02T13:21:00+08:00
slug: hugo-shortcodes-iframe
draft: false
categories: ["Coding", "Website"]
---

你也想在你的 Hugo 部落格裡嵌入其他網站的畫面，但因為 Hugo 不支援 iframe 功能而放棄嗎？這篇教學會一步一步教你在 Hugo 裡新增自訂的簡短原始碼。如果你也相同的需求，照著這篇教學就能解決了。

<!--more-->

昨天把部落格從 [nobelium](https://github.com/craigary/nobelium) 又再遷回來 Hugo。由於 Hugo 沒有內建 embde iframe 的功能，讓原先嵌入的 Google 簡報都無法使用，所以我查了一點資料實作。


# 寫一段 Hugo Shortcodes

前面有提到 Hugo 本身是不支援 `<iframe` 標籤的，所以直接在單篇文章中使用反而會造成編譯錯誤。
因此我們要來寫一段簡短原始碼，讓 Hugo 在編譯的時候知道 `<iframe ...> ` 的用法。

```bash
➜  blog.imych.one git:(main) ✗ hugo 
Start building sites … 
hugo v0.123.6-92684f9a26838a46d1a81e3c250fef5207bcb735+extended darwin/arm64 BuildDate=2024-02-28T18:29:40Z VendorInfo=brew

Total in 617 ms
Error: error building site: process: readAndProcessContent: "/Users/yc97463/Documents/projects/blog.imych.one/content/post/2023/08/sitcon2022-vlogger.md:13:1": failed to extract shortcode: template for shortcode "iframe" not found
```
iframe 標籤在還沒有被定義前的編譯結果：shortcode "iframe" not found

## 確認 shortcodes 資料夾

在你的 Hugo 根目錄應該會有 `layouts` 資料夾。我們要把我們的 shortcodes 原始碼放在 `layouts` 的 `shortcodes` 資料夾裡，如果 `shortcodes` 資料夾不存在則由你建一個。

## 建立原始碼

確認好放 shortcode 的資料夾後，我們要來寫 `<iframe` 原始碼了。

在剛剛的 `/layouts/shortcodes/` 資料夾底下建立一個檔案 `iframe.html`，接著貼上下面的原始碼。

```html
<iframe src="{{ .Get 0 }}"></iframe>
```

這時文章的 `<iframe` 在指令 `hugo` 編譯時就能正確解析，內嵌視窗出現了！

![](../images/hugo-shortcodes-iframe/SCR-20240302-mgpa.png)

## 套用美美的 CSS

目前已經完成一半了，但在編譯後在前端的呈現可能有點大小不搭嘎，所以我們要來為 iframe 內嵌視窗補一點樣式。

在 Hugo 的路徑 `/assets/css/` 下有個 `extended` 資料夾，裡面可以放佈景主題之外的樣式檔。我們建立一個新的檔案 `iframe.css`，接著貼上下面的原始碼。

這裡所定義的 `iframe` 會在容器最寬或最高時，維持 16:9 的長寬比例，並且套用圓角 ><（圓角好香）。

我的 16:9 的畫面比例通常用於 YouTube 影片、Google Slide 簡報內嵌，可以根據需要調整。

```css
iframe {
    aspect-ratio: 16 / 9;
    width: 100%;
    height: 100%;
    border-radius: 4px;
    border: 0;
}
```

如此一來就能得到符合容器寬度且 16:9 比例的內嵌視窗了！

![](../images/hugo-shortcodes-iframe/SCR-20240302-mneb.jpeg)




# 參考資料

- [Embedding Iframe in Hugo Site](https://stackoverflow.com/questions/68036749/embedding-iframe-in-hugo-site)
- [Hugo Shortcodes](https://gohugo.io/content-management/shortcodes/)
- [creating a 16:9 aspect ratio iframe based on browser size (percentage)](https://stackoverflow.com/questions/32664971/creating-a-169-aspect-ratio-iframe-based-on-browser-size-percentage)
- [aspect-ratio - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/aspect-ratio)