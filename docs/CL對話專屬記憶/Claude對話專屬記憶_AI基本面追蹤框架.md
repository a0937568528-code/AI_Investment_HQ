# Claude 對話專屬記憶（Memory）匯出
# 主題：AI基本面追蹤框架 v1.0 與 AI Investment HQ 治理紀錄

> 說明：本檔案內容來自 Claude（claude.ai）背後獨立於 Google Drive 的 memory 系統，
> 是 Claude 在過往對話中整理、儲存的筆記摘要，並非 Google Drive 內任何正式文件的複本。
> 匯出日期：2026-07-31

---

- 採用三層追蹤框架，用於AI相關持股的基本面監控，每季更新一次燈號與觀察結論，架構本身不隨單一事件調整（每年固定review一次架構是否需更新）

## 第一層：長期基本面
- 領先指標：雲端大廠CapEx guidance（Microsoft、Google、Meta、Amazon、Oracle）、Inference/推論用量成長
- 同步指標：台積電CapEx guidance（視為雲端CapEx下游反應，通常落後1-2季，不算領先）

## 第二層：供應鏈景氣（同步指標）
- CoWoS/先進封裝利用率
- HBM/記憶體景氣
- 載板接單（欣興月營收）

## 第三層：驗證端（落後指標）
- Hyperscaler AI Revenue（Copilot/Azure AI/Gemini/AWS AI等）
- AI ROI具體案例
- 持股實際財務表現（00991A淨值、欣興月營收、法人預估）

## 燈號定義
🟢正常／🟡留意／⚪未揭露或資訊不足（不等於惡化）／🔴明確惡化，四級分開判斷，不用0-100分數

## 持股對照
- 00991A：對第一、二層全部高敏感，視為AI景氣溫度計
- 00981A：對第一層（雲端/台積電CapEx）敏感度高
- 欣興：本身即CoWoS/載板接單的觀測標的，不只是受惠股
- 華邦電：獨立於AI CapEx循環，用記憶體循環框架判斷，不套用此框架
- 00988A／00997A：需先確認實際持股才能對應

## 使用紀律
- 領先指標轉黃/紅時不需等落後指標確認即可提高警戒
- 三層訊號不一致時，不因單一新聞或單一事件改變長期投資結論；需多項領先與同步指標持續惡化、且落後指標逐步確認，才重新評估長期投資假設
- 注意財年與自然季錯位（Microsoft、Oracle財年非自然季）
- 每天產出 Daily Brief，涵蓋第一層領先指標、AI需求、半導體、雲端CapEx、台積電、記憶體、網通、ETF、風險、結論等十個固定欄位
- Event Update 只在重大事件時建立；同一事件的新進展以版本號更新（v1.1、v1.2…），不建立新事件
- 工作原則：不重複建立知識或事件、優先引用官方資料、不猜測、不依股價推論基本面、證據不足時明確標示仍需觀察
- Claude 負責第一層分析（Daily Brief、Event Update、知識庫更新、Master Memory 維護）；ChatGPT（AI投資長）負責第二層交叉驗證（排除雜訊、驗證基本面影響、補充風險、評估是否重新評估持股）
- 投資理念：長期投資（5～10年以上）、AI產業為核心配置、基本面優先價格第二、官方資料優先、所有結論須有證據、不因單日漲跌改變看法
- 本框架為最高分析標準，未來所有分析依此框架執行；若投資理念、工作流程或框架有重大更新，應同步更新 Master Memory 而非僅記住零散聊天

## AI_Investment_HQ 資料管理員工作原則
- Claude 擔任 AI_Investment_HQ（Google Drive）資料管理員，只處理新增資料，不重複讀取舊資料
- 新增 PDF 時自動整理成 Markdown
- 內容與知識庫重複時只更新差異，不建立重複文件
- 所有檔案依既定資料夾分類存放
- 除非使用者要求，否則不重新分析整個知識庫，以節省運算資源
- Claude 不主動做投資決策，分析以事實為主
- 資料不足或無法確認時，需明確指出缺少哪些資訊，不自行推測或編造內容
- 優先處理本次新增資料，只有需要交叉比對或更新既有內容時才讀取相關知識庫文件，不每次重新掃描整個 AI_Investment_HQ
- Claude 角色為 AI 研究助理，負責資料蒐集、整理、分類與知識庫維護；投資判斷、策略建議與持股分析由 ChatGPT 負責

