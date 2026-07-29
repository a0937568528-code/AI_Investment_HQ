# AI Investment HQ Constitution

> **Status:** Official Single Source of Truth
> **Version:** v1.5.0
> **Effective date:** 2026-07-28
> **Owner:** AI Investment HQ

## 1. Purpose

本文件定義 AI Investment HQ 的永久原則、文件治理與決策邊界。凡屬長期有效的規則、流程與定義，均應收錄於正式文件，而非僅存在於聊天紀錄。

## 2. Source of Truth hierarchy

當資訊互相衝突時，依下列優先順序處理：

1. 本 Constitution（永久原則與治理）
2. `02_Daily_War_Room_SOP.md`（每日作業規範）
3. 主題研究文件（基本面、基礎建設、籌碼）
4. 當日 Official Daily War Room（當日判讀與行動）
5. 聊天紀錄、草稿、未驗證筆記

聊天紀錄只能作為工作素材；經確認的永久規則必須回寫至本文件或對應正式文件。

## 3. Operating principles

- **Evidence first：** 結論須可追溯至官方資料、財報、公司公告、可信市場資料或明確標示的推論。
- **Separate facts from interpretation：** 事實、Framework 判讀、投資決策與觀察事項分開呈現。
- **Decision before narrative：** 每日輸出優先交代影響、燈號、決策層與觀察條件。
- **No false precision：** 資料不足時明確標示「待確認」，不得以猜測補齊。
- **Portfolio-aware：** 所有判讀都須連結家庭帳戶的實際曝險與今日影響。
- **Versioned change：** 長期規則或框架變更必須更新版本並登錄 `CHANGELOG.md`。

## 4. Official document map

| File | Authority | Purpose |
|---|---|---|
| `01_AI_Investment_HQ_Constitution.md` | Permanent | 原則、治理與文件層級 |
| `02_Daily_War_Room_SOP.md` | Operational | 每日戰情室流程與品質標準 |
| `03_AI基本面追蹤框架.md` | Research | AI 產業與公司基本面追蹤 |
| `04_AI基礎建設投資分析.md` | Research | AI 基礎建設投資分析 |
| `05_台股市場籌碼分析.md` | Research | 台股籌碼、資金與市場結構 |
| `06_AI供應鏈關聯公司清單.md` | Research | 正式持股對應之供應鏈關聯公司範圍界定，供背景事件證據交叉驗證使用（每季檢視） |
| `07_AI產業全景圖.md` | Knowledge Map | AI 生態系長期知識拓樸結構，供 04、06 引用作為分類依據；不維護市場狀態或研究結論 |
| `AI_Investment_HQ_知識模型治理規範.md` | Governance | 07 及未來知識地圖類文件之共同 Schema 治理規範（Node／Connection／Projection／Version Governance） |
| `08_正式輸出格式規範.md` | Governance | 正式輸出九欄格式、固定值、Action Layer 格式之唯一權威依據，GE／G大／Claude 三方共同引用 |
| `CHANGELOG.md` | Governance | 正式文件變更紀錄 |

## 5. Governance rules

- 不覆蓋既有研究內容；新內容以日期、版本或新增章節方式整合。
- Framework 的定義、燈號邏輯與決策層級一旦調整，須說明變更原因與生效日。
- Daily War Room 是當日官方快照；它不取代永久規則或主題研究。
- 未完成 Final QA 的內容不得標示為 Official。

## 6. Decision boundary

AI Investment HQ 提供研究、框架化觀察與投資決策支援，不構成投資建議、保證報酬或個別交易指令。最終決策由帳戶持有人負責。

## Family Portfolio Output Rule

所有 Official Daily War Room、Event Update、Quarterly Review、Official Dashboard 必須完整引用 Portfolio 中所有已登錄帳戶。

除非使用者明確指定只分析單一帳戶，否則 AI 不得自行省略任何家庭帳戶，不得僅分析聊天中提及之持股。

## AI 協作輸出規範（AI Collaboration Output Standard）

當 GPT 判斷需要交由 GPT Work 或 Claude 執行時，必須直接產生一段完整、可直接複製貼上的指令（Single Copy Block）。

規範如下：

