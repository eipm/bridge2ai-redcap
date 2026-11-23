<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Harvard Sentences

**Form name:** `q_generic_harvard_sentences` · **Category:** Adult Questionnaires (Generic) · **Status:** 🟢 Active  
**Introduced:** [v4.0.0] (2025-08-19) · **Last changed:** [v4.9.1] (2026-07-21)  
**Fields:** 📋 9 in REDCap · ⚫ 0 removed · ✏️ 3 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `harvard_sentences_session_id` | Session ID | text | free text | ✔ |  | [v4.0.0] | — |
| 2 | `harvard_sentences_recording_acoustic_task_id` | Acoustic Task ID | text | free text | ✔ |  | [v4.0.0] | — |
| 3 | `harvard_sentences_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v4.0.0] | — |
| 4 | `harvard_sentences_completed_at` | Questionnaire Completed At | text | free text |  | 🔒 | [v4.0.0] | — |
| 5 | `harvard_sentences_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v4.0.0] | — |
| 6 | `harvard_sentences_origin` | Harvard Sentences - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.9.1] ([3×](#harvard_sentences_origin)) |
| 7 | `harvard_sentences_via` | Harvard Sentences - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#harvard_sentences_via)) |
| 8 | `harvard_sentences_language` | Harvard Sentences - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#harvard_sentences_language)) |
| | **Harvard Sentences** | | | | | | | |
| 9 | `harvard_sentences_list_order` | Harvard Sentence List Order Array (comma separated) | text | free text | ✔ |  | [v4.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `harvard_sentences_origin`

<details><summary>Harvard Sentences - origin — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Harvard Sentences |
| [v4.8.0] | 2026-06-04 | Label | `Harvard Sentences Origin` | `Harvard Sentences - origin` |
|  |  | Choices / calculation | 2 options | ✏️ `website`: Bridge2AI Web Appa → Bridge2AI Web App |
| [v4.9.0] | 2026-07-21 | Choices / calculation | 2 options | ✏️ `website`: Bridge2AI Web App → Bridge2AI Web Appa |
| [v4.9.1] | 2026-07-21 | Choices / calculation | 2 options | ✏️ `website`: Bridge2AI Web Appa → Bridge2AI Web App |

</details>

### `harvard_sentences_via`

<details><summary>Harvard Sentences - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Harvard Sentences |
| [v4.8.0] | 2026-06-04 | Label | `Harvard Sentences via` | `Harvard Sentences - via` |

</details>

### `harvard_sentences_language`

<details><summary>Harvard Sentences - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Harvard Sentences |
| [v4.8.0] | 2026-06-04 | Label | `Harvard Sentences Language` | `Harvard Sentences - Language` |

</details>

<!-- milestone links -->
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
[v4.9.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.1
