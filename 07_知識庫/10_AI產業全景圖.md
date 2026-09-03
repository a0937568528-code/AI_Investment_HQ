# 07_AI產業全景圖.md（AI Ecosystem Map）

> **Status:** Official Knowledge Map（v1.3，Commit 1、Commit 2 均已完成，判準文字已精確化）
> **Version:** v1.3
> **Effective date:** 2026-07-27
> **Owner:** AI Investment HQ
> **依循規範：** 本文件之知識結構完全依《AI_Investment_HQ_知識模型治理規範.md》v1.0 組織，若本文件內容與該規範衝突，以規範為準。

---

## Chapter 1｜文件使命

本文件旨在描述 AI 生態系的長期拓樸結構（Topology），而非市場競爭、公司排名、產品世代或短期商業狀態。所有內容均依《AI Investment HQ 知識模型治理規範》組織；若與其他研究文件內容有差異，以各研究文件的專業分析為準。

本文件維護 AI 生態系之長期知識結構（Knowledge Topology），不維護市場狀態、競爭態勢、產品世代、財務數據或短期事件。當前狀態一律引用 `04_AI基礎建設投資分析.md`（公司研究）、`06_AI供應鏈關聯公司清單.md`（持股驗證）、`03_AI基本面追蹤框架.md`（框架判定）。

**自我檢驗機制：** 若本文件需要頻繁更新才能反映最新資訊，即為設計失敗之訊號，應回頭檢視是否誤將 Technical Instantiation 以下的產品／財務層級內容寫入本文件。

**引用方向：** `04`、`06` 引用 `07`；`07` 不引用 `04`、`06`。**07 不引用任何研究結論，只定義知識位置。** 本文件之預期更新頻率應為 AI Investment HQ 全部研究文件中最低者（參考知識模型治理規範第五章 Knowledge Health Indicator）。

---

## Chapter 2｜AI 生態系五層架構

AI 生態系依「越上游越穩定、越下游越易變動」之原則，劃分為五層：

| 層級 | 定義 | 生命週期預期 |
|---|---|---|
| **材料設備層** | 支撐晶片與硬體製造之上游材料、設備與設計工具 | 最穩定，5 年以上不易變動 |
| **運算硬體層** | 將材料設備轉化為 AI 運算能力之晶片、記憶體與封裝技術 | 穩定，技術路線更替以數年為單位 |
| **基礎設施層** | 將運算硬體組裝為可運行 AI 工作負載之系統與服務，含雲端服務供應商 | 中度穩定，新進入者可能出現但既有玩家更替較慢 |
| **模型層** | 提供基礎模型與智能能力之研發與訓練 | 變動較快，領先者可能於數年內洗牌 |
| **應用層** | 將模型能力整合為終端可用之產品與服務 | 變動最快，新應用持續湧現 |

**特殊說明：** 部分節點（如雲端服務供應商）同時具備多重角色（基礎設施提供者、大量採購方、資本投資方），其分類依《知識模型治理規範》第三章 Connection Standard 以多重連結類型表達，不因此拆分為多個節點。

---

## Chapter 3｜Capability Taxonomy（能力分類體系）

依 Chapter 2 五層架構，建立各層之 Capability Node。所有 Node 均為功能性描述，不使用公司名稱、產品型號或技術品牌（依《知識模型治理規範》第二章 Node Naming Standard）。

### 材料設備層
- 晶圓製造設備能力
- 特殊材料供給能力（矽晶圓、化學品、氣體、CMP／過濾／晶圓搬運耗材）
- 晶片設計工具能力（EDA／IP 授權）

### 運算硬體層
- AI 運算能力（涵蓋通用加速與客製化加速兩種技術路線）
- 高頻寬記憶體能力
- 標準與利基型記憶體能力
- 晶圓代工能力
- 先進封裝能力

### 基礎設施層
- 伺服器系統整合能力
- 網路互連能力（含光通訊）
- 電源與散熱管理能力
- 雲端基礎設施能力