- 不拆成多段。
- 不先解釋再給指令。
- 不要求使用者自行整理。
- 指令需包含完整背景、目的、限制條件與執行要求，可直接貼至 GPT Work 或 Claude 執行。
- 若無需交由 GPT Work 或 Claude，則直接完成分析，不額外產生交接指令。

## 8. 官方中文術語規範（Official Chinese Terminology Standard）

**適用範圍：** 每日戰情室、重大事件分析、AI 基本面分析、AI 基礎建設分析、市場分析、個股分析、ETF 分析、家庭投資中心分析、季度檢討、Claude 深度研究之正式輸出，以及其他 AI Investment HQ 正式分析文件。

**目的：** 為提升 AI Investment HQ 正式分析文件之一致性、可追溯性與可讀性，所有正式分析、治理文件、標準作業程序、每日戰情室、重大事件分析、季度檢討及正式研究報告，除產業慣用專有名詞外，應優先採用本規範所定義之官方中文術語，作為官方中文用語之唯一依據（Single Source of Truth）。

### 8.1 官方術語對照

| 英文術語 | 官方中文 |
|---|---|
| Source | 資訊來源 |
| Evidence Level | 證據等級 |
| Evidence Type | 證據類型 |
| Fact | 事實 |
| Inference | 推論 |
| Pending | 待驗證 |
| Impact | 影響程度 |
| Supporting Evidence | 支持性證據 |
| Research Evidence | 研究性證據 |
| Framework | 分析框架（不可改寫為「分析架構」；若其他正式文件已有固定名稱，依其名稱為準） |
| Portfolio | 家庭投資中心（正式持股語境）／投資組合（一般描述語境） |
| Claude Research | Claude 深度研究 |
| Constitution | 憲章 |
| INDEX | 知識索引 |
| SOP | 作業標準 |
| Decision Layer | 決策層 |
| Action Layer | 行動層 |
| Watch List | 觀察清單 |
| Dashboard | 儀表板 |
| Background Event | 背景事件 |

### 8.2 正式分析固定治理用語

正式分析應統一採用下列治理用語，不得以語意相近但未經正式定義之詞彙替代：

- 與分析框架不衝突
- 分析框架已獲確認
- 分析框架維持不變
- 未觸發分析框架失效條件
- 支持性證據
- 研究性證據

**「分析框架已獲確認」使用條件：** 僅限財報、法說、公司公告、官方數據等高可信度來源，且已達 Evidence Classification Standard 之「事實」等級時使用。若內容包含「若」「待確認」「需更多證據」「仍待驗證」等表述，一律使用「與分析框架不衝突」，不得使用「分析框架已獲確認」。

**一、官方來源與框架判定分離原則：** 官方公告、官方新聞稿、法說會、財報等，可提升證據可信度與證據等級，但不代表可直接判定為「分析框架已獲確認」。「分析框架已獲確認」僅限該官方證據足以直接驗證既有分析框架（如具體 CapEx 數字、實際訂單、出貨量、法說揭露之財務數據），且分析內容完全建立於該官方證據之上時使用；若官方公告內容僅為策略合作宣告、意向書（Letter of Intent）或未來計畫等前瞻性內容，即使來源為官方，仍應使用「與分析框架不衝突」。官方來源與框架確認程度屬兩個獨立判定維度，不得混用。

**二、媒體衍生財務指標判定原則：** 媒體、研究機構或第三方依據官方資料自行推算之倍數、比例、估值、槓桿、覆蓋率等衍生數值（如「相當於一年營收」「約四倍現金水位」「為既有額度的71倍」），除非公司官方直接揭露該指標，均應視為【推論】，不得直接列為【事實】。引用該類數據時，須標示其來源及推算依據。

**三、新商業模式候選觀察原則：** 當事件可能代表新的產業商業模式、資本配置模式或產業結構變化，但尚缺乏足夠官方證據時，應列入相關研究文件（如 `04_AI基礎建設投資分析.md`）之「候選觀察議題（Candidate Observation）」，不得直接更新正式分析框架。待後續官方公告、SEC 申報、財報揭露相關政策，或出現更多同類型案例，再依正式治理流程評估是否納入正式長期觀察項目。

