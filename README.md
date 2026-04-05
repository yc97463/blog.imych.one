## hugo new command

如果要建立一篇新文章的話，這樣做：

```bash
hugo new content post/2026/04/<article-slug>/index.md
```

如果這篇文章是 /now 性質的，這樣做：

```bash
hugo new content --kind now now/<date-in-YYYY-MM-DD>/index.md
```

## 常用的語法

### figure

如果想要幫圖片加上文字解說，這樣做：

```markdown
{{< figure src="<img-path>" title="<your-description>" >}}
```