<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Random Item Generation

**Form name:** `q_neuro_random_item_generation` · **Category:** Adult Questionnaires (Neurological & Neurodegenerative) · **Status:** 🟢 Active  
**Introduced:** [v3.0.0] (2023-12-08) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 9 in REDCap · ⚫ 0 removed · ✏️ 5 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_neurological_and_neurogenerativ_6688` | `q_neuro_random_item_generation` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `random_session_id` | Session ID | text | free text |  |  | [v3.0.0] | — |
| 2 | `random_recording_acoustic_task_id` | Acoustic Task ID | text | free text | ✔ |  | [v3.0.0] | — |
| 3 | `random_started_at` | Questionnaire Started At | text | free text |  | 🔒 | [v3.0.0] | [v3.3.0] ([1×](#random_started_at)) |
| 4 | `random_completed_at` | Questionnaire Completed At | text | free text |  | 🔒 | [v3.0.0] | [v3.3.0] ([1×](#random_completed_at)) |
| 5 | `random_duration` | Questionnaire Duration (seconds) | text | free text |  |  | [v3.0.0] | — |
| 6 | `random_origin` | Random Item Generation - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#random_origin)) |
| 7 | `random_via` | Random Item Generation - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#random_via)) |
| 8 | `random_language` | Random Item Generation - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#random_language)) |
| | **Random item generation / semantic fluency** | | | | | | | |
| 9 | `random_item_generation_category` | Random item generation category | radio | numbers=Numbers · letters=Letters · firstNames=First names · cityNames=City names … (10 options) |  |  | [v3.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `random_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Random Item Generation |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `random_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Random Item Generation |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `random_origin`

<details><summary>Random Item Generation - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Random Item Generation |
| [v4.8.0] | 2026-06-04 | Label | `Random Item Generation Origin` | `Random Item Generation - origin` |

</details>

### `random_via`

<details><summary>Random Item Generation - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Random Item Generation |
| [v4.8.0] | 2026-06-04 | Label | `Random Item Generation via` | `Random Item Generation - via` |

</details>

### `random_language`

<details><summary>Random Item Generation - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Random Item Generation |
| [v4.8.0] | 2026-06-04 | Label | `Random Item Generation Language` | `Random Item Generation - Language` |

</details>

<!-- milestone links -->
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