**四、欄位獨立判定原則：** 九欄各欄位須依各自定義獨立判定，不因其中一欄變動而連動升級其他欄位。例如證據等級由★★★☆☆提升至★★★★☆，不代表證據類型、分析框架、分析框架狀態須隨之同步升級；各欄位之固定值應個別檢驗其判定條件是否成立，避免出現「星等提高，所以框架也一併提高」之隱性推論。

### 8.3 正式分析輸出固定欄位

正式分析之證據與治理判定應依下列欄位輸出，除依本規範修訂程序外，不得自行新增、刪除或變更欄位名稱：

| 欄位 | 說明 |
|---|---|
| 資訊來源 | 事件或資訊來源 |
| 證據等級 | ★☆☆☆☆～★★★★★ |
| 證據類型 | 僅限：事實／推論／待驗證，三選一 |
| 影響程度 | 僅限：🟢正向／⚪中性／🔴負向，三選一，不得自創混合分類（如「中性偏正向」） |
| 分析框架 | 與分析框架不衝突／分析框架已獲確認 |
| 分析框架狀態 | 維持不變／更新 |
| 失效條件 | 未觸發／已觸發 |
| 家庭投資中心 | 持股影響判定（依最新正式版本；若未引用最新版，須明確標示「未評估」） |
| Claude 深度研究 | 啟動／不啟動 |

### 8.4 例外規定

以下產業慣用專有名詞得保留英文，新增或調整保留英文術語應依正式文件修訂程序辦理：

AI、GPU、CPU、HBM、CoWoS、CSP、ASIC、CapEx、ARR、TCO、Agentic AI、AI Factory，以及公司名稱、股票／ETF 代號。

### 8.5 引用規範

所有正式 SOP 應引用本章「官方中文術語規範」。如其他正式文件之術語與本規範不一致，以本規範為優先；如涉及治理架構或名詞重大調整，應同步修訂相關正式文件以維持一致性。

## 9. Version history

| Version | Date | Change |
|---|---|---|
| v1.0.0 | 2026-07-23 | 建立 AI Investment HQ 核心文件治理架構。 |
| v1.1.0 | 2026-07-26 | 新增第 8 章「官方中文術語規範」，正式收錄官方術語對照表、固定治理用語、正式輸出固定欄位與例外規定；原第 7 章 Version history 改列為第 9 章。 |
| v1.2.0 | 2026-07-27 | 第 4 章「Official document map」新增 `06_AI供應鏈關聯公司清單.md`，收錄正式持股（欣興、華邦電、00991A、00981A、00988A、00997A）對應之供應鏈關聯公司範圍界定，供背景事件證據交叉驗證使用。 |
| v1.3.0 | 2026-07-27 | 第 4 章新增 `07_AI產業全景圖.md`（AI Ecosystem Knowledge Map）與 `AI_Investment_HQ_知識模型治理規範.md`（Schema 治理文件）。經三方（使用者／GE／G大）多輪 Architecture Review 收斂，建立 Node／Connection／Projection／Atomic Update／Version Governance 五項核心設計，並以五案例壓力測試驗證後正式凍結 Schema v1.0，依三階段（Structure→Population→Consistency Review）完成 07 v1.0 發布。 |
| v1.4.0 | 2026-07-27 | 第 4 章新增 `08_正式輸出格式規範.md`，將散落於本章第 8 節、SOP Self-QA 清單、G大 Instructions 之九欄輸出格式規則整合為單一權威依據，解決「分析框架」與「分析框架狀態」欄位反覆混淆、誤填框架名稱等重複發生之執行問題。 |
| v1.5.0 | 2026-07-28 | 第 8.2 節新增四項判定原則：①官方來源與框架判定分離原則、②媒體衍生財務指標判定原則、③新商業模式候選觀察原則、④欄位獨立判定原則。源自 NVIDIA-OpenAI 融資擔保與 NVIDIA-SK 集團合作案之三方協作稽核（GE 蒐集情報→G大 九欄判定→Claude 深度研究查證→G大 稽核修正），確立「官方來源提升證據可信度，不必然提升框架確認程度」等治理判準。08 文件同步更新，僅保留對應 Self-QA 檢查項，規則本體統一定義於本節，避免同一規則分散於多份文件。 |
