# AI Investment HQ Knowledge Index

> **Status:** Official Single Source of Truth
> **Version:** v1.0（首次正式標示版本號，2026-07-29；此前文件內容存在但未標示版本，經G大確認內容一致，追溯定為v1.0）
> **Effective date:** 2026-07-29
> **Owner:** AI Investment HQ

本文件為 AI Investment HQ 唯一知識入口（Single Source of Truth）。之後 Daily War Room、Event Update、Quarterly Review 均以本 Index 作為引用順序。

## Analysis Execution Order

所有 Official Daily War Room、Event Update、Quarterly Review 執行前，AI 必須依下列順序讀取正式文件，不得依聊天歷史或模型記憶推論：

1. `AI_Investment_HQ_INDEX.md`（唯一知識入口）
2. `01_AI_Investment_HQ_Constitution.md`（最高治理，含第 8 章官方中文術語規範）
3. `Daily_War_Room_SOP.md`（正式流程，含每日固定輸出、Action Layer、結案摘要、資訊分級）
4. `AI基本面追蹤框架_v1.2.md`（Decision Layer 唯一依據）
5. Research Documents（Research Evidence，依 Knowledge Map 分支引用，見下）
6. Portfolio（最新持股，家庭投資中心唯一持股來源）

Portfolio 為家庭投資中心唯一持股來源（Single Source of Truth）。AI 必須先讀取 Portfolio，再完成 Framework、Decision Layer、Action Layer 與 Official Daily War Room。

## Governance

`01_AI_Investment_HQ_Constitution.md`

用途：最高治理規範，含官方中文術語規範（第 8 章）與正式文件地圖。

`AI_Investment_HQ_知識模型治理規範.md`

用途：`07_AI產業全景圖.md` 及未來知識地圖類文件之共同 Schema 治理規範（Node Naming Standard、Connection Standard、Projection Standard、Atomic Update Rule、Version Governance）。不隸屬任何研究文件，為獨立治理文件。

`08_正式輸出格式規範.md`

用途：正式輸出九欄格式、固定值、Action Layer 格式之唯一權威依據。GE、G大、Claude 三方所有正式分析輸出均須引用本文件，不得自行重新定義或推導固定值。如與 Constitution 第 8 章、SOP 之輸出格式條文有出入，以本文件最新版本為準。

## Workflow

`Daily_War_Room_SOP.md`

用途：Daily War Room 執行流程、每日固定輸出十項、Action Layer、結案摘要、資訊分級（框架級情報／背景事件／短線操作情報）。

## Decision Framework

`AI基本面追蹤框架_v1.2.md`

用途：Decision Layer 唯一判斷依據，三層架構（Leading／Confirmation／Validation）與失效條件定義。

## Research Knowledge（依知識分支引用）

Research Knowledge 分為 **AI Knowledge** 與 **Market Knowledge** 兩個獨立分支，兩者互不隸屬，各自可獨立擴充：

### AI Knowledge 分支

`07_AI產業全景圖.md`

用途：AI 生態系長期知識拓樸結構（Knowledge Map），描述 Capability Node 與 Technical Instantiation，不維護市場狀態或研究結論。供 04、06 引用作為分類依據；本身不引用 04、06 之研究結論。

`04_AI基礎建設投資分析_v1.0.md`

用途：公司研究、供應鏈研究、事件背景、Research Evidence。引用 07 之 Capability Node 作為分類依據。不得直接作為 Decision。

`06_AI供應鏈關聯公司清單.md`

用途：正式持股（欣興、華邦電、00991A、00981A、00988A、00997A）對應之供應鏈關聯公司範圍界定，供背景事件證據交叉驗證使用；研究輸出須標明「主要影響持股」。每季檢視更新。引用 07 之節點結構作為上游依據。

### Market Knowledge 分支

`05_台股市場籌碼分析.md`

用途：法人、ETF、融資、市場情緒、籌碼研究、Research Evidence。不隸屬 AI Knowledge 分支，無直接引用 07 之關係。不得直接作為 Decision。

`Seasonality_Strategy_TW_2009_2026_v1.0.md`

用途：台股季度與月份季節性評估、Decision Layer Supporting Evidence、加碼節奏／現金比例／風險控管之輔助資料。不得凌駕 Framework，不得直接作為長期趨勢判斷或 Decision。

## Daily War Room 引用順序

```text
Step 1
Constitution（含第 8 章術語規範）
  ↓
Step 2
SOP（含資訊分級判定）
  ↓
Step 3
Framework
  ↓
Step 4
Research Evidence
（AI Knowledge：07 全景圖 → 04 基礎建設投資分析 → 06 供應鏈關聯公司清單）
（Market Knowledge：05 台股市場籌碼分析、季節性策略）
  ↓
Step 5
Portfolio（家庭投資中心）
  ↓
Step 6
Decision Layer
  ↓
Step 7
08 正式輸出格式規範（輸出前依此規範完成九欄格式與 Self-QA）
  ↓
Official Daily War Room
```

本文件僅作為知識索引，不得新增任何新規則。文件識別碼一經建立即為永久識別碼，不因知識架構調整而重新編號；知識體系之層級與依賴關係由本索引及各文件內部引用關係表達。

---

## 版本紀錄

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-07-29 | 首次正式標示版本號。此前文件內容已存在並持續使用（G大知識庫、Drive手機的資料夾均有一致內容），但檔案本身從未標示版本標頭，屬治理文件格式缺口補正，非內容變更。G大先前口頭回報之「v1.2」經比對確認為口頭推算版本，與實際檔案內容不符，故不沿用該版號，改依實際可追溯狀態重新定為v1.0。 |