### 模型層
- 基礎模型能力（Foundation Model Capability）

### 應用層
- 企業軟體整合能力
- 垂直領域應用能力
- 消費端應用能力

**備註：** 本清單為 Capability Node 之頂層分類，各節點下之 Technical Instantiation（如「AI 運算能力」下之 GPU、ASIC）收錄於 Chapter 6 Representative Mapping，不在本章重複列出，以維持 Node 與 Instantiation 兩層之分離（依知識模型治理規範第二章）。

---

## Chapter 4｜Layer Relationship（層級關係）

五層之間存在雙向動態，非單純線性上下游：

```
材料設備層 → 運算硬體層 → 基礎設施層 → 模型層 → 應用層
```

**主要驅動方向（Tech／Val 連結為主）：** 材料設備支撐運算硬體製造；運算硬體組裝為基礎設施；基礎設施承載模型訓練與服務；模型能力交付應用層。

**反向影響（Biz／Cap 連結為主）：** 應用層與模型層之需求規模，回頭驅動基礎設施層（雲端服務供應商）擴大採購運算硬體，進而帶動材料設備層擴產。此雙向動態為結構性事實，其對長期投資判斷之意義與具體判定邏輯，依 `03_AI基本面追蹤框架.md` 之研究內容為準，本文件不重複闡述。

**跨層雙重角色節點：** 雲端基礎設施能力（基礎設施層）之代表案例（如 Microsoft、Google、Amazon），同時對運算硬體層構成「商業依賴」連結（大量採購方），並可能對模型層構成「資本合作」連結（投資模型公司）。此類節點不因跨層角色而拆分為多個 Node，依《知識模型治理規範》第三章以多重 Connection 類型完整表達。

---

## Chapter 5｜AI Ecosystem Topology（節點關係圖）

依《知識模型治理規範》第四章 Projection Standard，本章提供 Technology View（技術依賴關係）作為初版 Projection；Business View、Capital View、Value Flow View 待實際治理需求出現時再行補充，不預先填滿。

```
【材料設備層】
晶圓製造設備能力 ──Tech──→ 晶圓代工能力
特殊材料供給能力 ──Tech──→ 晶圓代工能力
晶片設計工具能力 ──Tech──→ AI運算能力

【運算硬體層】
晶圓代工能力 ──Tech──→ AI運算能力
晶圓代工能力 ──Tech──→ 先進封裝能力
高頻寬記憶體能力 ──Tech──→ AI運算能力（訓練用途）
標準與利基型記憶體能力 ──Tech──→ 基礎設施層（伺服器系統整合能力）
先進封裝能力 ──Tech──→ AI運算能力（產出完整運算模組）

【基礎設施層】
AI運算能力 ──Tech──→ 伺服器系統整合能力
網路互連能力 ──Tech──→ 伺服器系統整合能力
電源與散熱管理能力 ──Tech──→ 伺服器系統整合能力
伺服器系統整合能力 ──Tech──→ 雲端基礎設施能力

【模型層】
雲端基礎設施能力 ──Val──→ 基礎模型能力（提供訓練與推論算力）

【應用層】
基礎模型能力 ──Val──→ 企業軟體整合能力
基礎模型能力 ──Val──→ 垂直領域應用能力
基礎模型能力 ──Val──→ 消費端應用能力
```

**跨層額外連結（非單純技術依賴，列示以完整呈現生態系全貌，不納入本 Technology View 主圖）：**
- 雲端基礎設施能力 ──Biz──→ AI運算能力（大量採購方角色）
- 雲端基礎設施能力 ──Cap──→ 基礎模型能力（部分代表案例存在資本投資關係）

