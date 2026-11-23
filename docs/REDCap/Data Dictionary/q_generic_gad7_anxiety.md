<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# GAD-7 Anxiety

**Form name:** `q_generic_gad7_anxiety` · **Category:** Adult Questionnaires (Generic) · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 15 in REDCap · ⚫ 0 removed · ✏️ 6 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_across_all_cohorts_gad7_anxiety` | `q_generic_gad7_anxiety` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `gad_7_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `gad_7_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#gad_7_started_at)) |
| 3 | `gad_7_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#gad_7_completed_at)) |
| 4 | `gad_7_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 5 | `gad_7_origin` | GAD-7 - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#gad_7_origin)) |
| 6 | `gad_7_via` | GAD-7 - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#gad_7_via)) |
| 7 | `gad_7_language` | GAD-7 - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#gad_7_language)) |
| | **Over the last two weeks, how often have you been bothered by the following problems?** | | | | | | | |
| 8 | `nervous_anxious` | Feeling nervous, anxious, or on edge. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 9 | `cant_control_worry` | Not being able to stop or control worrying. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 10 | `worry_too_much` | Worrying too much about different things. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 11 | `trouble_relaxing` | Trouble relaxing. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 12 | `hard_to_sit_still` | Being so restless that it is hard to sit still. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 13 | `easily_agitated` | Becoming easily annoyed or irritable. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 14 | `afraid_of_things` | Feeling afraid, as if something awful might happen. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 15 | `tough_to_work` | How difficult have they made it for you to do your work, take care of things at home, or get along with other people? | radio | 0=Not difficult at all · 1=Somewhat difficult · 2=Very difficult · 3=Extremely difficult |  |  | [v1.0.0] | [v3.1.0] ([1×](#tough_to_work)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `gad_7_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across all cohorts - GAD-7 Anxiety |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `gad_7_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across all cohorts - GAD-7 Anxiety |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `gad_7_origin`

<details><summary>GAD-7 - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | GAD-7 Anxiety |
| [v4.8.0] | 2026-06-04 | Label | `GAD-7 Origin` | `GAD-7 - origin` |

</details>

### `gad_7_via`

<details><summary>GAD-7 - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | GAD-7 Anxiety |
| [v4.8.0] | 2026-06-04 | Label | `GAD-7 via` | `GAD-7 - via` |

</details>

### `gad_7_language`

<details><summary>GAD-7 - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | GAD-7 Anxiety |
| [v4.8.0] | 2026-06-04 | Label | `GAD-7 Language` | `GAD-7 - Language` |

</details>

### `tough_to_work`

<details><summary>How difficult have they made it for you to do your work, take care of things at home, or… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across all cohorts - GAD-7 Anxiety |
| [v3.1.0] | 2024-01-24 | Branching logic | `[nervous_anxious] > 1 or [cant_control_worry] > 1 or [worry_too_much] > 1 or [trouble_relaxing] > 1 or [hard_to_sit_still] > 1 or [easily_agitated] > 1 or [afr…` | `[nervous_anxious] > 0 or [cant_control_worry] > 0 or [worry_too_much] > 0 or [trouble_relaxing] > 0 or [hard_to_sit_still] > 0 or [easily_agitated] > 0 or [afr…` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