## 工作原則更新 v1.1
- 新增資料若可能改變既有知識庫重要結論（核心假設、長期趨勢、失效條件），不直接覆蓋原有內容：保留原有紀錄，另建新版本或更新紀錄，並清楚標示（1）哪一項結論可能需要更新（2）更新原因（3）支持更新的證據（4）目前證據是否足夠或仍需持續觀察
- 知識庫以「證據」為核心而非結論：優先記錄原始事實、官方數據、公司公告、法說內容、財務數字、市場事件；分析、推論與預測需與事實分開紀錄，原始事實保持完整且可追溯

## 工作原則更新 v1.2：AI產業追蹤範圍
- 研究範圍不限於目前持股，每日持續追蹤全球AI產業重要公司：AI晶片（NVIDIA、AMD、Broadcom、Marvell）、晶圓代工（TSMC）、AI雲端（Microsoft、Amazon、Google、Oracle）、AI模型（OpenAI、Anthropic、xAI、Google DeepMind、Meta AI）、半導體設備（ASML、Applied Materials、Lam Research、KLA）、記憶體（SK Hynix、Samsung、Micron）、AI伺服器（Supermicro、Dell、HPE）、AI網路／交換器／CPO（Arista、Cisco、Coherent）
- 追蹤內容包含：法說會、財報、Guidance（財測）、CapEx、重大產品發布、重大合作、官方公告、能影響AI供應鏈的重要新聞
- 事件分級：一般事件→Daily Brief；重大事件→Event Update；法說季→Quarterly Review；不得因單純新聞熱度或股價波動升級事件

## 工作原則更新 v1.3：Daily Brief 精簡化
- 從2026/07/23起，Daily Brief 只保留「真正會影響框架」的事件，一般新聞不放入戰情報告，每日控制在5-8個重點事件
- 使用者以「CIO第二層審核」角色，在 Claude 產出的 Daily Brief 之上再做一層判定，格式包含：Event Level（🟡Level 2等分級）、是否修改框架、是否更新知識庫、失效條件是否觸發，並附五層框架狀態表（AI基本面／AI供應鏈／估值／市場情緒／失效條件）與關鍵事件表

## Event Update 命名與累積原則（2026/07/25 CIO裁示）
- Event Update 以「市場敘事／判讀模式」命名而非單一公司事件，讓同類型後續事件累加為同一份文件的版本更新，避免建立多份重複文件
- 新增 Watch Item：Hyperscaler CapEx Guidance vs Market Reaction（追蹤 Microsoft、Meta、Amazon），觀察重點不只是CapEx是否增加，而是「Guidance↑但股價↓」是否同時出現於三家
- 五層框架中「估值」由🟢調整為🟡（理由：市場提高ROI要求，估值可能重新收斂）；「AI基本面」第一層維持🟢，無公司下修CapEx、無公司證實AI需求放緩
- 事件分級原則再確認：股價下跌 ≠ 基本面轉弱；失效條件為「多家CSP連續兩季下修CapEx」或「多家公司共同證實AI需求放緩」
- 文件治理：Single Source of Truth 原則，正式引用以文件庫內正式版為準；目前正式框架版本為 v1.2（草稿），v1.3 是否已定版列為【待確認】，若定版須同步更新 Index 與 CHANGELOG
- Event Update 日期規則：固定採 Event Date（公司公告／財報發布日，美東日期），與 Daily War Room 記錄日（台灣日期）分開標示
- Event Update 內建固定追蹤表欄位：公司／CapEx Guidance／股價反應／ROI Discussion／Framework判定，後續財報只更新同一表格不重寫文件
- 晨報季節性欄位固定表述：「第三季屬季節性偏保守區間；7月相對較佳，但整體Q3操作仍以控制節奏與風險管理為主」，燈號🟡
- Seasonality 定位：屬 Decision Layer Supporting Evidence，用於調整加碼節奏、現金比例與風險控管，不得凌駕 AI 基本面 Framework
- 技術指標（均線排列、MACD等）與短線過熱訊號比照 Seasonality，同屬 Decision Layer：只用於控制持股水位（進場節奏、分批、現金比例），不用於推翻或質疑第一層基本面判定
- 決定建立「Seasonality Evidence Appendix」，固定收錄 S&P500／NASDAQ／SOX 月份統計與 Midterm Election Cycle，供晨報與框架共同引用

