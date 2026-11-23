<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Pediatric — VHI-10

**Form name:** `pediatric_q_generic_vhi_10` · **Category:** Pediatric · **Status:** 🟢 Active  
**Introduced:** [v3.15.0] (2024-10-07) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 32 in REDCap · ⚫ 0 removed · ✏️ 4 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `peds_vhi_session_id` | Session ID | text | free text | ✔ |  | [v3.15.0] | — |
| 2 | `peds_vhi_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v3.15.0] | — |
| 3 | `peds_vhi_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v3.15.0] | — |
| 4 | `peds_vhi_duration` | Questionnaire Duration (seconds) | text | free text |  |  | [v3.15.0] | — |
| 5 | `peds_vhi_origin` | Peds VHI-10 - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App · reproschema=Bridge2AI Reproschema | ✔ |  | [v4.7.0] | [v4.10.0] ([2×](#peds_vhi_origin)) |
| 6 | `peds_vhi_via` | Peds VHI-10 - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#peds_vhi_via)) |
| 7 | `peds_vhi_language` | Peds VHI-10 - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#peds_vhi_language)) |
| | **Pediatric VHI 10 Questionnaire** | | | | | | | |
| 8 | `peds_vhi_talkativeness` | I would rate my child's talkativeness as the following: | slider | slider: Quiet Talker \| Average Talker \| Extremely Talkative |  |  | [v3.15.0] | — |
| 9 | `peds_voice_difficult_hear` | My child's voice makes it difficult for people to hear him/her. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 10 | `peds_difficulty_understanding` | People have difficulty understanding my child in a noisy room. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 11 | `peds_difficulty_hearing` | At home, we have difficulty hearing my child when he/she calls through the house. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 12 | `peds_avoid_communicating` | My child tends to avoid communicating because of his/her voice. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 13 | `peds_speaks_less` | My child speaks with friends, neighbours, or relatives less often because of his/her voice. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 14 | `peds_repeat_speaking` | People ask my child to repeat him/herself when speaking face-to-face. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 15 | `peds_voice_diffculities` | My child's voice difficulties restrict personal, educational and social activities. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 16 | `peds_out_of_air_talking` | My child runs out of air when talking. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 17 | `peds_voice_changes` | The sound of my child's voice changes throughout the day. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 18 | `peds_wrong_with_voice` | People ask, "What's wrong with my child's voice?" | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 19 | `peds_dry_raspy_hoarse` | My child's voice sounds dry, raspy, and/or hoarse. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 20 | `peds_unpredictable` | The quality of my child's voice is unpredictable. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 21 | `peds_straining` | My child uses a great deal of effort to speak (e.g., straining). | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 22 | `peds_worse_in_evening` | My child's voice is worse in the evening. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 23 | `peds_gives_out` | My child's voice "gives out" when speaking. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 24 | `peds_yell_to_hear` | My child has to yell in order for others to hear him/her. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 25 | `peds_tense_talking` | My child appears tense when talking with others because of his/her voice. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 26 | `peds_seem_irritated` | People seem irritated with my child's voice. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 27 | `peds_other_not_understand` | I find other people don't understand my child's voice problem. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 28 | `peds_frustrated_voice` | My child is frustrated with his/her voice problem. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 29 | `peds_less_out_going` | My child is less out-going because of his/her voice problem. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 30 | `peds_annoyed_repeat` | My child is annoyed when people ask him/her to repeat. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 31 | `peds_embarrassed_repeat` | My child is embarrassed when people ask him/her to repeat. | radio | never=Never · almostNever=Almost Never · sometimes=Sometimes · almostAlways=Almost Always … (5 options) |  |  | [v3.15.0] | — |
| 32 | `peds_severity_voice_problem` | Please indicate the severity of your child's voice problem | slider | slider: Normal \| \| Severe |  |  | [v3.15.0] | [v4.9.0] ([1×](#peds_severity_voice_problem)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `peds_vhi_origin`

<details><summary>Peds VHI-10 - origin — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — VHI-10 |
| [v4.8.0] | 2026-06-04 | Label | `Peds VHI-10 Origin` | `Peds VHI-10 - origin` |
| [v4.10.0] | 2026-08-27 | Choices / calculation | 2 options | ➕ `reproschema`=Bridge2AI Reproschema |

</details>

### `peds_vhi_via`

<details><summary>Peds VHI-10 - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — VHI-10 |
| [v4.8.0] | 2026-06-04 | Label | `Peds VHI-10 via` | `Peds VHI-10 - via` |

</details>

### `peds_vhi_language`

<details><summary>Peds VHI-10 - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — VHI-10 |
| [v4.8.0] | 2026-06-04 | Label | `Peds VHI-10 Language` | `Peds VHI-10 - Language` |

</details>

### `peds_severity_voice_problem`

<details><summary>Please indicate the severity of your child's voice problem — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — VHI-10 |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |

</details>

<!-- milestone links -->
[v3.15.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.15.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
