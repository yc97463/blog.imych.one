---
title: "如何使用簡潔的 @ndhu.edu.tw 電子郵件地址寄信"
date: 2024-04-25T01:40:22+08:00
draft: false
build: 
    list: never
categories: [""]
tags: [""]
---

在使用學校 gms 帳號寄出電子郵件時，電子郵件地址預設以 `xxx@gms.ndhu.edu.tw` 子網域寄出。這篇文章會教你設定使用簡潔的學校主網域 `xxx@ndhu.edu.tw` 寄出信件。

<!--more-->

# 東華信箱轉換歷史

參考 [ems, mail 信箱轉換說明](https://gms.ndhu.edu.tw/transfer.html)，東華在 105 學年間逐步將校內架設的 Mail2000 郵件系統轉移至 Google Workspace 的 Gmail，郵件伺服器也從學生校友郵件伺服器 `ems.ndhu.edu.tw`、教職員工郵件伺服器`mail.ndhu.edu.tw` 整合至 `gms.ndhu.edu.tw`。

目前統一使用 Google 提供的 Gmail 信箱，使用 `xxx@gms.ndhu.edu.tw` 網域登入 Google 帳號，俗稱 gms 帳號。

{{<figure src="../images/email-send-from-ndhu-edu-tw/google-login-at-gms-ndhu-edu-tw.jpeg" title="登入 gms 帳號即可使用東華的信箱">}}

# MX record 配置

電子郵件地址的網域（例如 `@gms.ndhu.edu.tw`）可以理解成一間店的招牌名稱，如果這間店還開了分店，可能就會需要用階層的方式管理，網域也是。在這裡，我們可以看看每個招牌分別對應到實際的地址，也就是郵件伺服器。

從下面的 MX record 中可以得知，圖資因應舊郵件伺服器棄用，將舊的網域與 `ndhu.edu.tw` 均接入 Gmail 中，並且會依照 Google Workspace 的規則自動轉寄，避免漏信。

也就是說，無論收信時使用 `@ndhu.ndhu`、`@ems.ndhu` 或 `@mail.ndhu` 等舊的信箱網域，都會自動轉寄回 `@gms.ndhu.edu.tw` 信箱中。

```bash
# @gms.ndhu.edu.tw 現行 gms 信箱本人，使用 Google Workspace Gmail 服務
➜  ~ dig gms.ndhu.edu.tw MX +short
10 ALT3.ASPMX.L.GOOGLE.COM.
5 ALT2.ASPMX.L.GOOGLE.COM.
10 ALT4.ASPMX.L.GOOGLE.COM.
1 ASPMX.L.GOOGLE.COM.
5 ALT1.ASPMX.L.GOOGLE.COM.

# @ndhu.edu.tw 由 Workspace Gmail 接收，轉寄回 gms 信箱
➜  ~ dig ndhu.edu.tw MX +short
5 ALT2.ASPMX.L.GOOGLE.COM.
10 ALT3.ASPMX.L.GOOGLE.COM.
1 ASPMX.L.GOOGLE.COM.
10 ALT4.ASPMX.L.GOOGLE.COM.
5 ALT1.ASPMX.L.GOOGLE.COM.

# @ems.ndhu.edu.tw 是已棄用的學生校友 Mail2000，但一樣接入 Workspace Gmail 接收，轉寄回 gms 信箱
➜  ~ dig ems.ndhu.edu.tw MX +short
2 ASPMX.L.GOOGLE.COM.
10 ASPMX3.L.GOOGLE.COM.
5 ALT1.ASPMX.L.GOOGLE.COM.
5 ALT2.ASPMX.L.GOOGLE.COM.
10 ASPMX2.L.GOOGLE.COM.
20 ems.ndhu.edu.tw.

# @mail.ndhu.edu.tw 是已棄用的教職員工 Mail2000，但一樣接入 Workspace Gmail 接收，轉寄回 gms 信箱
➜  ~ dig mail.ndhu.edu.tw MX +short
10 ALT4.ASPMX.L.GOOGLE.COM.
10 ALT3.ASPMX.L.GOOGLE.COM.
5 ALT1.ASPMX.L.GOOGLE.COM.
5 ALT2.ASPMX.L.GOOGLE.COM.
1 ASPMX.L.GOOGLE.COM.
```

# @gms.ndhu.edu.tw 和 @ndhu.edu.tw 有什麼差別嗎？

老實說實質上並無差別，尤其是圖資處已為大家設定了自動轉寄規則，信件幾乎不會因為使用舊的電子郵件地址而漏信。

如果你也想要用漂亮簡潔的 `@ndhu.edu.tw` 電子郵件地址寄信，而非長長醜醜的 `@gms.ndhu.edu.tw` 寄信，那麼請繼續看下去。

# 設定使用 @ndhu.edu.tw 網域寄信

## 登入 gms 信箱

[登入東華的 Google 帳號](https://accounts.google.com/v3/signin/identifier?service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&hd=gms.ndhu.edu.tw&theme=mn)，注意這裡使用的帳號是 `xxx@gms.ndhu.edu.tw`。

如果忘記密碼或登入錯誤，請至 [gms/passwd 電子郵件系統重設密碼](https://gms.ndhu.edu.tw/passwd/)。

## 新增 @ndhu.edu.tw 電子郵件地址

在網頁版 Gmail 右上角齒輪，展開 Gmail 設定。

![](../images/email-send-from-ndhu-edu-tw/gmail-go-setting.jpeg)

在「帳戶」頁籤中，預設應該只有 `xxx@gms.ndhu.edu.tw` 帳號本人，我們點選「新增另一個電子郵件地址」。

![](../images/email-send-from-ndhu-edu-tw/gmail-setting-account.jpeg)

這時候會跳出新的視窗來「新增其他的電子郵件」，分別填入以下資料：

- 名稱：你想要的寄件者姓名。
- 電子郵件地址：`xxx@ndhu.edu.tw` 電子郵件地址，`xxx` 同你 gms 電子郵件的帳號名稱，學生是學號。
- 視為別名：取消勾選。

![](../images/email-send-from-ndhu-edu-tw/gmail-add-email-address.jpeg)

按「下一步」後，依照畫面指示驗證信箱即可。

## 設定 @ndhu.edu.tw 為預設收發信件地址

新增完成電子郵件地址後，會跳回來 Gmail 的設定頁面，在「帳戶」分頁中可以完整看到所有新增的電子郵件。

我們剛剛新增的 `@ndhu.edu.tw` 已經成功新增了✅。這時點按「設為預設值」，可以在收發電子郵件時，自動使用 `xxx@ndhu.edu.tw` 網域的信箱郵件地址。

![](../images/email-send-from-ndhu-edu-tw/gmail-set-ndhuedutw-as-default-address.jpeg)

套用成功，你可以使用 `xxx@ndhu.edu.tw` 寄信了！🎉

![](../images/email-send-from-ndhu-edu-tw/gmail-compose-use-ndhuedutw-address.jpeg)

# 我可以也將 @mail.ndhu.edu.tw 加入嗎？

可以。

# 參考資料

- [東華大學教職員、學生暨校友信箱（mail.ndhu.edu.tw, ems.ndhu.edu.tw）轉換說明](https://gms.ndhu.edu.tw/transfer.html)
- [gms.ndhu.edu.tw 電子郵件信箱使用說明](https://gms.ndhu.edu.tw/)
- [How to check domain’s MX ( mail exchange ) records using dig command on Linux](https://linuxconfig.org/how-to-check-domain-s-mx-mail-exchange-records-using-dig-command-on-linux)