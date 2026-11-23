<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Pediatric — PHQ-A

**Form name:** `pediatric_q_generic_phqa` · **Category:** Pediatric · **Status:** 🟢 Active  
**Introduced:** [v3.15.0] (2024-10-07) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 16 in REDCap · ⚫ 0 removed · ✏️ 3 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `peds_phqa_session_id` | Session ID | text | free text | ✔ |  | [v3.15.0] | — |
| 2 | `peds_phqa_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v3.15.0] | — |
| 3 | `peds_phqa_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v3.15.0] | — |
| 4 | `peds_phqa_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v3.15.0] | — |
| 5 | `peds_phqa_origin` | Peds PHQ-A - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App · reproschema=Bridge2AI Reproschema | ✔ |  | [v4.7.0] | [v4.10.0] ([2×](#peds_phqa_origin)) |
| 6 | `peds_phqa_via` | Peds PHQ-A - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#peds_phqa_via)) |
| 7 | `peds_phqa_language` | Peds PHQ-A - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#peds_phqa_language)) |
| | **How often have you been bothered by each of the following symptoms during the past two weeks? For each symptom select t…** | | | | | | | |
| 8 | `peds_phqa_feeling_depressed` | Feeling down, depressed, irritable, or hopeless? | radio | notAtAll=Not at all · severalDays=Several days · moreThanHalfTheDays=More than half the days · nearlyEveryDay=Nearly every day | ✔ |  | [v3.15.0] | — |
| 9 | `peds_phqa_no_interest` | Little interest or pleasure in doing things? | radio | notAtAll=Not at all · severalDays=Several days · moreThanHalfTheDays=More than half the days · nearlyEveryDay=Nearly every day | ✔ |  | [v3.15.0] | — |
| 10 | `peds_phqa_trouble_sleeping` | Trouble falling asleep, staying asleep, or sleeping too much? | radio | notAtAll=Not at all · severalDays=Several days · moreThanHalfTheDays=More than half the days · nearlyEveryDay=Nearly every day | ✔ |  | [v3.15.0] | — |
| 11 | `peds_phqa_no_appetite` | Poor appetite, weight loss, or overeating? | radio | notAtAll=Not at all · severalDays=Several days · moreThanHalfTheDays=More than half the days · nearlyEveryDay=Nearly every day | ✔ |  | [v3.15.0] | — |
| 12 | `peds_phqa_no_energy` | Feeling tired, or having little energy? | radio | notAtAll=Not at all · severalDays=Several days · moreThanHalfTheDays=More than half the days · nearlyEveryDay=Nearly every day | ✔ |  | [v3.15.0] | — |
| 13 | `peds_phqa_feeling_bad_self` | Feeling bad about yourself - or feeling that you are a failure, or that you have let yourself or your family down? | radio | notAtAll=Not at all · severalDays=Several days · moreThanHalfTheDays=More than half the days · nearlyEveryDay=Nearly every day | ✔ |  | [v3.15.0] | — |
| 14 | `peds_phqa_trouble_concentrate` | Trouble concentrating on things like school work, reading, or watching TV? | radio | notAtAll=Not at all · severalDays=Several days · moreThanHalfTheDays=More than half the days · nearlyEveryDay=Nearly every day | ✔ |  | [v3.15.0] | — |
| 15 | `peds_phqa_move_speak_slow` | Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you were moving arou… | radio | notAtAll=Not at all · severalDays=Several days · moreThanHalfTheDays=More than half the days · nearlyEveryDay=Nearly every day | ✔ |  | [v3.15.0] | — |
| 16 | `peds_phqa_thoughts_death` | Thoughts that you would be better off dead, or of hurting yourself in some way? | radio | notAtAll=Not at all · severalDays=Several days · moreThanHalfTheDays=More than half the days · nearlyEveryDay=Nearly every day | ✔ |  | [v3.15.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `peds_phqa_origin`

<details><summary>Peds PHQ-A - origin — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — PHQ-A |
| [v4.8.0] | 2026-06-04 | Label | `Peds PHQ-A Origin` | `Peds PHQ-A - origin` |
| [v4.10.0] | 2026-08-27 | Choices / calculation | 2 options | ➕ `reproschema`=Bridge2AI Reproschema |

</details>

### `peds_phqa_via`

<details><summary>Peds PHQ-A - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — PHQ-A |
| [v4.8.0] | 2026-06-04 | Label | `Peds PHQ-A via` | `Peds PHQ-A - via` |

</details>

### `peds_phqa_language`

<details><summary>Peds PHQ-A - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — PHQ-A |
| [v4.8.0] | 2026-06-04 | Label | `Peds PHQ-A Language` | `Peds PHQ-A - Language` |

</details>

<!-- milestone links -->
[v3.15.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.15.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
