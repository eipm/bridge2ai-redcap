<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Voice Perception

**Form name:** `q_generic_voice_perception` · **Category:** Adult Questionnaires (Generic) · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 8 in REDCap · ⚫ 0 removed · ✏️ 6 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_across_all_cohorts_voice_perception` | `q_generic_voice_perception` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `voice_perception_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `voice_perception_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#voice_perception_started_at)) |
| 3 | `voice_perception_completed_at` | Questionnaire Completed At | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#voice_perception_completed_at)) |
| 4 | `voice_perception_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 5 | `voice_perception_origin` | Voice Perception - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#voice_perception_origin)) |
| 6 | `voice_perception_via` | Voice Perception - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#voice_perception_via)) |
| 7 | `voice_perception_language` | Voice Perception - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#voice_perception_language)) |
| | **Voice Perception** | | | | | | | |
| 8 | `voice_quality_perception` | How would rate your voice quality today from 1-10? 1 is the lowest quality and 10 is the best voice quality | radio | 1=1 · 2=2 · 3=3 · 4=4 … (10 options) | ✔ |  | [v1.0.0] | [v4.0.1] ([3×](#voice_quality_perception)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `voice_perception_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across all cohorts - Voice Perception |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `voice_perception_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across all cohorts - Voice Perception |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `voice_perception_origin`

<details><summary>Voice Perception - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Voice Perception |
| [v4.8.0] | 2026-06-04 | Label | `Voice Perception Origin` | `Voice Perception - origin` |

</details>

### `voice_perception_via`

<details><summary>Voice Perception - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Voice Perception |
| [v4.8.0] | 2026-06-04 | Label | `Voice Perception via` | `Voice Perception - via` |

</details>

### `voice_perception_language`

<details><summary>Voice Perception - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Voice Perception |
| [v4.8.0] | 2026-06-04 | Label | `Voice Perception Language` | `Voice Perception - Language` |

</details>

### `voice_quality_perception`

<details><summary>How would rate your voice quality today from 1-10? 1 is the lowest quality and 10 is the… — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across all cohorts - Voice Perception |
| [v3.0.0] | 2023-12-08 | Label | `How would rate your voice quality today from 1-10. 1 is the lowest quality and 10 is the best voice quality` | `How would rate your voice quality today from 1-10? 1 is the lowest quality and 10 is the best voice quality` |
| [v3.13.0] | 2024-08-16 | Label | `How would rate your voice quality today from 1-10? 1 is the lowest quality and 10 is the best voice quality` | `How would rate your voice quality today from 1-10? 1 is the lowest quality and 10 is the best voice quality` |
| [v4.0.1] | 2025-08-28 | Section header | `Voice Quality Perception` | `Voice Perception` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v3.13.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.13.0
[v4.0.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.1
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
