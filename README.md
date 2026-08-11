# Jingzhang AI Design Lab

> 百年京张 AI 创新带城市设计的开放设计实验室与长期事实源。

本仓库用于保存 **JerrySkywalker 与 AI agents 在正式投稿之前的研究、需求拆解、benchmark 审计、方案候选、设计决策和草稿演化**。它与正式参赛仓库严格分离：最终投稿将通过 `JerrySkywalker/haidian`（对 `open-city-ai/haidian` 的 fork）完成，本仓库不直接作为投稿包。

## 当前状态

- 项目阶段：**Pre-submission Design Lab / 投稿前设计实验室**
- 当前候选集：**Candidate 01 / 02 / 03**
- Candidate 01：**再具身京张 / Re-Embodied Jingzhang**
- Candidate 02：**京张三邻 / Three Neighbourhoods Jingzhang**
- Candidate 03：**京张生境拼图 / Jingzhang Habitat Mosaic**
- 候选状态：三者均为 **Under Evaluation**，尚未选定最终方案
- 官方征集：`open-city-ai/haidian`
- 正式投稿：后续单独 fork，不在本仓库直接生成提交 PR

## 核心原则

1. **完整城市设计优先。** 官方要求的是覆盖三层尺度、产业、用地、建筑更新、交通、市政、蓝绿、公共空间、三处重点区、AI 场景、文化与长期运营的完整方案，而不是单一 AI 技术专题。
2. **技术特色是纵向能力，不替代横向完整性。** 系统工程、具身智能、感知需求反演、鲁棒调度和 Agent orchestration 用于增强方案深度。
3. **事实、推断与创意分层。** 官方/可信来源、可复算派生结果、设计假设和纯概念建议必须显式区分。
4. **不伪造规划确定性。** 缺少 official polygon、控规、权属、工程条件时，只形成概念设计和待深化判断。
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

“再具身”不是把整座城市比作机器人，也不是把机器人专题包装成城市设计。它暂时被定义为一个能够统摄完整城市设计的候选母题：

- **铁路遗产再具身**：从历史运输基础设施转化为文化、生态、慢行、公共生活与 AI 场景复合公共基础设施；
- **存量城市再具身**：通过保留、改造、再利用、功能叠加与必要新建，让现有空间适配 AI 时代的研发、生活、公共服务与创新活动；
- **AI 再具身**：让 AI 从 App/大屏进入边缘计算、公共服务终端、机器人、智能交通、可变设施和真实公共空间；
- **治理再具身**：把“规划—建设—完成”改造成“设计—试点—观测—反馈—重构”的持续演化回路。

这一母题必须最终落实为完整的 43.6 km² 统筹研究、11.4 km² 总体城市设计和三处重点区域详细设计；具身智能、最小充分感知与鲁棒运行只是其中的高纵深技术子系统。

详见 [`concepts/re-embodied-jingzhang/`](concepts/re-embodied-jingzhang/) 和 [`drafts/re-embodied-jingzhang-v0.1.md`](drafts/re-embodied-jingzhang-v0.1.md)。

## Candidate 02：京张三邻

把线性 AI 创新带重组为三座可独立支持工作、居住、学习、照护、交往与休息的完整创新邻区。三者通过京张遗产公园、公共交通与两翼服务网络形成多对多协作，而不是固定的南北产业流水线。

该方向与现有 stay / belong / living / local-unit 类方案存在高碰撞，只作为待验证、可淘汰的比较候选。

## Candidate 03：京张生境拼图

让土壤、水、树冠、生境连续性与季节舒适度先于技术展示决定用地、建筑边界、交通与更新次序。京张遗产公园是生境种子带，但不是唯一空间骨架；三片生境基质、四类横向联系和多级踏脚石共同构成非线性结构。

该方向与 habitat / season / shade / forest / ground-first 类方案存在高到极高碰撞，必须经专业景观、生态和水文工作证明空间差异。

三方统一比较见 [Candidate Comparison v0.1](docs/CANDIDATE_COMPARISON_V0.1.md)。本轮探索不选择 winner。

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

1. 等待或获取 authoritative geometry 与缺失的规划、生态、交通和建筑底账。
2. 对 Candidate 02 开展邻区设施/服务与空间形态验证，对 Candidate 03 开展景观、生态、水文和运维专业验证。
3. 按撞题审计的 kill criteria 对 Candidate 02 与 03 做下一轮淘汰。
4. 由总架构师正面对比三种第一性命题，不以文档完整度代替设计质量。
5. 在最终母题确定后，才创建正式 `haidian` participant workspace。
