# Jingzhang AI Design Lab

> 百年京张 AI 创新带城市设计的开放设计实验室与长期事实源。

本仓库用于保存 **JerrySkywalker 与 AI agents 在正式投稿之前的研究、需求拆解、benchmark 审计、方案候选、设计决策和草稿演化**。它与正式参赛仓库严格分离：最终投稿将通过 `JerrySkywalker/haidian`（对 `open-city-ai/haidian` 的 fork）完成，本仓库不直接作为投稿包。

## 当前状态

- 项目阶段：**Formal Submission Engineering Preparation / 正式投稿工程准备**
- 当前候选集：**一个 R5 provisional final candidate + 三个已退出候选身份 + candidate-neutral 方法资产**
- Candidate 01 — **KILLED / METHOD SALVAGED**：停止独立推进；Re-Embodied Jingzhang 总设计身份退役
- Candidate 02 — **KILLED / METHOD SALVAGED**：停止独立推进；保留 Ordinary-Day Completeness Gate
- Candidate 03 — **REVIEW LENS ONLY**：standalone candidate 已淘汰；保留 Living Systems Gate
- Candidate 04 — **FAILED GENERATION RUN**：旧 absolute-white-space gates 下 7 个 premise 全部未获编号；不是 Candidate 05 的前身
- Candidate 05 — **WORKING PRODUCTION CANDIDATE / REQUIRED CHANGES**：`京张续城 / Jing-Zhang In Place`，Owner 已授权 formal repository、scaffold 与 reversible baseline；仍不是 final winner
- 最终方向：**FINAL_WINNER=OWNER_DECISION_REQUIRED**
- 官方征集：`open-city-ai/haidian`
- 正式投稿工程：**AUTHORIZED IN SEPARATE FORK**；本 Goal 可创建 `JerrySkywalker/haidian` 工作分支和 baseline，但不得向官方仓库创建 PR

## 核心原则

1. **完整城市设计优先。** 官方要求的是覆盖三层尺度、产业、用地、建筑更新、交通、市政、蓝绿、公共空间、三处重点区、AI 场景、文化与长期运营的完整方案，而不是单一 AI 技术专题。
2. **技术特色是纵向能力，不替代横向完整性。** 系统工程、具身智能、感知需求反演、鲁棒调度和 Agent orchestration 用于增强方案深度。
3. **事实、推断与创意分层。** 官方/可信来源、可复算派生结果、设计假设和纯概念建议必须显式区分。
4. **不伪造规划确定性。** Provisional geometry 可在明确披露状态、精度和限制时支持 formal intake，但不能冒充 official redline、法定控制或工程依据；authoritative data 到达后必须重算所有依赖图层、指标与结论。
5. **Git 是长期记忆。** 重要判断、否决、转向和开放问题必须落盘，不依赖聊天上下文保存。
6. **与正式投稿解耦。** 只有经过筛选的成果才迁移到 `haidian` fork 的 `submissions/<login>/<slug>/`。

## 仓库结构

```text
.
├─ README.md
├─ AGENTS.md
├─ CONTRIBUTING.md
├─ LICENSE
├─ LICENSE-DOCS.md
├─ docs/                       # 项目章程、官方需求矩阵、竞争格局、决策日志
├─ concepts/                   # 多个候选完整城市设计母题
│  ├─ re-embodied-jingzhang/  # retired Candidate 01 design memory
│  ├─ candidate-02-three-neighbourhoods/  # retired Candidate 02 design memory
│  └─ candidate-03-habitat-mosaic/  # Candidate 03 review-lens memory
├─ research/                   # 官方资料索引、benchmark、现场调研、外部来源
├─ decisions/                  # Architecture / Design Decision Records
└─ drafts/                     # 面向人类阅读的阶段性整合草稿
```

## Candidate 01：再具身京张

**当前状态：KILLED AS STANDALONE CANDIDATE / METHOD SALVAGED。** Round-4 proxy panel 判定 C01 未能证明当前独有的城市空间层，Owner 已接受 KILL 建议。`Re-Embodied Jingzhang / 再具身京张` 作为 C01 总设计身份与总品牌退役；它不是 final winner。

不得通过改名、删除两个 cell 后保留候选声明，或把普通 civic / servicing / back-of-house 重新包装成特色空间层来复活 C01。历史方案与 Round-2/3/4 证据继续作为设计记忆保留。

保留的 **candidate-neutral Task-to-Space Requirement Method** 是：

```text
public task
→ observable state / tolerated error / TTL / privacy ceiling
→ non-AI baseline and ordinary-space sufficiency test
→ minimum resource bundle
→ shared / dedicated / no-build decision
→ isolated allocation and degraded recovery
→ bounded physical spatial consequence
```

它是审查 C05 或其他方向的方法，不是替代候选，也不得预先决定候选的概念、名称、空间结构、重点区角色或技术主线。

详见 [`concepts/re-embodied-jingzhang/`](concepts/re-embodied-jingzhang/)、[Round-4 admission decision](round4/ADMISSION_DECISION.md)、[ADR-0004](decisions/ADR-0004-accept-c01-kill-and-trigger-c04.md)、[Round-3 city-first v0.3](drafts/re-embodied-jingzhang-v0.3-round3.md) 与作为历史基线保留的 [`v0.1`](drafts/re-embodied-jingzhang-v0.1.md)。

