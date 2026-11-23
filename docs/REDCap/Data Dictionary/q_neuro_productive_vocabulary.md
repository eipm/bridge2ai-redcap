<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Productive Vocabulary

**Form name:** `q_neuro_productive_vocabulary` · **Category:** Adult Questionnaires (Neurological & Neurodegenerative) · **Status:** 🟢 Active  
**Introduced:** [v3.0.0] (2023-12-08) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 26 in REDCap · ⚫ 0 removed · ✏️ 11 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_neurological_and_neurogenerativ_6ced` | `q_neuro_productive_vocabulary` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `vocabulary_session_id` | Session ID | text | free text |  |  | [v3.0.0] | — |
| 2 | `vocabulary_recording_acoustic_task_id` | Acoustic Task ID | text | free text | ✔ |  | [v3.0.0] | — |
| 3 | `vocabulary_started_at` | Questionnaire Started At | text | free text |  | 🔒 | [v3.0.0] | [v3.3.0] ([1×](#vocabulary_started_at)) |
| 4 | `vocabulary_completed_at` | Questionnaire Completed At | text | free text |  | 🔒 | [v3.0.0] | [v3.3.0] ([1×](#vocabulary_completed_at)) |
| 5 | `vocabulary_duration` | Questionnaire Duration (seconds) | text | free text |  |  | [v3.0.0] | — |
| 6 | `vocabulary_origin` | Productive Vocabulary - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#vocabulary_origin)) |
| 7 | `vocabulary_via` | Productive Vocabulary - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#vocabulary_via)) |
| 8 | `vocabulary_language` | Productive Vocabulary - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#vocabulary_language)) |
| | **Item 1** | | | | | | | |
| 9 | `vocabulary_item_word_1` | Item 1 Word | text | free text |  |  | [v3.0.0] | [v4.0.0] ([1×](#vocabulary_item_word_1)) |
| 10 | `vocabulary_item_difficulty_1` | Item 1 Word Difficulty | radio | 1=1 · 2=2 · 3=3 |  |  | [v3.0.0] | — |
| 11 | `vocabulary_item_correct_1` | Item 1 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 2** | | | | | | | |
| 12 | `vocabulary_item_word_2` | Item 2 Word | text | free text |  |  | [v3.0.0] | [v4.0.0] ([1×](#vocabulary_item_word_2)) |
| 13 | `vocabulary_item_difficulty_2` | Item 2 Word Difficulty | radio | 1=1 · 2=2 · 3=3 |  |  | [v3.0.0] | — |
| 14 | `vocabulary_item_correct_2` | Item 2 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 3** | | | | | | | |
| 15 | `vocabulary_item_word_3` | Item 3 Word | text | free text |  |  | [v3.0.0] | [v4.0.0] ([1×](#vocabulary_item_word_3)) |
| 16 | `vocabulary_item_difficulty_3` | Item 3 Word Difficulty | radio | 1=1 · 2=2 · 3=3 |  |  | [v3.0.0] | — |
| 17 | `vocabulary_item_correct_3` | Item 3 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 4** | | | | | | | |
| 18 | `vocabulary_item_word_4` | Item 4 Word | text | free text |  |  | [v3.0.0] | [v4.0.0] ([1×](#vocabulary_item_word_4)) |
| 19 | `vocabulary_item_difficulty_4` | Item 4 Word Difficulty | radio | 1=1 · 2=2 · 3=3 |  |  | [v3.0.0] | — |
| 20 | `vocabulary_item_correct_4` | Item 4 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 5** | | | | | | | |
| 21 | `vocabulary_item_word_5` | Item 5 Word | text | free text |  |  | [v3.0.0] | [v4.0.0] ([1×](#vocabulary_item_word_5)) |
| 22 | `vocabulary_item_difficulty_5` | Item 5 Word Difficulty | radio | 1=1 · 2=2 · 3=3 |  |  | [v3.0.0] | — |
| 23 | `vocabulary_item_correct_5` | Item 5 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |
| | **Item 6** | | | | | | | |
| 24 | `vocabulary_item_word_6` | Item 6 Word | text | free text |  |  | [v3.0.0] | [v4.0.0] ([1×](#vocabulary_item_word_6)) |
| 25 | `vocabulary_item_difficulty_6` | Item 6 Word Difficulty | radio | 1=1 · 2=2 · 3=3 |  |  | [v3.0.0] | — |
| 26 | `vocabulary_item_correct_6` | Item 6 Correct? | radio | yes=Yes · no=No |  |  | [v3.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `vocabulary_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Productive Vocabulary |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `vocabulary_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Productive Vocabulary |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `vocabulary_origin`

<details><summary>Productive Vocabulary - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Productive Vocabulary |
| [v4.8.0] | 2026-06-04 | Label | `Productive Vocabulary Origin` | `Productive Vocabulary - origin` |

</details>

### `vocabulary_via`

<details><summary>Productive Vocabulary - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Productive Vocabulary |
| [v4.8.0] | 2026-06-04 | Label | `Productive Vocabulary via` | `Productive Vocabulary - via` |

</details>

### `vocabulary_language`

<details><summary>Productive Vocabulary - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Productive Vocabulary |
| [v4.8.0] | 2026-06-04 | Label | `Productive Vocabulary Language` | `Productive Vocabulary - Language` |

</details>

### `vocabulary_item_word_1`

<details><summary>Item 1 Word — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Productive Vocabulary |
| [v4.0.0] | 2025-08-19 | Type | `radio` | `text` |
|  |  | Choices / calculation | 182 options | ➖ `boil`=boil, `duckling`=duckling, `cupboard`=cupboard, `workbench`=workbench, `agreeable`=agreeable, `swear`=swear … |

</details>

### `vocabulary_item_word_2`

<details><summary>Item 2 Word — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Productive Vocabulary |
| [v4.0.0] | 2025-08-19 | Type | `radio` | `text` |
|  |  | Choices / calculation | 182 options | ➖ `boil`=boil, `duckling`=duckling, `cupboard`=cupboard, `workbench`=workbench, `agreeable`=agreeable, `swear`=swear … |

</details>

### `vocabulary_item_word_3`

<details><summary>Item 3 Word — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Productive Vocabulary |
| [v4.0.0] | 2025-08-19 | Type | `radio` | `text` |
|  |  | Choices / calculation | 182 options | ➖ `boil`=boil, `duckling`=duckling, `cupboard`=cupboard, `workbench`=workbench, `agreeable`=agreeable, `swear`=swear … |

</details>

### `vocabulary_item_word_4`

<details><summary>Item 4 Word — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Productive Vocabulary |
| [v4.0.0] | 2025-08-19 | Type | `radio` | `text` |
|  |  | Choices / calculation | 182 options | ➖ `boil`=boil, `duckling`=duckling, `cupboard`=cupboard, `workbench`=workbench, `agreeable`=agreeable, `swear`=swear … |

</details>

### `vocabulary_item_word_5`

<details><summary>Item 5 Word — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Productive Vocabulary |
| [v4.0.0] | 2025-08-19 | Type | `radio` | `text` |
|  |  | Choices / calculation | 182 options | ➖ `boil`=boil, `duckling`=duckling, `cupboard`=cupboard, `workbench`=workbench, `agreeable`=agreeable, `swear`=swear … |

</details>

### `vocabulary_item_word_6`

<details><summary>Item 6 Word — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Neurological and Neurogenerative Disorders - Productive Vocabulary |
| [v4.0.0] | 2025-08-19 | Type | `radio` | `text` |
|  |  | Choices / calculation | 182 options | ➖ `boil`=boil, `duckling`=duckling, `cupboard`=cupboard, `workbench`=workbench, `agreeable`=agreeable, `swear`=swear … |

</details>

<!-- milestone links -->
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
