<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# ADHD Adult

**Form name:** `q_mood_adhd_adult` · **Category:** Adult Questionnaires (Mood & Psychiatric) · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 25 in REDCap · ⚫ 0 removed · ✏️ 5 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_mood_disorders_adhd_adult` | `q_mood_adhd_adult` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `adhd_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `adhd_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#adhd_started_at)) |
| 3 | `adhd_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#adhd_completed_at)) |
| 4 | `adhd_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 5 | `adhd_origin` | ADHD Adult - Origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#adhd_origin)) |
| 6 | `adhd_via` | ADHD Adult - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#adhd_via)) |
| 7 | `adhd_language` | ADHD Adult - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#adhd_language)) |
| | **Please answer the questions below, rating yourself on each of the criteria shown using the scale on the right side of t…** | | | | | | | |
| 8 | `wrapping_up` | How often do you have trouble wrapping up the final details of a project, once the challenging parts have been done? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 9 | `things_in_order` | How often do you have difficulty getting things in order when you have to do a task that requires organization? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 10 | `remembering_appt` | How often do you have problems remembering appointments or obligations? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 11 | `avoidance` | When you have a task that requires a lot of thought, how often do you avoid or delay getting started? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 12 | `fidget` | How often do you fidget or squirm with your hands or feet when you have to sit down for a long time? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 13 | `overly_active` | How often do you feel overly active and compelled to do things, like you were driven by a motor? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 14 | `careless` | How often do you make careless mistakes when you have to work on a boring or difficult project? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 15 | `difficulty_attention` | How often do you have difficulty keeping your attention when you are doing boring or repetitive work? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 16 | `difficulty_concentrating` | How often do you have difficulty concentrating on what people say to you, even when they are speaking to you directly? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 17 | `misplace` | How often do you misplace or have difficulty finding things at home or at work? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 18 | `distracted` | How often are you distracted by activity or noise around you? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 19 | `remain_seated` | How often do you leave your seat in meetings or other situations in which you are expected to remain seated? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 20 | `restless` | How often do you feel restless or fidgety? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 21 | `difficulty_unwinding` | How often do you have difficulty unwinding and relaxing when you have time to yourself? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 22 | `talking_too_much` | How often do you find yourself talking too much when you are in social situations? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 23 | `finish_other_sent` | When you're in a conversation, how often do you find yourself finishing the sentences of the people you are talking to, before they can fin… | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 24 | `difficulty_waiting` | How often do you have difficulty waiting your turn in situations when turn taking is required? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |
| 25 | `interrupt_others` | How often do you interrupt others when they are busy? | radio | never=Never · rarely=Rarely · sometimes=Sometimes · often=Often … (5 options) | ✔ |  | [v1.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `adhd_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - ADHD Adult |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `adhd_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - ADHD Adult |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `adhd_origin`

<details><summary>ADHD Adult - Origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | ADHD Adult |
| [v4.8.0] | 2026-06-04 | Label | `ADHD Adult Origin` | `ADHD Adult - Origin` |

</details>

### `adhd_via`

<details><summary>ADHD Adult - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | ADHD Adult |
| [v4.8.0] | 2026-06-04 | Label | `ADHD Adult via` | `ADHD Adult - via` |

</details>

### `adhd_language`

<details><summary>ADHD Adult - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | ADHD Adult |
| [v4.8.0] | 2026-06-04 | Label | `ADHD Adult Language` | `ADHD Adult - Language` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
