<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Voice Problem Severity

> 🗄️ **Retired** from the Voice protocol in [v4.0.0] (2025-08-19). No new data is collected, but the fields stay in REDCap so data from earlier participants remains valid. · [Retired PDF (English)](<../../../docs/Adults/PDFs/en-us/Retired%20Questionnaire%20-%20PDFs/Voice/Q%20-%20Voice%20-%20Voice%20Problem%20Severity%20-%20English.pdf>)

**Form name:** `q_voice_voice_problem_severity` · **Category:** Adult Questionnaires (Voice) · **Status:** 🗄️ Retired  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.9.0] (2026-07-21)  
**Fields:** 📋 8 in REDCap · ⚫ 0 removed · ✏️ 6 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_voice_disorders_voice_problem_severi` | `q_voice_voice_problem_severity` |

## 📋 Fields

_All fields below share the instrument's status: 🗄️ Retired._

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `voice_severity_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `voice_severity_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#voice_severity_started_at)) |
| 3 | `voice_severity_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#voice_severity_completed_at)) |
| 4 | `voice_severity_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 5 | `voice_severity_origin` | Voice Severity - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#voice_severity_origin)) |
| 6 | `voice_severity_via` | Voice Severity - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#voice_severity_via)) |
| 7 | `voice_severity_language` | Voice Severity - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#voice_severity_language)) |
| | **Voice problem severity** | | | | | | | |
| 8 | `describe_the_severity_of_a` | Describe the severity of auditory-perceptual attributes of a voice problem *Overall severity scale (0-100) | slider | slider: 0 \| \| 100 | ✔ |  | [v1.0.0] | [v4.9.0] ([2×](#describe_the_severity_of_a)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `voice_severity_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Voice Disorders - Voice problem severity |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `voice_severity_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Voice Disorders - Voice problem severity |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `voice_severity_origin`

<details><summary>Voice Severity - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Voice Problem Severity |
| [v4.8.0] | 2026-06-04 | Label | `Voice Severity Origin` | `Voice Severity - origin` |

</details>

### `voice_severity_via`

<details><summary>Voice Severity - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Voice Problem Severity |
| [v4.8.0] | 2026-06-04 | Label | `Voice Severity via` | `Voice Severity - via` |

</details>

### `voice_severity_language`

<details><summary>Voice Severity - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Voice Problem Severity |
| [v4.8.0] | 2026-06-04 | Label | `Voice Severity Language` | `Voice Severity - Language` |

</details>

### `describe_the_severity_of_a`

<details><summary>Describe the severity of auditory-perceptual attributes of a voice problem *Overall sever… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Voice Disorders - Voice problem severity |
| [v3.13.0] | 2024-08-16 | Label | `Describe the severity of auditory-perceptual attributes of a voice problem *Overall severity scale (0-100)` | `Describe the severity of auditory-perceptual attributes of a voice problem *Overall severity scale (0-100)` |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v3.13.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.13.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