## Repository Governance（2026/07/25 CIO 裁示）
- 採用 Official / Workspace / Archive 三分制：正式文件只能有一份 Official；Workspace（GPT、Claude、GE、草稿）可有多份；Archive 可有多份；正式文件禁止放 Workspace
- 資料夾結構：08_System（治理）／07_Knowledge_Base（研究）／06_Portfolio／05_Event_Update／04_Daily_Brief／03_Research／02_Archive／01_Workspace
- 引用順序：Constitution → SOP → Framework → Research → Portfolio → Daily War Room
- 舊副本一律移入 Archive／不刪除，保留至少三個月（本次為 Archive/2026-07-25 Migration）
- 版本分叉處理原則：不猜、不挑最大、不挑最新，必須逐段 Diff 後才決定 Official；CHANGELOG 分叉須 Merge 而非覆蓋
- 優先順序：①雲端重整 ②Official Repository Policy v1.0（最高）③Framework與CHANGELOG逐版Diff ④舊副本移入Archive ⑤再新增研究內容
- 新增治理紀律（M2完成後正式化）：任何正式文件版本升級（如 v1.2→v1.3）必須附 Diff Summary；沒有 Diff Summary 不得升版、不得更新 INDEX
- Diff 報告格式為「治理導向 Diff」四段式：①Executive Summary ②Chapter Diff（依章節非行號）③Governance Impact 分級（文字修飾無／名稱調整低／新增指標高／修改失效條件極高／修改燈號極高／Action Layer 不屬Framework應移出）④CIO Decision Table（保留A／採用B／合併／捨棄，保留裁定欄）
- Diff 目的不是自動合併，而是提供 CIO 裁定依據
- 程序保留：最終 Official 須以 CIO 對 Diff Report 原文的逐項裁定為準，不得依 Claude 的摘要定案（符合「沒有 Diff，不決定 Official」紀律）
- 若採納，v1.3 定位為「First Official Release」——第一份真正經治理流程定版的 Framework，而非 v1.2 修正版
- D2（領先指標轉黃/紅不需等落後指標確認即可提高警戒）若確認被移除且無等價條文，列為 Critical Governance Regression，優先於 D3 回補
- 裁定後須同步完成三件事：①更新 INDEX 指向 v1.3 ②更新 CHANGELOG（記錄升版原因、治理修正／內容修正／回補三類）③將 Workspace 版 v1.2 移入 Archive 並禁止後續引用
- Frozen Rule（納入 Repository Policy）：文件處於版本分叉期間不得作為新增正式分析的引用來源；若必須引用須標示「版本分叉・待CIO裁定」；凍結解除後由 Official 版本取代所有 Frozen 引用
- ChatGPT／第二層審核者無法存取 Google Drive，需要 Diff Report 等文件以對話貼上或可下載檔案形式提供，才能做獨立逐條審閱
- 未來擴充建議（尚未執行）：加入「文件生命週期 Document Lifecycle」概念——Workspace → Review → Frozen（如有版本分叉）→ Official → Superseded → Archive，讓每份文件任何時刻都有單一明確狀態，而非僅以資料夾位置區分
- 版本號命名空間（Version Namespace）應正式制度化：禁止裸版本號（如「v1.2」），一律寫成「Framework v1.2」「Repository Policy v1.1」「CHANGELOG v1.0」「Daily War Room SOP v1.0.1」；INDEX 也應全面採用此命名方式
- 治理有效性 vs 治理合規性須分離：文件經正式核准後即生效（Validity）；未同步更新 CHANGELOG 屬程序違規需補正（Compliance），不因此推定文件未生效——避免遞迴失效問題。應於 Repository Policy 後續版本釐清
- CHANGELOG 事實錯誤之處理：保留原文＋加註 Correction Note，不直接改寫歷史（稽核紀錄應保留當時狀態）
- 治理分析文件集中管理於 08_System/Governance/，命名格式一致（Framework_Governance_Diff_Report_v1.0、CHANGELOG_Merge_Analysis_v1.0、Repository_Policy_v1.1）
- CHANGELOG Merge 原則：Merge 不 Override——保留 X 的工作原則演進 + Y 的文件庫建立紀錄，合併為唯一 Official，不二選一

