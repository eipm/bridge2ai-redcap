<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Patient Health Questionnaire (PHQ-9)

**Form name:** `q_generic_patient_health_questionnaire9` · **Category:** Adult Questionnaires (Generic) · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 17 in REDCap · ⚫ 0 removed · ✏️ 6 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_across_all_cohorts_patient_health_qu` | `q_generic_patient_health_questionnaire9` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `phq_9_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `phq_9_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#phq_9_started_at)) |
| 3 | `phq_9_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#phq_9_completed_at)) |
| 4 | `phq_9_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 5 | `phq_9_origin` | Patient Health Questionnaire 9 - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#phq_9_origin)) |
| 6 | `phq_9_via` | Patient Health Questionnaire 9 - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#phq_9_via)) |
| 7 | `phq_9_language` | Patient Health Questionnaire 9 - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#phq_9_language)) |
| | **Over the last 2 weeks, how often have you been bothered by any of the following problems?** | | | | | | | |
| 8 | `no_interest` | Little interest or pleasure in doing things. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 9 | `feeling_depressed` | Feeling down, depressed, or hopeless. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 10 | `trouble_sleeping` | Trouble falling or staying asleep, or sleeping too much. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 11 | `no_energy` | Feeling tired or having little energy. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 12 | `no_appetite` | Poor appetite or overeating. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 13 | `feeling_bad_self` | Feeling bad about yourself - or that you are a failure or have let yourself or your family down. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 14 | `trouble_concentrate` | Trouble concentrating on things, such as reading the newspaper or watching television. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 15 | `move_speak_slow` | Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving… | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 16 | `thoughts_death` | Thoughts that you would be better off dead or of hurting yourself in some way. | radio | 0=Not at all · 1=Several days · 2=More than half the days · 3=Nearly every day | ✔ |  | [v1.0.0] | — |
| 17 | `hard_to_work` | How difficult have they made it for you to do your work, take care of things at home, or get along with other people? | radio | 0=Not difficult at all · 1=Somewhat difficult · 2=Very difficult · 3=Extremely difficult |  |  | [v1.0.0] | [v3.1.0] ([1×](#hard_to_work)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `phq_9_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across all cohorts - Patient Health Questionnaire-9 |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `phq_9_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across all cohorts - Patient Health Questionnaire-9 |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `phq_9_origin`

<details><summary>Patient Health Questionnaire 9 - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Patient Health Questionnaire (PHQ-9) |
| [v4.8.0] | 2026-06-04 | Label | `Patient Health Questionnaire 9 Origin` | `Patient Health Questionnaire 9 - origin` |

</details>

### `phq_9_via`

<details><summary>Patient Health Questionnaire 9 - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Patient Health Questionnaire (PHQ-9) |
| [v4.8.0] | 2026-06-04 | Label | `Patient Health Questionnaire 9 via` | `Patient Health Questionnaire 9 - via` |

</details>

### `phq_9_language`

<details><summary>Patient Health Questionnaire 9 - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Patient Health Questionnaire (PHQ-9) |
| [v4.8.0] | 2026-06-04 | Label | `Patient Health Questionnaire 9 Language` | `Patient Health Questionnaire 9 - Language` |

</details>

### `hard_to_work`

<details><summary>How difficult have they made it for you to do your work, take care of things at home, or… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Across all cohorts - Patient Health Questionnaire-9 |
| [v3.1.0] | 2024-01-24 | Branching logic | `[no_interest] > 1 or [feeling_depressed] > 1 or [trouble_sleeping] > 1 or [no_energy] > 1 or [no_appetite] > 1 or [feeling_bad_self] > 1 or [trouble_concentrat…` | `[no_interest] > 0 or [feeling_depressed] > 0 or [trouble_sleeping] > 0 or [no_energy] > 0 or [no_appetite] > 0 or [feeling_bad_self] > 0 or [trouble_concentrat…` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
