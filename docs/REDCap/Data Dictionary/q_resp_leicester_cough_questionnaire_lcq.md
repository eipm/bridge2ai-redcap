<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Leicester Cough Questionnaire (LCQ)

**Form name:** `q_resp_leicester_cough_questionnaire_lcq` · **Category:** Adult Questionnaires (Respiratory) · **Status:** 🟢 Active  
**Introduced:** [v3.0.0] (2023-12-08) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 26 in REDCap · ⚫ 0 removed · ✏️ 5 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_respiratory_disorders_leicester_coug` | `q_resp_leicester_cough_questionnaire_lcq` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `leicester_cough_session_id` | Session ID | text | free text | ✔ |  | [v3.0.0] | — |
| 2 | `leicester_cough_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v3.0.0] | [v3.3.0] ([1×](#leicester_cough_started_at)) |
| 3 | `leicester_cough_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v3.0.0] | [v3.3.0] ([1×](#leicester_cough_completed_at)) |
| 4 | `leicester_cough_duration` | Questionnaire Duration (seconds) | text | free text | ✔ |  | [v3.0.0] | — |
| 5 | `leicester_cough_origin` | Leicester Cough Questionnaire (LCQ) - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#leicester_cough_origin)) |
| 6 | `leicester_cough_via` | Leicester Cough Questionnaire (LCQ) - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#leicester_cough_via)) |
| 7 | `leicester_cough_language` | Leicester Cough Questionnaire (LCQ) - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#leicester_cough_language)) |
| | **Please answer the following questions using a 1-7 rating scale. 1 = None of the time; 2 = Hardly any of the time; 3 = A…** | | | | | | | |
| 8 | `lcq_chest_stomach_pains` | In the last 2 weeks, have you had chest or stomach pains as a result of your cough? | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 9 | `lcq_sputum_phlegm` | In the last 2 weeks, have you been bothered by sputum (phlegm) production when you cough? | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 10 | `lcq_tired` | In the last 2 weeks, have you been tired because of your cough? | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 11 | `lcq_embarrassed` | How often during the last 2 weeks have you felt embarrassed by your coughing? | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 12 | `lcq_anxious` | In the last 2 weeks, my cough has made me feel anxious. | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 13 | `lcq_interfere_job` | In the last 2 weeks, my cough has interfered with my job or other daily tasks. | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 14 | `lcq_interfere_life` | In the last 2 weeks, I felt that my cough interfered with the overall enjoyment of my life. | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 15 | `lcq_exposure_paint` | In the last 2 weeks, exposure to paint or fumes has made me cough. | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 16 | `lcq_sleep` | In the last 2 weeks, has your cough disturbed your sleep? | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 17 | `lcq_bout` | In the last 2 weeks, how many times a day have you had a coughing bout? | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 18 | `lcq_frustrated` | In the last 2 weeks, my cough has made me feel frustrated. | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 19 | `lcq_fed_up` | In the last 2 weeks, my cough has made me feel fed up. | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 20 | `lcq_hoarse_voice` | In the last 2 weeks, have you suffered from a hoarse voice as a result of your cough? | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 21 | `lcq_serious_illness` | In the last 2 weeks, have you worried that your cough may indicate serious illness? | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 22 | `lcq_other_people` | In the last 2 weeks, have you been concerned that other people think something is wrong with you, because of your cough? | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 23 | `lcq_interrupt_conversation` | In the last 2 weeks, my cough has interrupted conversation or telephone calls. | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 24 | `lcq_partner` | In the last 2 weeks, I feel that my cough has annoyed my partner, family, or friends. | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 25 | `lcq_felt_in_control` | In the last 2 weeks, have you felt in control of your cough? | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |
| 26 | `lcq_energy` | In the last 2 weeks, have you had a lot of energy? | radio | noneOfTheTime=None of the time · hardlyAnyOfTheTime=Hardly any of the time · aLittleOfTheTime=A little of the time · someOfTheTime=Some of the time … (7 options) | ✔ |  | [v3.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `leicester_cough_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Respiratory Disorders - Leicester Cough Questionnaire (LCQ) |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `leicester_cough_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire - Respiratory Disorders - Leicester Cough Questionnaire (LCQ) |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `leicester_cough_origin`

<details><summary>Leicester Cough Questionnaire (LCQ) - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Leicester Cough Questionnaire (LCQ) |
| [v4.8.0] | 2026-06-04 | Label | `Leicester Cough Questionnaire (LCQ) Origin` | `Leicester Cough Questionnaire (LCQ) - origin` |

</details>

### `leicester_cough_via`

<details><summary>Leicester Cough Questionnaire (LCQ) - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Leicester Cough Questionnaire (LCQ) |
| [v4.8.0] | 2026-06-04 | Label | `Leicester Cough Questionnaire (LCQ) via` | `Leicester Cough Questionnaire (LCQ) - via` |

</details>

### `leicester_cough_language`

<details><summary>Leicester Cough Questionnaire (LCQ) - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Leicester Cough Questionnaire (LCQ) |
| [v4.8.0] | 2026-06-04 | Label | `Leicester Cough Questionnaire (LCQ) Language` | `Leicester Cough Questionnaire (LCQ) - Language` |

</details>

<!-- milestone links -->
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