**多重 Capability Node 代表案例說明：** 部分代表公司同時為多個 Capability Node 之 Representative（例如 NVIDIA 同時代表「AI運算能力」與「網路互連能力」；台積電同時代表「晶圓代工能力」與「先進封裝能力」；Google／Amazon／Microsoft 同時代表「雲端基礎設施能力」與「AI運算能力」之 ASIC 路線）。此為知識模型治理規範第六章壓力測試已驗證之正常情況，不因此需要拆分節點或新增 Node。

---

## Chapter 6｜Representative Mapping（代表案例對照）

**Representative Mapping 原則：** Representative Mapping 之目的在於展示各 Capability Node 的代表性實現，而非建立完整公司資料庫。原則上每個 Capability Node 維持約 5–10 家具長期代表性的公司；除非 AI 生態系出現結構性變化，否則不因短期市場熱度、新創公司興衰或產品世代更替而頻繁調整 Representative 清單。新興公司（如市占尚小之新創加速器廠商）於已證明具備長期 Capability 代表性前，暫不納入，可於觀察後再行收錄。

**Knowledge Coverage Policy（知識涵蓋範圍政策）：** 本文件採用**方案 B：全球公開市場導向（Global Public Market Coverage）**——Representative Mapping 原則上收錄具有全球代表性之公開上市公司，作為 Capability Node 的 Representative。

**核心判準（避免未來誤用地區作為收錄依據）：** Representative Mapping 之收錄依據為**公開市場代表性與可驗證性**，不以公司所屬國家或地區作為判準。

具體原則：
- 收錄判準為「是否為公開上市公司且具全球代表性」，**判準為公開市場地位，不是地區**。日本、韓國、歐洲等地區之公開上市代表公司（如 Tokyo Electron、Disco、Advantest、Shin-Etsu 等），若確實為所屬 Capability Node 之全球公開市場重要代表，應予納入，不因地區而排除。
- 非公開發行、資訊揭露透明度不足以支持 Evidence First 原則（如無法取得可驗證財報、法說）之企業，除經正式治理決議外，不納入 Representative Mapping；此類公司不論其產業地位或所屬地區為何，均依此一致判準處理，不因特定地區而系統性排除或系統性收錄。
- 本政策之目的在於維持 07 之知識完整性（涵蓋全球主要公開市場代表公司）、治理穩定性（收錄判準明確，不因新增公司而重新討論邊界）與維護成本（避免演變為無上限之公司名錄），並維持與 04（公司研究）、06（持股映射）之職責分離——07 定義知識結構，不隨 Portfolio 或市場熱度變動而調整收錄範圍。
- 本政策為 Commit 2 治理決策之正式結論（相對於方案 A「全球完整生態」與方案 C「投資研究導向」），一經確立即為 07 及未來知識地圖類文件之預設收錄政策，如需變更，依《知識模型治理規範》第六章 Version Governance 之 RFC 流程處理。

各 Capability Node 下之 Technical Instantiation 與代表公司，僅列名，不展開財務或時效性內容。詳細公司研究一律引用 `04_AI基礎建設投資分析.md`；持股驗證關聯一律引用 `06_AI供應鏈關聯公司清單.md`。

### 材料設備層
| Capability Node | Technical Instantiation | 代表公司 |
|---|---|---|
| 晶圓製造設備能力 | 微影設備／蝕刻沉積設備／量測設備 | ASML、Applied Materials、Lam Research、東京威力科創、KLA、迪思科（Disco）、愛德萬測試（Advantest） [→見04] |
| 特殊材料供給能力 | 矽晶圓／特殊氣體化學品／CMP與過濾耗材 | 信越化學、SUMCO、環球晶、Linde、Air Liquide、Entegris [→見04] |
| 晶片設計工具能力 | EDA軟體／CPU架構IP | Synopsys、Cadence、Arm [→見04] |

