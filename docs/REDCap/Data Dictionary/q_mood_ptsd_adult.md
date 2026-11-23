<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# PTSD Adult

> 🗄️ **Retired** from the Mood protocol in [v4.0.0] (2025-08-19). No new data is collected, but the fields stay in REDCap so data from earlier participants remains valid. · [Retired PDF (English)](<../../../docs/Adults/PDFs/en-us/Retired%20Questionnaire%20-%20PDFs/Mood/Q%20-%20Mood%20-%20PTSD%20Adult%20-%20English.pdf>)

**Form name:** `q_mood_ptsd_adult` · **Category:** Adult Questionnaires (Mood & Psychiatric) · **Status:** 🗄️ Retired  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 18 in REDCap · ⚫ 0 removed · ✏️ 5 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_mood_disorders_ptsd_adult` | `q_mood_ptsd_adult` |

## 📋 Fields

_All fields below share the instrument's status: 🗄️ Retired._

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `ptsd_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `ptsd_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#ptsd_started_at)) |
| 3 | `ptsd_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#ptsd_completed_at)) |
| 4 | `ptsd_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 5 | `ptsd_origin` | PTSD Adult - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#ptsd_origin)) |
| 6 | `ptsd_via` | PTSD Adult - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#ptsd_via)) |
| 7 | `ptsd_language` | PTSD Adult - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#ptsd_language)) |
| | **Severity of Posttraumatic Stress Symptoms - Adult** | | | | | | | |
| 8 | `traumatic_event` | Please list the traumatic event that you experienced | notes | free text (long) |  |  | [v1.0.0] | — |
| 9 | `traumatic_event_date` | Date of the traumatic event: | text | `date_ymd` |  |  | [v1.0.0] | — |
| | **People sometimes have problems after extremely stressful events or experiences. How much have you been bothered during…** | | | | | | | |
| 10 | `flashbacks` | Having "flashbacks", that is, you suddenly acted or felt as if a stressful experience from the past was happening all over again (for examp… | radio | 0=0=Not at all · 1=1=A little bit · 2=2=Moderately · 3=3=Quite a bit … (5 options) | ✔ |  | [v1.0.0] | — |
| 11 | `emotionally_upset` | Feeling very emotionally upset when something reminded you of a stressful experience? | radio | 0=0=Not at all · 1=1=A little bit · 2=2=Moderately · 3=3=Quite a bit … (5 options) | ✔ |  | [v1.0.0] | — |
| 12 | `avoiding_reminders` | Trying to avoid thoughts, feelings, or physical sensations that reminded you of a stressful experience? | radio | 0=0=Not at all · 1=1=A little bit · 2=2=Moderately · 3=3=Quite a bit … (5 options) | ✔ |  | [v1.0.0] | — |
| 13 | `thinking_stressful_event` | Thinking that a stressful event happened because you or someone else (who didn't directly harm you) did something wrong or didn't do everyt… | radio | 0=0=Not at all · 1=1=A little bit · 2=2=Moderately · 3=3=Quite a bit … (5 options) | ✔ |  | [v1.0.0] | — |
| 14 | `neg_emotional_state` | Having a very negative emotional state (for example, you were experiencing lots of fear, anger, guilt, shame, or horror) after a stressful… | radio | 0=0=Not at all · 1=1=A little bit · 2=2=Moderately · 3=3=Quite a bit … (5 options) | ✔ |  | [v1.0.0] | — |
| 15 | `losing_interest` | Losing interest in activities you used to enjoy before having a stressful experience? | radio | 0=0=Not at all · 1=1=A little bit · 2=2=Moderately · 3=3=Quite a bit … (5 options) | ✔ |  | [v1.0.0] | — |
| 16 | `super_alert` | Being "super alert", on guard, or constantly on the lookout for danger? | radio | 0=0=Not at all · 1=1=A little bit · 2=2=Moderately · 3=3=Quite a bit … (5 options) | ✔ |  | [v1.0.0] | — |
| 17 | `feeling_jumpy` | Feeling jumpy or easily startled when you hear an unexpected noise? | radio | 0=0=Not at all · 1=1=A little bit · 2=2=Moderately · 3=3=Quite a bit … (5 options) | ✔ |  | [v1.0.0] | — |
| 18 | `irritable` | Being extremely irritable or angry to the point where you yelled at other people, got into fights, or destroyed things? | radio | 0=0=Not at all · 1=1=A little bit · 2=2=Moderately · 3=3=Quite a bit … (5 options) | ✔ |  | [v1.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `ptsd_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - PTSD Adult |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `ptsd_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - PTSD Adult |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `ptsd_origin`

<details><summary>PTSD Adult - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | PTSD Adult |
| [v4.8.0] | 2026-06-04 | Label | `PTSD Adult Origin` | `PTSD Adult - origin` |

</details>

### `ptsd_via`

<details><summary>PTSD Adult - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | PTSD Adult |
| [v4.8.0] | 2026-06-04 | Label | `PTSD Adult via` | `PTSD Adult - via` |

</details>

### `ptsd_language`

<details><summary>PTSD Adult - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | PTSD Adult |
| [v4.8.0] | 2026-06-04 | Label | `PTSD Adult Language` | `PTSD Adult - Language` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
