<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Word-Color Stroop

**Form name:** `q_neuro_wordcolor_stroop` · **Category:** Adult Questionnaires (Neurological & Neurodegenerative) · **Status:** 🟢 Active  
**Introduced:** [v3.0.0] (2023-12-08) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 68 in REDCap · ⚫ 0 removed · ✏️ 8 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_neurological_and_neurogenerativ_919a` | `q_neuro_wordcolor_stroop` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `stroop_session_id` | Session ID | text | free text |  |  | [v3.0.0] | — |
| 2 | `stroop_recording_acoustic_task_id` | Acoustic Task ID | text | free text | ✔ |  | [v3.0.0] | — |
| 3 | `stroop_started_at` | Questionnaire Started At | text | free text |  | 🔒 | [v3.0.0] | [v3.3.0] ([1×](#stroop_started_at)) |
| 4 | `stroop_completed_at` | Questionnaire Completed At | text | free text |  | 🔒 | [v3.0.0] | [v3.3.0] ([1×](#stroop_completed_at)) |
| 5 | `stroop_duration` | Questionnaire Duration (seconds) | text | free text |  |  | [v3.0.0] | — |
| 6 | `stroop_origin` | Word-Color Stroop - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#stroop_origin)) |
| 7 | `stroop_via` | Word-Color Stroop - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#stroop_via)) |
| 8 | `stroop_language` | Word-Color Stroop - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#stroop_language)) |
| | **Item 1** | | | | | | | |
| 9 | `stroop_item_stimulus_1` | Item 1 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | — |
| 10 | `stroop_item_color_1` | Item 1 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 11 | `stroop_item_time_1` | Item 1 Time Start | text | free text |  |  | [v3.0.0] | — |
| 12 | `stroop_item_correct_1` | Item 1 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 2** | | | | | | | |
| 13 | `stroop_item_stimulus_2` | Item 2 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | — |
| 14 | `stroop_item_color_2` | Item 2 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 15 | `stroop_item_time_2` | Item 2 Time Start | text | free text |  |  | [v3.0.0] | — |
| 16 | `stroop_item_correct_2` | Item 2 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 3** | | | | | | | |
| 17 | `stroop_item_stimulus_3` | Item 3 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | — |
| 18 | `stroop_item_color_3` | Item 3 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 19 | `stroop_item_time_3` | Item 3 Time Start | text | free text |  |  | [v3.0.0] | — |
| 20 | `stroop_item_correct_3` | Item 3 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 4** | | | | | | | |
| 21 | `stroop_item_stimulus_4` | Item 4 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | — |
| 22 | `stroop_item_color_4` | Item 4 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 23 | `stroop_item_time_4` | Item 4 Time Start | text | free text |  |  | [v3.0.0] | — |
| 24 | `stroop_item_correct_4` | Item 4 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 5** | | | | | | | |
| 25 | `stroop_item_stimulus_5` | Item 5 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | — |
| 26 | `stroop_item_color_5` | Item 5 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 27 | `stroop_item_time_5` | Item 5 Time Start | text | free text |  |  | [v3.0.0] | — |
| 28 | `stroop_item_correct_5` | Item 5 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 6** | | | | | | | |
| 29 | `stroop_item_stimulus_6` | Item 6 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | — |
| 30 | `stroop_item_color_6` | Item 6 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 31 | `stroop_item_time_6` | Item 6 Time Start | text | free text |  |  | [v3.0.0] | — |
| 32 | `stroop_item_correct_6` | Item 6 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 7** | | | | | | | |
| 33 | `stroop_item_stimulus_7` | Item 7 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | — |
| 34 | `stroop_item_color_7` | Item 7 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 35 | `stroop_item_time_7` | Item 7 Time Start | text | free text |  |  | [v3.0.0] | — |
| 36 | `stroop_item_correct_7` | Item 7 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 8** | | | | | | | |
| 37 | `stroop_item_stimulus_8` | Item 8 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | — |
| 38 | `stroop_item_color_8` | Item 8 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 39 | `stroop_item_time_8` | Item 8 Time Start | text | free text |  |  | [v3.0.0] | — |
| 40 | `stroop_item_correct_8` | Item 8 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 9** | | | | | | | |
| 41 | `stroop_item_stimulus_9` | Item 9 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | — |
| 42 | `stroop_item_color_9` | Item 9 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 43 | `stroop_item_time_9` | Item 9 Time Start | text | free text |  |  | [v3.0.0] | — |
| 44 | `stroop_item_correct_9` | Item 9 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 10** | | | | | | | |
| 45 | `stroop_item_stimulus_10` | Item 10 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | — |
| 46 | `stroop_item_color_10` | Item 10 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 47 | `stroop_item_time_10` | Item 10 Time Start | text | free text |  |  | [v3.0.0] | — |
| 48 | `stroop_item_correct_10` | Item 10 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 11** | | | | | | | |
| 49 | `stroop_item_stimulus_11` | Item 11 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | [v4.6.0] ([1×](#stroop_item_stimulus_11)) |
| 50 | `stroop_item_color_11` | Item 11 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 51 | `stroop_item_time_11` | Item 11 Time Start | text | free text |  |  | [v3.0.0] | — |
| 52 | `stroop_item_correct_11` | Item 11 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 12** | | | | | | | |
| 53 | `stroop_item_stimulus_12` | Item 12 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | — |
| 54 | `stroop_item_color_12` | Item 12 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 55 | `stroop_item_time_12` | Item 12 Time Start | text | free text |  |  | [v3.0.0] | — |
| 56 | `stroop_item_correct_12` | Item 12 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 13** | | | | | | | |
| 57 | `stroop_item_stimulus_13` | Item 13 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | — |
| 58 | `stroop_item_color_13` | Item 13 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 59 | `stroop_item_time_13` | Item 13 Time Start | text | free text |  |  | [v3.0.0] | — |
| 60 | `stroop_item_correct_13` | Item 13 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 14** | | | | | | | |
| 61 | `stroop_item_stimulus_14` | Item 14 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | [v4.6.0] ([1×](#stroop_item_stimulus_14)) |
| 62 | `stroop_item_color_14` | Item 14 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 63 | `stroop_item_time_14` | Item 14 Time Start | text | free text |  |  | [v3.0.0] | — |
| 64 | `stroop_item_correct_14` | Item 14 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 15** | | | | | | | |
| 65 | `stroop_item_stimulus_15` | Item 15 Stimulus | radio | oooo=oooo · red=red · green=green · blue=blue … (6 options) |  |  | [v3.0.0] | [v4.6.0] ([1×](#stroop_item_stimulus_15)) |
| 66 | `stroop_item_color_15` | Item 15 Color | radio | red=red · green=green · blue=blue · purple=purple … (5 options) |  |  | [v3.0.0] | — |
| 67 | `stroop_item_time_15` | Item 15 Time Start | text | free text |  |  | [v3.0.0] | — |
| 68 | `stroop_item_correct_15` | Item 15 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `stroop_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Word-Color Stroop |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `stroop_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Word-Color Stroop |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `stroop_origin`

<details><summary>Word-Color Stroop - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Word-Color Stroop |
| [v4.8.0] | 2026-06-04 | Label | `Word-Color Stroop Origin` | `Word-Color Stroop - origin` |

</details>

### `stroop_via`

<details><summary>Word-Color Stroop - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Word-Color Stroop |
| [v4.8.0] | 2026-06-04 | Label | `Word-Color Stroop via` | `Word-Color Stroop - via` |

</details>

### `stroop_language`

<details><summary>Word-Color Stroop - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Word-Color Stroop |
| [v4.8.0] | 2026-06-04 | Label | `Word-Color Stroop Language` | `Word-Color Stroop - Language` |

</details>

### `stroop_item_stimulus_11`

<details><summary>Item 11 Stimulus — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Word-Color Stroop |
| [v4.6.0] | 2026-04-01 | Section header | `Item 1` | `Item 11` |

</details>

### `stroop_item_stimulus_14`

<details><summary>Item 14 Stimulus — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Word-Color Stroop |
| [v4.6.0] | 2026-04-01 | Section header | `Item 4` | `Item 14` |

</details>

### `stroop_item_stimulus_15`

<details><summary>Item 15 Stimulus — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Word-Color Stroop |
| [v4.6.0] | 2026-04-01 | Section header | `Item 5` | `Item 15` |

</details>

<!-- milestone links -->
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.6.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.6.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
