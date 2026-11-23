<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# PANAS

**Form name:** `q_mood_panas` · **Category:** Adult Questionnaires (Mood & Psychiatric) · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 17 in REDCap · ⚫ 0 removed · ✏️ 5 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_mood_disorders_panas` | `q_mood_panas` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `panas_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `panas_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#panas_started_at)) |
| 3 | `panas_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#panas_completed_at)) |
| 4 | `panas_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 5 | `panas_origin` | PANAS - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#panas_origin)) |
| 6 | `panas_via` | PANAS - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#panas_via)) |
| 7 | `panas_language` | PANAS - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#panas_language)) |
| | **Thinking about yourself and how you normally feel, to what extent do you generally feel? Interval measure: never 1 2 3…** | | | | | | | |
| 8 | `upset` | Upset | radio | 1=1 · 2=2 · 3=3 · 4=4 … (5 options) | ✔ |  | [v1.0.0] | — |
| 9 | `hostile` | Hostile | radio | 1=1 · 2=2 · 3=3 · 4=4 … (5 options) | ✔ |  | [v1.0.0] | — |
| 10 | `alert` | Alert | radio | 1=1 · 2=2 · 3=3 · 4=4 … (5 options) | ✔ |  | [v1.0.0] | — |
| 11 | `ashamed` | Ashamed | radio | 1=1 · 2=2 · 3=3 · 4=4 … (5 options) | ✔ |  | [v1.0.0] | — |
| 12 | `inspired` | Inspired | radio | 1=1 · 2=2 · 3=3 · 4=4 … (5 options) | ✔ |  | [v1.0.0] | — |
| 13 | `nervous` | Nervous | radio | 1=1 · 2=2 · 3=3 · 4=4 … (5 options) | ✔ |  | [v1.0.0] | — |
| 14 | `determined` | Determined | radio | 1=1 · 2=2 · 3=3 · 4=4 … (5 options) | ✔ |  | [v1.0.0] | — |
| 15 | `attentive` | Attentive | radio | 1=1 · 2=2 · 3=3 · 4=4 … (5 options) | ✔ |  | [v1.0.0] | — |
| 16 | `afraid` | Afraid | radio | 1=1 · 2=2 · 3=3 · 4=4 … (5 options) | ✔ |  | [v1.0.0] | — |
| 17 | `active` | Active | radio | 1=1 · 2=2 · 3=3 · 4=4 … (5 options) | ✔ |  | [v1.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `panas_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - PANAS |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `panas_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - PANAS |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `panas_origin`

<details><summary>PANAS - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | PANAS |
| [v4.8.0] | 2026-06-04 | Label | `PANAS Origin` | `PANAS - origin` |

</details>

### `panas_via`

<details><summary>PANAS - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | PANAS |
| [v4.8.0] | 2026-06-04 | Label | `PANAS via` | `PANAS - via` |

</details>

### `panas_language`

<details><summary>PANAS - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | PANAS |
| [v4.8.0] | 2026-06-04 | Label | `PANAS Language` | `PANAS - Language` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
