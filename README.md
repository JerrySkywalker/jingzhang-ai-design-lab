# Jingzhang AI Design Lab

> 百年京张 AI 创新带城市设计的开放设计实验室与长期事实源。

本仓库用于保存 **JerrySkywalker 与 AI agents 在正式投稿之前的研究、需求拆解、benchmark 审计、方案候选、设计决策和草稿演化**。它与正式参赛仓库严格分离：最终投稿将通过 `JerrySkywalker/haidian`（对 `open-city-ai/haidian` 的 fork）完成，本仓库不直接作为投稿包。

## 当前状态

- 项目阶段：**Pre-submission Design Lab / 投稿前设计实验室**
- 当前候选母题：**Candidate 01 — 再具身京张 / Re-Embodied Jingzhang**
- 候选状态：**Under Evaluation**，尚未选定为最终方案
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
│  └─ re-embodied-jingzhang/  # Candidate 01
├─ research/                   # 官方资料索引、benchmark、现场调研、外部来源
├─ decisions/                  # Architecture / Design Decision Records
└─ drafts/                     # 面向人类阅读的阶段性整合草稿
```

## 当前候选：再具身京张

“再具身”不是把整座城市比作机器人，也不是把机器人专题包装成城市设计。它暂时被定义为一个能够统摄完整城市设计的候选母题：

- **铁路遗产再具身**：从历史运输基础设施转化为文化、生态、慢行、公共生活与 AI 场景复合公共基础设施；
- **存量城市再具身**：通过保留、改造、再利用、功能叠加与必要新建，让现有空间适配 AI 时代的研发、生活、公共服务与创新活动；
- **AI 再具身**：让 AI 从 App/大屏进入边缘计算、公共服务终端、机器人、智能交通、可变设施和真实公共空间；
- **治理再具身**：把“规划—建设—完成”改造成“设计—试点—观测—反馈—重构”的持续演化回路。

这一母题必须最终落实为完整的 43.6 km² 统筹研究、11.4 km² 总体城市设计和三处重点区域详细设计；具身智能、最小充分感知与鲁棒运行只是其中的高纵深技术子系统。

详见 [`concepts/re-embodied-jingzhang/`](concepts/re-embodied-jingzhang/) 和 [`drafts/re-embodied-jingzhang-v0.1.md`](drafts/re-embodied-jingzhang-v0.1.md)。

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

1. 固化官方 Requirement Matrix。
2. 继续比较成熟 benchmark 对每个必答项的处理方式。
3. 至少提出 2 个与“再具身京张”明显不同的完整城市设计母题。
4. 对 Candidate 01 做空间、产业、城市更新、交通蓝绿、重点区、文化运营和技术子系统的逐项反证。
5. 在最终母题确定后，才创建正式 `haidian` participant workspace。