### 運算硬體層
| Capability Node | Technical Instantiation | 代表公司 |
|---|---|---|
| AI運算能力 | GPU（通用加速）／ASIC（客製化加速） | NVIDIA、AMD、Broadcom、Marvell、Qualcomm、MediaTek、Google、Amazon、Microsoft（Google／Amazon／Microsoft 為自研 ASIC 路線之代表公司，具體產品屬 Technical Instantiation 以下之產品層，不於本文件收錄）[→見04][→見06] |
| 高頻寬記憶體能力 | HBM | SK hynix、Samsung、Micron [→見04][→見06] |
| 標準與利基型記憶體能力 | 標準型DRAM／利基型DRAM／NOR Flash | 長鑫科技（標準型）、華邦電、旺宏（利基型）[→見04][→見06] |
| 晶圓代工能力 | 先進製程代工 | 台積電、三星、Intel Foundry [→見04][→見06] |
| 先進封裝能力 | CoWoS／載板／玻璃基板等技術實現 | 台積電、日月光投控、欣興、南電、景碩 [→見04][→見06] |

### 基礎設施層
| Capability Node | Technical Instantiation | 代表公司 |
|---|---|---|
| 伺服器系統整合能力 | ODM代工／品牌伺服器 | 廣達、緯創、緯穎、Super Micro、Dell、HPE、Lenovo [→見04] |
| 網路互連能力 | 交換器／光通訊元件／高速網路架構 | Arista、Cisco、穩懋、Coherent、NVIDIA（Spectrum／InfiniBand 網路架構）、Ciena、Lumentum [→見04][→見06] |
| 電源與散熱管理能力 | 電源系統／液冷散熱 | Vertiv、台達電、奇鋐、雙鴻 [→見04] |
| 雲端基礎設施能力 | Hyperscaler | Microsoft、Google、Amazon、Meta、Oracle [→見04][→見06] |

### 模型層
| Capability Node | Technical Instantiation | 代表公司 |
|---|---|---|
| 基礎模型能力 | 封閉模型／開源模型 | OpenAI、Anthropic、Google DeepMind、xAI、Meta（開源路線代表）[→見04] |

### 應用層
| Capability Node | Technical Instantiation | 代表公司 |
|---|---|---|
| 企業軟體整合能力 | AI輔助辦公／企業流程整合 | Microsoft（Copilot）、Salesforce（Agentforce）[→見04] |
| 垂直領域應用能力 | 政府/國防數據、企業流程 | Palantir、ServiceNow [→見04] |
| 消費端應用能力 | 對話助手／AI搜尋 | 各類消費端產品（依當期市場狀態，一律見04） |

---

## Chapter 7｜與其他研究文件的關係

| 文件 | 與本文件之關係 |
|---|---|
| `04_AI基礎建設投資分析.md` | 引用本文件之 Capability Node 作為公司研究分類依據；不得於本文件重複填入 04 之研究內容 |
| `05_台股市場籌碼分析.md` | 不隸屬本文件之知識分支（Market Knowledge 獨立分支），無直接引用關係 |
| `06_AI供應鏈關聯公司清單.md` | 引用本文件之節點結構，作為持股驗證錨點之上游依據 |
| `03_AI基本面追蹤框架.md` | 不直接引用本文件；框架判定規則獨立運作，本文件僅提供背景拓樸知識 |
| `AI_Investment_HQ_知識模型治理規範.md` | 本文件之 Schema 依據，本文件不得逕自變更節點命名、連結分類或更新規則，如需調整須依該規範第六章 RFC 流程處理 |

---

## Chapter 8｜維護原則

1. 新增 Technical Instantiation（如新技術、新代表公司）：日常維護，可隨時更新，無需觸發架構討論。
2. 新增或調整 Capability Node、Connection 類型：屬架構變更，須依《知識模型治理規範》第六章 Version Governance 流程處理，不得於本文件內逕自新增。
3. 每次更新須檢查是否符合 Node Naming Standard（無公司名稱、產品型號、技術品牌作為 Node）。
4. 本文件版本紀錄獨立於 Constitution 與 CHANGELOG 之外部版本號管理，但重大版本（如 v1.0 首次發布）須同步登錄 `CHANGELOG.md`。

---

