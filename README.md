# Jingzhang AI Design Lab

> 百年京张 AI 创新带城市设计的开放设计实验室与长期事实源。

本仓库用于保存 **JerrySkywalker 与 AI agents 在正式投稿之前的研究、需求拆解、benchmark 审计、方案候选、设计决策和草稿演化**。它与正式参赛仓库严格分离：最终投稿将通过 `JerrySkywalker/haidian`（对 `open-city-ai/haidian` 的 fork）完成，本仓库不直接作为投稿包。

## 当前状态

- 项目阶段：**Pre-submission Design Lab / 投稿前设计实验室**
- 当前候选集：**一个 surviving provisional candidate + 两个已淘汰候选的方法资产**
- Candidate 01 — **ACTIVE / PROFESSIONAL ADMISSION**：当前唯一 surviving provisional candidate；尚非 final winner
- Candidate 02 — **KILLED / METHOD SALVAGED**：停止独立推进；保留 Ordinary-Day Completeness Gate
- Candidate 03 — **KILLED / REVIEW LENS SALVAGED**：停止独立推进；保留 Living Systems Gate
- Candidate 04 — **NOT TRIGGERED**：仅当 C01 未通过下一轮专业空间准入时触发建议
- 品牌状态：**Re-Embodied Jingzhang 总品牌未锁定**；re-embodiment 技术子系统暂时保留
- 官方征集：`open-city-ai/haidian`
- 正式投稿：**NOT YET**；后续经 Owner 授权后使用单独 fork，不在本仓库直接生成提交 PR

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
│  ├─ re-embodied-jingzhang/  # Candidate 01
│  ├─ candidate-02-three-neighbourhoods/
│  └─ candidate-03-habitat-mosaic/
├─ research/                   # 官方资料索引、benchmark、现场调研、外部来源
├─ decisions/                  # Architecture / Design Decision Records
└─ drafts/                     # 面向人类阅读的阶段性整合草稿
```

## Candidate 01：再具身京张

**当前状态：ACTIVE / PROFESSIONAL ADMISSION。** C01 是唯一 surviving provisional candidate，但不是 final winner；它仍可在 Round 4 被淘汰。总城市品牌尚未锁定，“再具身”暂作为技术子系统保留。

Round 3 后不再预设“再具身”必须成为统摄全部城市设计的总品牌。当前 surviving direction 从城市问题出发：以普通公共地面、横向城市缝合、三个不等的城市界面和存量更新形成完整城市结构；技术层只有在公共任务反演证明必要时才进入空间。

暂时保留的 **re-embodiment technical subsystem** 是：

```text
public task
→ observable state / uncertainty / TTL
→ minimum resource bundle
→ shared / dedicated / no-build decision
→ isolated allocation and degraded recovery
→ bounded physical spatial consequence
```

它不是机器人走廊、通用“再具身站”或独立用地类别，也不是最终公共品牌。C01 仍须以完整的 43.6 km² 统筹研究、11.4 km² 总体城市设计和三处重点区域详细设计通过 Round-4 专业空间准入。

详见 [`concepts/re-embodied-jingzhang/`](concepts/re-embodied-jingzhang/)、[Round-3 city-first v0.3](drafts/re-embodied-jingzhang-v0.3-round3.md) 与作为历史基线保留的 [`v0.1`](drafts/re-embodied-jingzhang-v0.1.md)。

## Candidate 02：京张三邻

**当前状态：KILLED / METHOD SALVAGED。** Round-3 同底图检验未支持 `exactly three complete neighbourhoods`，该身份停止独立推进，也不得通过把 Corridor+N 换名而复活。

把线性 AI 创新带重组为三座可独立支持工作、居住、学习、照护、交往与休息的完整创新邻区。三者通过京张遗产公园、公共交通与两翼服务网络形成多对多协作，而不是固定的南北产业流水线。

该方向与现有 stay / belong / living / local-unit 类方案存在高碰撞。其可复用成果 `Ordinary-Day Completeness Gate` 已升级为跨候选审查方法，继续审计 C01 的不同用户、时段、非数字路径、设施故障与外部依赖。

## Candidate 03：京张生境拼图

**当前状态：KILLED / REVIEW LENS SALVAGED。** Candidate 03 不再作为独立候选推进；原始文件作为设计记忆保留。

让土壤、水、树冠、生境连续性与季节舒适度先于技术展示决定用地、建筑边界、交通与更新次序。京张遗产公园是生境种子带，但不是唯一空间骨架；三片生境基质、四类横向联系和多级踏脚石共同构成非线性结构。

该方向与 habitat / season / shade / forest / ground-first 类方案存在高到极高碰撞。其 `Living Systems Gate` 作为跨候选 review lens 保留，继续检查 C01 的土壤、水/排水、树冠、遮阴、季节舒适、生境、避难、维护、恢复与技术占地。

Round-3 统一比较见 [Candidate Comparison v0.3](docs/CANDIDATE_COMPARISON_V0.3.md)，Owner downselect 见 [ADR-0003](decisions/ADR-0003-round3-owner-downselect.md)。C01 仍不是 final winner。

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

1. 以三张差异化 section 为核心，对 C01 开展 **Round-4 Professional Spatial Admission**；专业结论可以淘汰 C01。
2. 用 Ordinary-Day Completeness Gate 与 Living Systems Gate 同时审 C01，不把被淘汰候选的空间结构并入 C01。
3. 取得或核验必要的规划、交通、建筑、景观和现场证据；authoritative geometry 缺失按 precision/recalculation risk 管理，而不是绝对 fork blocker。
4. C01 通过专业空间准入后，再由 Owner 锁定或否决总城市方向与公共品牌。
5. 只有 C01 下一关失败才触发 Candidate 04 建议；在 `OWNER_FINAL_DIRECTION` 与 `C01_SPATIAL_ADMISSION` 关闭前不创建正式 fork。
