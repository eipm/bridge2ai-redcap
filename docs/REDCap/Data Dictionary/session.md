<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Session

**Form name:** `session` · **Category:** Sessions and Recordings · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 11 in REDCap · ⚫ 0 removed · ✏️ 7 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| 1 | `session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `session_record_id` | Record ID | text | free text | ✔ |  | [v4.3.0] | — |
| 3 | `session_status` | Session Status | radio | 1=In Progress · 2=Completed | ✔ |  | [v1.0.0] | [v4.4.0] ([1×](#session_status)) |
| 4 | `session_started_at` | Session Started At | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#session_started_at)) |
| 5 | `session_is_control_participant` | Is Control Participant? | radio | yes=Yes · no=No | ✔ |  | [v3.4.0] | — |
| 6 | `session_completed_at` | Session Completed At | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#session_completed_at)) |
| 7 | `session_duration` | Session Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 8 | `session_site` | Session Site? | radio | mit=MIT · mt_sinai=Mt. Sinai · sickkids=SickKids · usf=USF … (6 options) | ✔ |  | [v1.0.0] | [v4.1.0] ([3×](#session_site)) |
| 9 | `session_completed_by` | Who helped you answer the questions today? For example, did someone help you remember your medication list or how tired you are? This isn't… | checkbox | just_me=Just me · someone_else=Someone else helped me answer the quest… |  |  | [v4.0.0] | [v4.7.0] ([1×](#session_completed_by)) |
| 10 | `session_assigned_tasks` | Session Assigned Tasks | text | free text |  |  | [v4.2.0] | [v4.7.0] ([2×](#session_assigned_tasks)) |
| 11 | `session_language` | Session - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#session_language)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `session_status`

<details><summary>Session Status — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Session |
| [v4.4.0] | 2026-03-02 | Annotation | `@READONLY` | ∅ |

</details>

### `session_started_at`

<details><summary>Session Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Session |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `session_completed_at`

<details><summary>Session Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Session |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `session_site`

<details><summary>Session Site? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Session |
| [v3.0.0] | 2023-12-08 | Choices / calculation | 3 options | ➕ `bch`=BCH, `mit`=MIT, `mt_sinai`=Mt. Sinai, `usf`=USF, `vumc`=VUMC, `wcm`=WCM<br>➖ `USF`=USF, `WCM`=WCM, `MIT`=MIT |
| [v3.6.0] | 2024-06-10 | Choices / calculation | 6 options | ➕ `sickkids`=SickKids<br>➖ `bch`=BCH |
| [v4.1.0] | 2025-09-17 | Annotation | `@READONLY` | ∅ |

</details>

### `session_completed_by`

<details><summary>Who helped you answer the questions today? For example, did someone help you remember you… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Session |
| [v4.7.0] | 2026-05-04 | Annotation | ∅ | `@READONLY` |

</details>

### `session_assigned_tasks`

<details><summary>Session Assigned Tasks — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.2.0] | 2025-09-25 | 🆕 Introduced | | Session |
| [v4.4.0] | 2026-03-02 | Annotation | `@READONLY` | ∅ |
| [v4.7.0] | 2026-05-04 | Annotation | ∅ | `@READONLY` |

</details>

### `session_language`

<details><summary>Session - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Session |
| [v4.8.0] | 2026-06-04 | Label | `Session Language` | `Session - Language` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v3.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.4.0
[v3.6.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.6.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.2.0
[v4.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.3.0
[v4.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.4.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
