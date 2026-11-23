<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Pediatric — Voice Outcome Survey

**Form name:** `pediatric_q_generic_voice_outcome_survey` · **Category:** Pediatric · **Status:** 🟢 Active  
**Introduced:** [v3.15.0] (2024-10-07) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 11 in REDCap · ⚫ 0 removed · ✏️ 3 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `peds_os_session_id` | Session ID | text | free text |  |  | [v3.15.0] | — |
| 2 | `peds_os_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v3.15.0] | — |
| 3 | `peds_os_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v3.15.0] | — |
| 4 | `peds_os_duration` | Questionnaire Duration (seconds) | text | free text |  |  | [v3.15.0] | — |
| 5 | `peds_os_origin` | Peds Voice Outcome Survey - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App · reproschema=Bridge2AI Reproschema | ✔ |  | [v4.7.0] | [v4.10.0] ([2×](#peds_os_origin)) |
| 6 | `peds_os_via` | Peds Voice Outcome Survey - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#peds_os_via)) |
| 7 | `peds_os_language` | Peds Voice Outcome Survey - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#peds_os_language)) |
| | **Pediatric Voice Outcome Survey** | | | | | | | |
| 8 | `peds_os_limit_understood` | To what extent does you child's voice limit his or her ability to be understood in a noisy area? | radio | limitedALot=Limited a lot · limitedALittle=Limited a little · notLimitedAtAll=Not limited at all |  |  | [v3.15.0] | — |
| 9 | `peds_os_interfered_activities` | During the past 2 weeks, to what extent has your child's voice interfered with his or her normal social activities or with his or her schoo… | radio | notAtAll=Not at all · slightly=Slightly · moderately=Moderately · quiteABit=Quite a bit … (5 options) |  |  | [v3.15.0] | — |
| 10 | `peds_os_trouble_food_iquids` | How often does your child have trouble with food or liquids "going down the wrong pipe" when he or she eats food or drinks liquid and begin… | radio | allTheTime=All the time · mostOfTheTime=Most of the time · sometimes=Sometimes · rarely=Rarely … (5 options) |  |  | [v3.15.0] | — |
| 11 | `peds_os_straining` | Do you find your child "straining" when he or she speaks because of his or her voice problem? | radio | notAtAll=Not at all · aLittleBit=A little bit · moderately=Moderately · quiteABit=Quite a bit … (5 options) |  |  | [v3.15.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `peds_os_origin`

<details><summary>Peds Voice Outcome Survey - origin — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — Voice Outcome Survey |
| [v4.8.0] | 2026-06-04 | Label | `Peds Voice Outcome Survey Origin` | `Peds Voice Outcome Survey - origin` |
| [v4.10.0] | 2026-08-27 | Choices / calculation | 2 options | ➕ `reproschema`=Bridge2AI Reproschema |

</details>

### `peds_os_via`

<details><summary>Peds Voice Outcome Survey - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — Voice Outcome Survey |
| [v4.8.0] | 2026-06-04 | Label | `Peds Voice Outcome Survey via` | `Peds Voice Outcome Survey - via` |

</details>

### `peds_os_language`

<details><summary>Peds Voice Outcome Survey - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — Voice Outcome Survey |
| [v4.8.0] | 2026-06-04 | Label | `Peds Voice Outcome Survey Language` | `Peds Voice Outcome Survey - Language` |

</details>

<!-- milestone links -->
[v3.15.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.15.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
