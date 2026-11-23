<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Voice Handicap Index (VHI-10)

**Form name:** `q_generic_voice_handicap_index_vhi10` · **Category:** Adult Questionnaires (Generic) · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 18 in REDCap · ⚫ 0 removed · ✏️ 5 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_across_all_cohorts_voice_handicap_in` | `q_generic_voice_handicap_index_vhi10` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `vhi_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `vhi_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#vhi_started_at)) |
| 3 | `vhi_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#vhi_completed_at)) |
| 4 | `vhi_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 5 | `vhi_origin` | VHI-10 - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#vhi_origin)) |
| 6 | `vhi_via` | VHI-10 - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#vhi_via)) |
| 7 | `vhi_language` | VHI-10 - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#vhi_language)) |
| 8 | `vhi_10_calc_score` | VHI-10 Score: | calc | calc: `sum( if([voice_difficult_hear]="never", 0, if([voice_diffic…` |  |  | [v3.21.0] | — |
| | **Voice Handicap Index (VHI-10)** | | | | | | | |
| 9 | `voice_difficult_hear` | My voice makes it difficult for people to hear me. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) | ✔ |  | [v1.0.0] | — |
| 10 | `tough_to_understand` | People have difficulty understanding me in a noisy room. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) | ✔ |  | [v1.0.0] | — |
| 11 | `voice_restrict_social` | My voice difficulties restrict personal and social life. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) | ✔ |  | [v1.0.0] | — |
| 12 | `left_out_convo` | I feel left out of conversations because of my voice. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) | ✔ |  | [v1.0.0] | — |
| 13 | `voice_lose_income` | My voice problem causes me to lose income. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) | ✔ |  | [v1.0.0] | — |
| 14 | `strain_voice` | I feel as though I have to strain to produce voice. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) | ✔ |  | [v1.0.0] | — |
| 15 | `voice_clarity` | The clarity of my voice is unpredictable. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) | ✔ |  | [v1.0.0] | — |
| 16 | `voice_upsetting` | My voice problem upsets me. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) | ✔ |  | [v1.0.0] | — |
| 17 | `voice_handicapped` | My voice makes me feel handicapped. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) | ✔ |  | [v1.0.0] | — |
| 18 | `ask_whats_wrong_voice` | People ask, "What's wrong with your voice?" | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) | ✔ |  | [v1.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `vhi_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across all cohorts - Voice Handicap Index (VHI-10) |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `vhi_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across all cohorts - Voice Handicap Index (VHI-10) |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `vhi_origin`

<details><summary>VHI-10 - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Voice Handicap Index (VHI-10) |
| [v4.8.0] | 2026-06-04 | Label | `VHI-10 Origin` | `VHI-10 - origin` |

</details>

### `vhi_via`

<details><summary>VHI-10 - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Voice Handicap Index (VHI-10) |
| [v4.8.0] | 2026-06-04 | Label | `VHI-10 via` | `VHI-10 - via` |

</details>

### `vhi_language`

<details><summary>VHI-10 - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Voice Handicap Index (VHI-10) |
| [v4.8.0] | 2026-06-04 | Label | `VHI-10 Language` | `VHI-10 - Language` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v3.21.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.21.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
