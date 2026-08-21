# Anchor Packet Reproducibility Audit

Every anchor packet was built twice independently from clean inputs (`Packets Run 1` vs `Packets Run 2 Clean Rebuild`).
Determinism requirement: Identical file list, identical per-file SHA-256, and identical overall packet hash.

## Reproducibility Verification Table

| Neutral ID | Role | Official Score | Exact Source Head | File Count | Run 1 Packet Hash | Run 2 Packet Hash | Hash Identical | Status |
|---|---|---:|---|---:|---|---|:---:|:---:|
| `N4` | Core Baseline | 77 | `1d5cb1aaa9d76edc3532e593c803cb936070a744` | 64 | `b6d7abe22144bac673b12d2f944150fdc8b6f057a58e73658b68b268c2e58ed2` | `b6d7abe22144bac673b12d2f944150fdc8b6f057a58e73658b68b268c2e58ed2` | YES | `PASS` |
| `X8` | Core Strong | 86 | `b431e7f2fb3038af2a356ff2a4e1764a3b5bbfe4` | 179 | `21e73e95fa79477b8106706f273284d7b3344f944146e2a21cf0c2e465c4dac5` | `21e73e95fa79477b8106706f273284d7b3344f944146e2a21cf0c2e465c4dac5` | YES | `PASS` |
| `B2` | Core High A | 90 | `27bf3f5e6b41c3862cc8c97bc7516bc7ed416ccf` | 71 | `918ea1412c2bad70bf87a6576fd0432becce62ec1b58cc7536402c74ad0ba753` | `918ea1412c2bad70bf87a6576fd0432becce62ec1b58cc7536402c74ad0ba753` | YES | `PASS` |
| `W7` | Core High B | 90 | `6a118f1240c50f74ab27eb4cc22337b3b9c448cf` | 100 | `640a42ff7ca7fe7329f917c430d9443d2a1c0905ebb7017aa120c3b6ca70fd10` | `640a42ff7ca7fe7329f917c430d9443d2a1c0905ebb7017aa120c3b6ca70fd10` | YES | `PASS` |
| `J9` | Core Ceiling | 96 | `aca2abce610be2ddabbf1a22fd645ac221d36a34` | 59 | `e621e66a573c4d9dca3e0987572cd83c55b86240cbf10c25055622f2931a9221` | `e621e66a573c4d9dca3e0987572cd83c55b86240cbf10c25055622f2931a9221` | YES | `PASS` |
| `L5` | Backup High C | 90 | `e7bc0058aa00c1f93effd3814db82c36c22b4a5f` | 95 | `8ccdc3bf7a97b2ab4d513e3820afb28d823b2433cc7088e8c4719a17edb353ba` | `8ccdc3bf7a97b2ab4d513e3820afb28d823b2433cc7088e8c4719a17edb353ba` | YES | `PASS` |
| `P3` | Backup 91 | 91 | `81eedafe7db2e7142ea3a525f81c94327b4da61a` | 179 | `949309843cc8fff6ea29a875909d227eddb9632d8b6b8bc07f915f882e5cc997` | `949309843cc8fff6ea29a875909d227eddb9632d8b6b8bc07f915f882e5cc997` | YES | `PASS` |

Overall Packet Reproducibility: `PASS` (7/7 identical)