## 版本紀錄

| Version | Date | Change |
|---|---|---|
| v0.1 | 2026-07-27 | Phase 1：建立文件骨架（八章節結構），內容待 Phase 2 填充。依《知識模型治理規範》v1.0 與五案例壓力測試結果組織章節架構。 |
| v0.2 | 2026-07-27 | Phase 2：完成內容填充（Chapter 2-6），包含五層架構定義、Capability Taxonomy、Layer Relationship、Technology View 拓樸圖、Representative Mapping。納入 Design Review 四點修正（定位語句、Chapter 3 更名為 Capability Taxonomy、Chapter 5 不預先指定特定 Projection、Chapter 1 補充「不引用研究結論」原則）。待 Phase 3 一致性檢查（Schema Compliance Review）後正式發布 v1.0。 |
| v1.0 | 2026-07-27 | Phase 3：完成一致性檢查。發現並修正一處違規——Chapter 4 原引用 `03_AI基本面追蹤框架.md` 之具體判定邏輯與研究結論，違反 Chapter 1「07 不引用任何研究結論，只定義知識位置」原則，已修正為純結構性描述並改為引用 03 而非闡述其內容。全文重新掃描確認：無公司名稱作為 Node、無產品型號或技術品牌作為 Node、Node 與 Instantiation 兩層分離完整、無財務或時效性內容混入。正式發布 v1.0，同步登錄 `CHANGELOG.md`。 |
| v1.1 | 2026-07-27 | Commit 1（無爭議公司補充，經三方審查後採納）：Chapter 3／Chapter 6 新增 Entegris（特殊材料供給能力）、Qualcomm／MediaTek（AI運算能力）、NVIDIA（新增為網路互連能力代表，驗證多重 Capability Node 代表之正常情況）、Ciena／Lumentum（網路互連能力）、Lenovo（伺服器系統整合能力）；AI運算能力新增 Google／Amazon／Microsoft 作為自研 ASIC 路線代表公司（不收錄 TPU／Trainium／Maia 等產品名稱，以符合 Node 不含產品層之規範）。新增「Representative Mapping 原則」（每 Capability Node 維持 5–10 家長期代表公司，不因短期熱度或新創興衰頻繁調整）至 Chapter 6 開頭。Commit 2（中國／日本供應鏈是否納入、Knowledge Coverage Policy 之確立）留待使用者另行決策，本次不處理。 |
| v1.2 | 2026-07-27 | Commit 2（使用者決策確立，經三方審查修正政策定義精確度）：正式採用**方案 B：全球公開市場導向（Global Public Market Coverage）**作為 Knowledge Coverage Policy，寫入 Chapter 6。**收錄判準為「公開市場地位」，不是「地區」**——日本、韓國、歐洲等地區之公開上市代表公司應與其他地區公司採一致判準評估，不因地區而系統性排除或系統性收錄。依此判準，晶圓製造設備能力新增迪思科（Disco）、愛德萬測試（Advantest）等日本公開市場代表公司。原 v1.1 之政策文字曾將「日本供應鏈」與「中國供應鏈」混為一談列為同一類待決事項，經修正後明確：日本之公開上市代表公司依方案 B 判準應予收錄，非公開發行或資訊揭露不足之企業（不限特定地區）方為排除對象。本政策為預設收錄政策，變更須依知識模型治理規範 RFC 流程處理。 |
| v1.3 | 2026-07-27 | 判準精確化（非治理方向改變）：於 Knowledge Coverage Policy 開頭新增核心判準句——「Representative Mapping 之收錄依據為公開市場代表性與可驗證性，不以公司所屬國家或地區作為判準」，將公開市場、可驗證資訊、Representative Mapping 三者一次綁定，避免未來協作者以地區（如「日本」「中國」「美國」）作為收錄邏輯之思考起點。本次修正屬 07 文件內部文字精確化，不涉及 Constitution 或知識模型治理規範之上位規則調整。 |