## 2026/07/25 優先順序調整：治理線暫停，資源轉研究
- 治理線暫停，不再做 M2++／M3++／Policy v1.2，避免制度過度設計（Over-engineering）；剩餘待辦為 CIO 裁定與人工搬檔，非 Claude 可代替
- 現有治理能力已足以支撐現有規模；下一步是驗證這套治理能否順利支援下一次重大事件（Microsoft／Meta／Amazon 財報），順利運作後再決定是否擴充 M6 Document Lifecycle
- 額度配置：70% Microsoft／Meta／Amazon 財報前研究（直接支援 Event Update v1.1）、20% SOX Seasonality（T1）、10% 保留給突發重大事件（財報意外、FOMC、AI產業重大消息）
- 每家 Hyperscaler 固定回答五題：①CapEx Guidance 是否調整 ②管理層是否提到 ROI／Monetization／Inference ③Azure／AWS／Meta AI 需求是否改變 ④AI 投資是否出現放緩訊號 ⑤市場股價反應是否重演 Alphabet 模式
- SOX Seasonality（T1）目標不是急著找數字，而是確認公開統計是否真的不存在；若結論為「無可靠資料」，那也是一個正式結論
- 工具分工定位：ChatGPT 負責治理、架構、整合、策略討論、日常分析；Claude 負責長篇研究、跨資料整理、深度比較、建立研究基準。治理工作交給 ChatGPT，不佔用 Claude 額度
- Claude 一個月訂閱期的三層使用優先序：①重大事件深度研究（Hyperscaler 財報、NVIDIA／AMD 等 AI 基建公司、FOMC／CPI）②建立長期研究庫（AI供應鏈 HBM／CoWoS／先進封裝、Hyperscaler CapEx 與實體算力 GW／GPU／機櫃的對應關係、雲端業者 AI ROI 與變現模式、AI 基礎建設長期需求模型）③Framework 驗證（哪些指標最有預測力、哪些需補強、是否有新領先指標值得納入）——驗證而非修改
- AI Investment HQ 已從「整理資料」轉向「建立研究方法」；Claude 深度研究的重點應放在驗證假說，而非單純蒐集新聞

