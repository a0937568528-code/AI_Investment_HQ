# Diff Summary｜Drive／GitHub 版本對齊

**日期：** 2026-08-20
**核可者：** CIO
**執行方式：** 一次性、可追溯的無人值守同步批次
**GitHub：** `a0937568528-code/AI_Investment_HQ`
**基準提交：** `609c2c69bee9a4a8f86894314870c330a6ab94ae`

## 變更摘要

GitHub `docs/正式輸出格式規範.md` 與 Drive 現行 Governance 檔案均為 v1.8；Drive file ID 為 `1CYHLbO6cSzS1sRE5cbH4GIwqK4yqNPRo`，且與 GitHub 工作樹 SHA-256 一致。回讀確認 v1.7 歷史檔仍保留。v1.8 只新增早報資料可用性示警的精簡呈現規則與相應 Self-QA 條目，並保留缺口事實與未 H4 不得作正式水位引用的限制。本輪已將 GitHub CHANGELOG 的 v1.8 與 Drive 現行 CHANGELOG 對齊；供應鏈 v1.2 亦已以 GitHub 內容回寫 Drive，完成跨系統內容一致化。

## 已驗證不變項

MA21／MA81、100／80／80／0 風控正式規格書 v1.3 與風控官正式指令 v1.1 的 SHA-256 與 Drive 版本一致；本次不修改兩份文件。H0→H4 順序、正式持股水位、極端波動附則、交易權限、CIO 最終決策權與正式發布邊界均不變。

## 回滾方式

如需回滾，將 Drive 現行 v1.8 改名為歷史檔，再將原 Drive file ID `1RdCniLIm1E2RxgvFwR7Z2B5pDoItieA2` 的 v1.7 歷史檔恢復為現行名稱；全程不永久刪除。

## 驗收要求

同步驗收狀態：Drive 現行檔已為 v1.8、v1.7 歷史檔仍可定位；CHANGELOG 與供應鏈 v1.2 已寫回 Drive；GitHub 遠端基準提交可回讀；風控 v1.3／風控官 v1.1 雜湊保持一致。本 Diff Summary 與處置表已歸檔於 Drive Governance，並準備提交至 GitHub `docs/治理紀錄/`。
