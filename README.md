## hugo new command

如果要建立一篇新文章的話，這樣做：

```bash
hugo new content post/2026/04/<article-slug>/index.md
```

如果這篇文章是 /now 性質的，這樣做：

```bash
hugo new content --kind now now/<date-in-YYYYMMDD>/index.md
```

## 常用的語法

### figure

如果想要幫圖片加上文字解說，這樣做：

```markdown
{{< figure src="<img-path>" title="<your-description>" >}}
```

### iframe

如果想要 embed 一個 iframe 的話，這樣做：

```markdown
{{< iframe "<iframe-src>" >}}
```

## R2 圖片與 Cloudflare 縮圖

### R2 Info

- bucket: blog-imych-one
- path:
  - post: /<slug>/
  - now: /now/<date-YYYYMMDD>/
- tools: wrangler command.

一般文章的 slug 優先使用 front matter 的 `slug`；未設定時使用文章檔名（不含副檔名），bundle 則使用目錄名。包含原本位於 `static/images` 的圖片，都放在 `/<slug>/<檔名>`，例如 `r2:fosdem-2024/photo.jpeg`。R2 object key 不含開頭的 `/`；必要的圖片子目錄會保留，原始檔名不變。

內文圖片使用 R2；front matter 的 `images` 維持原站資源路徑，讓社群分享圖片繼續使用原站資源。本機原圖保留作為備份。圖片引用採百分比編碼，不額外附加版本參數。

### Usage

將原圖上傳到 R2，確認可從 `https://img.imych.one/<物件路徑>` 公開讀取後，文章可直接用 `r2:` 加上物件路徑：

```markdown
![Santa Cruz 旅行照片](r2:now/20261025/20260821-SFO-SantaCruz.jpeg)
```

需要圖說時，使用既有的 figure 語法：

```go-html-template
{{< figure src="r2:now/20261025/20260821-SFO-SantaCruz.jpeg" title="Santa Cruz 旅行照片" >}}
```

兩種語法也接受完整的 `https://img.imych.one/now/20261025/20260821-SFO-SantaCruz.jpeg`。路徑含空白時，Markdown 使用角括號包住目的地，例如 `![照片](<r2:旅行/海邊 照片.jpeg>)`。

模板會自動產生 Cloudflare 轉換網址、`srcset`、依文章欄寬計算的 `sizes`，並預設延遲載入。首屏重要照片可以明確指定 eager；已知尺寸也可填入，未知則省略：

```go-html-template
{{< figure src="r2:now/20261025/20260821-SFO-SantaCruz.jpeg" title="Santa Cruz 旅行照片" loading="eager" width="1280" height="960" >}}
```

設定集中於 `config.yaml`：

```yaml
params:
  cloudflareImages:
    enabled: true
    sourceHost: img.imych.one
    widths: [640, 960, 1280, 1920]
    defaultWidth: 1920
    quality: 75
```

`widths` 使用正整數，`quality` 範圍為 1–100，目前設為 75。`defaultWidth` 控制預設 `src`，目前為 1920px；模板選最小的 ≥`defaultWidth` 候選，沒有則選最大候選。瀏覽器仍會透過 `srcset` 依螢幕條件選擇適合的寬度。轉換使用 `fit=scale-down,format=auto`。`sizes` 對應目前 720px 文章欄寬、768px 斷點及手機左右各 14px 內距；將來調整版面時，需同步更新共用圖片 partial 中的計算。

只有 hostname 符合 `sourceHost` 的 HTTP／HTTPS 圖片會轉換。本機相對路徑、`/images/...`、其他網域、GIF、SVG 及已含 `/cdn-cgi/image/` 的圖片沿用原圖。`enabled: false` 可關閉轉換，`r2:` 仍會展開成原圖網址。模板不下載遠端原圖查詢尺寸，不需要 API token；上傳由你現有的 R2 流程處理。