## Hyperscaler CapEx Signal Validation（研究主題，2026/07/25 設定）
- 核心研究問題：CapEx 是否已從「需求指標」變成「需求＋成本」的混合指標？此題對 Framework 的影響大於補完 SOX Seasonality
- 研究任務不叫「研究 Microsoft 財報」，而叫「Hyperscaler CapEx Signal Validation」，四個子問題：①三家最新 CapEx Guidance 中有多少來自 AI 需求增加／記憶體 HBM 零組件成本上升／新資料中心建置 ②公司是否揭露實體產能（GW、GPU、Rack、Data Center）③若只公布金額不公布實體產能，是否降低 Guidance 作為需求指標的可信度 ④市場是否已開始區分「CapEx 金額」與「CapEx 品質」
- 新研究假說（尚未驗證）：市場是否已開始更重視「每美元 CapEx 能帶來多少算力」而非「CapEx 總額」；若三家財報都提供 GW／GPU／機櫃／資料中心容量等實體指標且市場更重視這些，代表投資人衡量 AI 投資的方式正在改變
- Claude 重置後第一天任務順序：Task 1 三家財報前 Baseline 驗證 + CapEx = Demand vs Cost 深度研究（最高優先）／Task 2 建立可重複使用的 Hyperscaler Earnings Research Template／Task 3 SOX Seasonality（T1）
- 建立研究 SOP 五階段（非 Framework）：①Hypothesis 假說 ②Pre-registration 事前登錄 ③Event 事件發生 ④Validation 驗證 ⑤Framework Impact 是否影響 Framework。使 Event Update 不只是新聞整理，而是完整研究循環
- 研究假說必須在事件發生前固定（freeze），否則易受事後資訊影響——與治理線 Frozen 概念一致，只是應用到研究流程
- H1 假說固定：CapEx Guidance 已成為需求與成本的混合訊號。預測：三家至少一家明確表示 CapEx 上修部分來自 HBM／DRAM／零組件成本；若未揭露實體產能則該公司 CapEx 作為需求代理指標可信度下降。否證條件：三家皆表示 CapEx 增加主要來自新增 AI 容量且幾乎未提成本因素，或提供足夠實體產能資訊使需求可直接驗證
- H2 於 pre-registration 中須保持中性，不得直接寫「新增指標」，應寫「若證據持續支持，將評估是否納入 Framework 候選觀察項」（目前資料點仍少）
- Alphabet（2026-07-23 已公布）定位為 Baseline Case，非用於驗證 H2，而是回答：法說是否揭露實體容量／分析師是否追問 GW、GPU、Rack、資料中心容量／管理層如何回答。若幾乎沒有，代表市場目前仍主要使用 CapEx 金額
- H2 須區分兩個層次，不可混為一談：**CapEx Quality Disclosure**（揭露 CapEx 組成，如伺服器／資料中心／網通占比）與 **Physical Capacity Disclosure**（揭露實體算力單位，如 GW／GPU／Rack）。Alphabet 目前證據屬前者上升，後者仍未出現
- H1 的正確表述不是「CapEx 已被成本污染」，而是「不同 Hyperscaler 對 CapEx 的組成可能不同，需要驗證」——Alphabet 為反例反而使 H1 更有研究價值
- 財報結束後（若流程順利）建立獨立文件「Research Methodology」或「Hypothesis Validation SOP」：①Hypothesis ②Pre-registration ③Freeze ④Event ⑤Validation Report ⑥Framework Impact Assessment。定位為研究方法而非投資知識，不寫進 Framework，可沿用於 AI、總體經濟、半導體、Seasonality 等所有主題
- 2026/07/25 收尾狀態：治理工作完成階段性目標待 CIO 裁定；H1、H2 已事前登錄並凍結；Alphabet 已建立第一個 Baseline Case；下一個關鍵節點為 Microsoft、Meta、Amazon 財報
- 2026/07/27 資源分配原則：往後工作比重抓 80%分析／20%治理
- 圖卡（視覺化摘要）治理原則：圖卡不具獨立治理效力，正式判定以文字版 Daily Brief 附錄為準；圖卡存檔須加註「僅供快速回顧，不代表分析框架、正式研究文件或知識庫狀態變更」，避免與 Official 文件語意混淆

