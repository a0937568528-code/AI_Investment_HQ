# AI Investment HQ｜AI 供應鏈關聯公司清單（Supply Chain Coverage Universe）

> **Status:** Official Research Document
> **Version:** v1.0
> **Effective date:** 2026-07-27
> **Owner:** AI Investment HQ
> **更新頻率：** 原則上每季（3 個月）檢視一次，如遇重大供應鏈結構性變化（如新增／剔除關鍵供應商、持股標的變更）可提前更新，並登錄 `CHANGELOG.md`。

---

## 一、目的

供應鏈關聯公司並非新增投資標的，其唯一用途為：

> 提供家庭投資中心正式持股之支持性證據與交叉驗證。

不得因供應鏈關聯公司本身表現優異，即直接形成投資建議。所有正式操作仍以家庭投資中心持股為核心，關聯公司之表現一律定位為**背景事件**，不得因其優異表現直接升級家庭投資中心持股之分析框架狀態。

---

## 二、分析原則

Daily War Room、重大事件分析與 Claude 深度研究，除正式持股外，同步追蹤本文件所列公司。

研究結果須明確指出：**此事件主要支持哪一檔正式持股。**

不得僅寫「AI 供應鏈利多」，須寫成具體因果連結，例如：

> 欣銓 ASIC 測試放量 → 支持欣興 ABF／AI 載板需求延續

若無法直接連結正式持股，應標示：**主要影響持股：無**，不得勉強建立關聯。

**分類邏輯提醒：** 本文件對個股（欣興、華邦電）採「第一層直接驗證公司／第二層需求來源／第三層終端需求」之供應鏈驗證層級分類；對 ETF（00991A／00981A／00988A／00997A）則採產業角色分類（GPU／ASIC／HBM／CoWoS 等）。兩套分類邏輯彼此獨立，不可混用或視為同一分層定義。此分類與 AI 基本面追蹤框架之「第一層領先／第二層供應鏈確認／第三層驗證」為不同體系，兩者對應關係須個案判斷，不預設等同。

---

## 三、正式持股對應供應鏈

### （一）3037 欣興

**第一層（直接驗證公司）** — ABF／先進封裝／AI 載板
南電、景碩、欣銓、京元電子、日月光投控

用途：驗證 AI 載板需求、ABF 利用率、CoWoS 需求、ASIC 測試需求、HPC 出貨

**第二層（需求來源）**
台積電、NVIDIA、Broadcom、Marvell、AMD

用途：驗證 ASIC、GPU、CoWoS、HPC 需求

**第三層（終端需求）**
Microsoft、Google、Meta、Amazon、Oracle

用途：驗證 AI 資料中心 CapEx

---

### （二）2344 華邦電

**第一層（直接驗證）**
旺宏、力積電、南亞科、Micron、SK hynix、Samsung

用途：驗證利基型 DRAM、NOR Flash、記憶體景氣、Edge AI
**提醒：** 依 AI 基本面追蹤框架既有原則，華邦電主力為利基型 DRAM／NOR Flash，不可直接以 HBM 價格或供需推論其基本面，須確認是否真正傳導至其產品線。

**第二層（需求來源）**
NVIDIA、AMD、Qualcomm、MediaTek

用途：驗證 AI PC、AI Edge、AI MCU

**第三層（終端）**
Microsoft、Dell、HP、Lenovo

用途：驗證 AI PC 需求

---

### （三）00991A

ETF 持股分散，採 AI Infrastructure Framework，追蹤：GPU、ASIC、HBM、CoWoS、ABF、Networking、Optical、Server、Cloud、Equipment

重點公司：NVIDIA、Broadcom、Marvell、台積電、Micron、SK hynix、ASML、Applied Materials、Lam Research、KLA、Arista、Cisco、Dell、HPE

---

### （四）00981A

追蹤大型 AI 平台：Microsoft、Google、Meta、Amazon、Oracle，加上台積電

---

### （五）00988A

全球 AI 供應鏈：NVIDIA、Broadcom、AMD、Micron、SK hynix、台積電、ASML

---

### （六）00997A

重點：Cloud、AI Service、Hyperscaler

追蹤：Microsoft、Google、Meta、Amazon、Oracle、OpenAI、Anthropic、xAI

---

## 四、研究輸出要求

引用本文件進行供應鏈公司研究時，須新增固定欄位：

**主要影響持股：**

範例：
- 欣銓 → 欣興
- 京元電子 → 欣興、00991A
- Broadcom → 00991A、00988A
- Micron → 華邦電（需區分產品線）、00991A
- 台積電 → 欣興、00991A、00981A
- NVIDIA → 00991A、00988A

若無法連結任何正式持股，標示「主要影響持股：無」。

---

## 五、與其他正式文件之關係

- 本文件之公司清單僅作為**背景事件證據來源之範圍界定**，不改變 Constitution v1.1.0 第 8 章對九欄格式、資訊分級（Daily_War_Room_SOP.md）之定義。
- 本文件所列公司若非正式持股，其相關資訊依 Daily_War_Room_SOP.md 資訊分級原則，原則上定位為**背景事件**，除非另有官方來源使其符合框架級情報判準。
- 家庭投資中心（Portfolio.md）之正式持股清單如有變動，本文件對應章節須同步檢視更新。

---

## 六、版本紀錄

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-07-27 | 建立本文件，收錄六個正式持股（欣興、華邦電、00991A、00981A、00988A、00997A）對應之供應鏈關聯公司清單。 |
