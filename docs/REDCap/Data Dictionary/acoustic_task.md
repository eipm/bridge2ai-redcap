<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Acoustic Task

**Form name:** `acoustic_task` · **Category:** Sessions and Recordings · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 11 in REDCap · ⚫ 0 removed · ✏️ 5 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| 1 | `acoustic_task_id` | Acoustic Task ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `acoustic_task_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 3 | `acoustic_task_name` | Acoustic Task Name | text | free text | ✔ |  | [v1.0.0] | — |
| 4 | `acoustic_task_cohort` | Acoustic Task Cohort | text | free text | ✔ |  | [v1.0.0] | — |
| 5 | `acoustic_task_status` | Acoustic Task Status | radio | 1=Skipped · 2=Completed |  |  | [v1.0.0] | — |
| 6 | `acoustic_task_started_at` | Acoustic Task Started At | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#acoustic_task_started_at)) |
| 7 | `acoustic_task_completed_at` | Acoustic Task Completed At | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#acoustic_task_completed_at)) |
| 8 | `acoustic_task_duration` | Acoustic Task Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 9 | `acoustic_task_origin` | Acoustic Task - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App · reproschema=Bridge2AI Reproschema | ✔ |  | [v4.7.0] | [v4.10.0] ([2×](#acoustic_task_origin)) |
| 10 | `acoustic_task_via` | Acoustic Task - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#acoustic_task_via)) |
| 11 | `acoustic_task_language` | Acoustic Task - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#acoustic_task_language)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `acoustic_task_started_at`

<details><summary>Acoustic Task Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Acoustic Task |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `acoustic_task_completed_at`

<details><summary>Acoustic Task Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Acoustic Task |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `acoustic_task_origin`

<details><summary>Acoustic Task - origin — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Acoustic Task |
| [v4.8.0] | 2026-06-04 | Label | `Acoustic Task Origin` | `Acoustic Task - origin` |
| [v4.10.0] | 2026-08-27 | Choices / calculation | 2 options | ➕ `reproschema`=Bridge2AI Reproschema |

</details>

### `acoustic_task_via`

<details><summary>Acoustic Task - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Acoustic Task |
| [v4.8.0] | 2026-06-04 | Label | `Acoustic Task via` | `Acoustic Task - via` |

</details>

### `acoustic_task_language`

<details><summary>Acoustic Task - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Acoustic Task |
| [v4.8.0] | 2026-06-04 | Label | `Acoustic Task Language` | `Acoustic Task - Language` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
