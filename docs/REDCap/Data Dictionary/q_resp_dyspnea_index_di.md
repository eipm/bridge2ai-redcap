<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Dyspnea Index (DI)

**Form name:** `q_resp_dyspnea_index_di` · **Category:** Adult Questionnaires (Respiratory) · **Status:** 🟢 Active  
**Introduced:** [v3.0.0] (2023-12-08) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 17 in REDCap · ⚫ 0 removed · ✏️ 5 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_respiratory_disorders_dyspnea_index_` | `q_resp_dyspnea_index_di` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `dyspnea_index_session_id` | Session ID | text | free text | ✔ |  | [v3.0.0] | — |
| 2 | `dyspnea_index_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v3.0.0] | [v3.3.0] ([1×](#dyspnea_index_started_at)) |
| 3 | `dyspnea_index_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v3.0.0] | [v3.3.0] ([1×](#dyspnea_index_completed_at)) |
| 4 | `dyspnea_index_duration` | Questionnaire Duration (seconds) | text | free text | ✔ |  | [v3.0.0] | — |
| 5 | `dyspnea_index_origin` | Dyspnea Index (DI) - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#dyspnea_index_origin)) |
| 6 | `dyspnea_index_via` | Dyspnea Index (DI) - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#dyspnea_index_via)) |
| 7 | `dyspnea_index_language` | Dyspnea Index (DI) - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#dyspnea_index_language)) |
| | **Please answer the following questions using a 0-4 rating scale. 0 = Never; 1 = Almost never; 2 = Sometimes; 3 = Almost…** | | | | | | | |
| 8 | `di_air_in` | I have trouble getting air in. | radio | never=Never · almostNever=Almost never · sometimes=Sometimes · almostAlways=Almost always … (5 options) | ✔ |  | [v3.0.0] | — |
| 9 | `di_tightness_throat` | I feel tightness in my throat when I am having my breathing problem. | radio | never=Never · almostNever=Almost never · sometimes=Sometimes · almostAlways=Almost always … (5 options) | ✔ |  | [v3.0.0] | — |
| 10 | `di_effort_breathe` | It takes more effort to breathe than it used to. | radio | never=Never · almostNever=Almost never · sometimes=Sometimes · almostAlways=Almost always … (5 options) | ✔ |  | [v3.0.0] | — |
| 11 | `di_weather_changes` | Changes in the weather affect my breathing problem. | radio | never=Never · almostNever=Almost never · sometimes=Sometimes · almostAlways=Almost always … (5 options) | ✔ |  | [v3.0.0] | — |
| 12 | `di_breathing_worse_stress` | My breathing gets worse with stress. | radio | never=Never · almostNever=Almost never · sometimes=Sometimes · almostAlways=Almost always … (5 options) | ✔ |  | [v3.0.0] | — |
| 13 | `di_sound_breathing_in` | I make sound/noise breathing in. | radio | never=Never · almostNever=Almost never · sometimes=Sometimes · almostAlways=Almost always … (5 options) | ✔ |  | [v3.0.0] | — |
| 14 | `di_strain` | I have to strain to breathe. | radio | never=Never · almostNever=Almost never · sometimes=Sometimes · almostAlways=Almost always … (5 options) | ✔ |  | [v3.0.0] | — |
| 15 | `di_exercise` | My shortness of breath gets worse with exercise or physical activity. | radio | never=Never · almostNever=Almost never · sometimes=Sometimes · almostAlways=Almost always … (5 options) | ✔ |  | [v3.0.0] | — |
| 16 | `di_breathing_stresses_me` | My breathing problem makes me feel stressed. | radio | never=Never · almostNever=Almost never · sometimes=Sometimes · almostAlways=Almost always … (5 options) | ✔ |  | [v3.0.0] | — |
| 17 | `di_restrict_personal_social_life` | My breathing problem causes me to restrict my personal and social life. | radio | never=Never · almostNever=Almost never · sometimes=Sometimes · almostAlways=Almost always … (5 options) | ✔ |  | [v3.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `dyspnea_index_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire Respiratory Disorders Dyspnea Index  |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `dyspnea_index_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Questionnaire Respiratory Disorders Dyspnea Index  |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `dyspnea_index_origin`

<details><summary>Dyspnea Index (DI) - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Dyspnea Index (DI) |
| [v4.8.0] | 2026-06-04 | Label | `Dyspnea Index (DI) Origin` | `Dyspnea Index (DI) - origin` |

</details>

### `dyspnea_index_via`

<details><summary>Dyspnea Index (DI) - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Dyspnea Index (DI) |
| [v4.8.0] | 2026-06-04 | Label | `Dyspnea Index (DI) via` | `Dyspnea Index (DI) - via` |

</details>

### `dyspnea_index_language`

<details><summary>Dyspnea Index (DI) - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Dyspnea Index (DI) |
| [v4.8.0] | 2026-06-04 | Label | `Dyspnea Index (DI) Language` | `Dyspnea Index (DI) - Language` |

</details>

<!-- milestone links -->
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