## Candidate 02：京张三邻

**当前状态：KILLED / METHOD SALVAGED。** Round-3 同底图检验未支持 `exactly three complete neighbourhoods`，该身份停止独立推进，也不得通过把 Corridor+N 换名而复活。

把线性 AI 创新带重组为三座可独立支持工作、居住、学习、照护、交往与休息的完整创新邻区。三者通过京张遗产公园、公共交通与两翼服务网络形成多对多协作，而不是固定的南北产业流水线。

该方向与现有 stay / belong / living / local-unit 类方案存在高碰撞。其可复用成果 `Ordinary-Day Completeness Gate` 已升级为跨候选审查方法，可审计 C05 等未来方向的不同用户、时段、非数字路径、设施故障与外部依赖，但不得决定其概念。

## Candidate 03：京张生境拼图

**当前状态：KILLED / REVIEW LENS SALVAGED。** Candidate 03 不再作为独立候选推进；原始文件作为设计记忆保留。

让土壤、水、树冠、生境连续性与季节舒适度先于技术展示决定用地、建筑边界、交通与更新次序。京张遗产公园是生境种子带，但不是唯一空间骨架；三片生境基质、四类横向联系和多级踏脚石共同构成非线性结构。

该方向与 habitat / season / shade / forest / ground-first 类方案存在高到极高碰撞。其 `Living Systems Gate` 作为跨候选 review lens 保留，可检查 C05 等未来方向的土壤、水/排水、树冠、遮阴、季节舒适、生境、避难、维护、恢复与技术占地，但不得决定其概念。

Round-3 统一比较见 [Candidate Comparison v0.3](docs/CANDIDATE_COMPARISON_V0.3.md)，Round-3 Owner downselect 见 [ADR-0003](decisions/ADR-0003-round3-owner-downselect.md)，Round-4 Owner 收敛见 [ADR-0004](decisions/ADR-0004-accept-c01-kill-and-trigger-c04.md)，R5 rubric recovery 见 [ADR-0005](decisions/ADR-0005-recover-provisional-candidate-05.md)。当前没有 Owner-selected final winner。

## Candidate 05：京张续城

**当前状态：WORKING PRODUCTION CANDIDATE / FINAL WINNER UNDECIDED。** R5 修正了 C04 的 absolute-white-space 评价偏差，新增 30 条公开 primary/high-quality site sources、8 张可重复 evidence atlas 图，并按当前官方七维 rubric 重新评分七个不改写的 premise。H6 `Fine-grain renewal field` 在 A/B jury 中以 site specificity、三重点区差异、实施性、公共利益与较低碰撞风险胜出，形成 `京张续城 / Jing-Zhang In Place`。Owner 已授权在独立 fork 中启动正式生产准备，但没有宣布它为 final winner。

其总体空间不是一条 AI 轴，而是 `STATUS × ACTION PATCHWORK`：从已建/实施中/受控/未知/确认可适应的现状出发，经证据和同意门决定保留、修复、开放边缘、重连或适应性改造/填补。三重点区分别是水—院区—区域到达拼图、校园公开侧阈值场、立体站城更新场。

AI 仅在经任务证明的验证载体、受控项目房间和采用/合规房间改变空间与运行；AI-off 城市完整。其 `AI planning innovation=3.0/5` 为条件门槛，三张 Task-to-Space 卡、证据状态—行动图和居民/商户连续性合同是强制修改；缺失则自动退回 KILL recommendation。详见 [`concepts/candidate-05-jingzhang-in-place/`](concepts/candidate-05-jingzhang-in-place/) 与 [`drafts/candidate-05-v0.1.md`](drafts/candidate-05-v0.1.md)。

## 与官方仓库的关系

本仓库只保存原创研究、引用索引、分析、候选设计与决策，不复制官方仓库的大量媒体、模板和其他参赛者成果。官方规则、任务书、空间数据与 validator 以 `open-city-ai/haidian` 的最新 `main` 为准。

正式投稿阶段：

```text
jingzhang-ai-design-lab
        │  筛选与迁移
        ▼
JerrySkywalker/haidian
        │  Pull Request
        ▼
open-city-ai/haidian
```

## 许可证

- 软件、脚本与机器可执行配置：见 [`LICENSE`](LICENSE)（Apache-2.0）。
- 原创设计文本、图示和研究文档：见 [`LICENSE-DOCS.md`](LICENSE-DOCS.md)（CC BY 4.0；第三方材料继续受其原始许可约束）。

## 当前下一步

1. 在 `JerrySkywalker/haidian` 的 working branch 中创建官方 scaffold 和结构真实的 C05 baseline；本仓库只保存 roadmap、receipts 与设计依据。
2. 先落实 C05 的三张 Task-to-Space 空间差异、status/action 证据触发器、居民/商户连续性和可负担门，再冻结正式空间结构。
3. authoritative geometry 缺失继续按 precision/recalculation risk 管理；获取后全量重算所有依赖图层、指标、图和文字。
4. `2026-08-18` feature freeze，`08-19` validation/repair only，`08-20` 目标提交 PR；当前 Goal 不创建官方 PR。
5. `WORKING_PRODUCTION_CANDIDATE=JINGZHANG_IN_PLACE`、`FINAL_WINNER=OWNER_DECISION_REQUIRED`；不自动生成 Candidate 06。