## AI Investment HQ 三層架構（角色定義，最新版）
- 三層分工：第一層 GE（Gather Evidence，情報官）：搜尋資料、收集資料、驗證來源、整理資料、去除重複事件、初步資訊分級建議、標註可能影響持股（初判）、建立背景事件、交棒；GE 不做分析、推論、正式判定、投資建議、框架判定、Claude 啟動判定
- 第二層 GPT（G大，策略分析官）：依 AI Investment HQ 正式文件分析、九欄分析、分析框架判定、分析框架更新、家庭投資中心分析、判斷是否需要 Claude 深度研究、正式輸出
- 第三層 Claude（深度研究官）：深度研究、多來源交叉驗證、長篇研究、補充證據、壓力測試、回傳研究結果供 G大採用；Claude 不做最終正式判定，研究結果仍由 G大納入正式分析
- 使用者堅持維持此三層架構與 GE 工作邊界，對 GPT 傾向擴大 GE 工作範圍（例如加入情報分析）持保留態度
- GE 工作邊界調整（最終確認）：去重、分級、關聯到既有背景事件、標註可能影響持股（初判）、判斷新聞屬於哪個既有事件，這些含判斷性質的工作全部歸屬 GPT，不屬於 GE；GE 最終定位為純蒐集端：搜尋資料、收集資料、驗證來源、整理資料（格式化，不含去重分級）、交棒

## 治理紀律新增：範圍擴張控制（2026/07/28）
- 使用者觀察 GPT 反覆出現「範圍自動放大＋自行攬入更多決策權」的模式（GE情報分析擴權、角色定義文件擴張成12-20頁正式治理文件、建議跳過草稿直接發v1.0正式版）
- 新增治理原則：任何新文件／新職權提案，預設先出「最小可行版本」（目錄＋摘要／單頁草案），不預設直接做完整正式版；範圍擴張須經 CIO 明確同意才能升級
- 「啟動 Claude」的決策權保留由使用者（CIO）本人決定，不交給 GPT 自動判斷

## 最高原則：80/20 討論比例（2026/07/28）
- AI投資總部內所有互動（晨報、收盤、晚報、一般分享、任意議題討論、法說會相關內容）均應維持80%投資相關事務／20%治理相關事務的比例；治理討論不得無限擴張排擠投資分析時間，遇重大治理缺口可例外提高治理比例，但處理完應回歸80/20常態
- 此原則暫不收進Governance Framework v1.0（避免再次觸發版本異動流程），獨立存在
- 此80/20原則適用對象為GE、Claude、GPT三個角色，均須遵守

## GitHub 整合（2026/07/28）
- 開始與 GPT 討論建立 GitHub Repository 存放正式文件（Constitution.md、Governance_Framework_v1.0.md、CHANGELOG.md、Portfolio.md），作為 Single Source of Truth，正式版再上傳至 Claude Project 知識庫供分析引用
- Repo 為 a0937568528-code/AI_Investment_HQ，已設為 Public
- 目前 GitHub Repo 內大部分是新建或 0KB 的空檔案，實際內容分散於：Google Drive 暫存資料夾（部分找得到）、手機裡的 md 檔案（尚未整理），檔案狀態目前混亂，搬移工作尚未完成
- 使用者今天在家、明天進公司後會繼續處理搬移，並請 Claude 屆時協助比對 GitHub 上兩台電腦（家用／公司）的同步狀態

## PE（Perplexity Evidence）情報官測試（2026/07/30）
- 決定每天 GE 與 PE（Perplexity）並行試跑情報蒐集，進行對照；目前正式唯一情報來源仍為 GE，PE 尚未正式取代

## 持股水位控制（Decision Layer 延伸，2026/07/31）
- 需求定位：基本面持續看好AI長期發展的前提下，用「長期投資＋右側交易控制水位」的方式管理部位，目標是修正時能降低回吐，但不做每日進出
- 計畫每天提供K線圖與籌碼數據，作為水位判定的輸入

## 角色調整（2026/07/31）
- 核可Claude角色提升為顧問層級，對GPT做的決策可提出否決意見
- 決定採納「GE每日蒐集負擔降低、GE只做例外查證」提案（Daily Intelligence Integration proposal），開始執行落地

## GE功能簡化正式核可（2026/07/31）
- CIO正式核可GE功能簡化定案（先前存在的「已定案」與「未定案」兩份紀錄矛盾，以本次核可為準）
