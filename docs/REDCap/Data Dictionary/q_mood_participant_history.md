<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Participant History

> 🗄️ **Retired** from the Mood protocol in [v4.0.0] (2025-08-19). No new data is collected, but the fields stay in REDCap so data from earlier participants remains valid. · [Retired PDF (English)](<../../../docs/Adults/PDFs/en-us/Retired%20Questionnaire%20-%20PDFs/Mood/Q%20-%20Mood%20-%20Participant%20History%20-%20English.pdf>)

**Form name:** `q_mood_participant_history` · **Category:** Adult Questionnaires (Mood & Psychiatric) · **Status:** 🗄️ Retired  
**Introduced:** [v3.16.0] (2024-10-07) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 14 in REDCap · ⚫ 4 removed · ✏️ 3 changed since introduction

## 📋 Fields

_All fields below share the instrument's status: 🗄️ Retired._

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `mph_session_id` | Session ID | text | free text | ✔ |  | [v3.16.0] | — |
| 2 | `mph_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v3.16.0] | — |
| 3 | `mph_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v3.16.0] | — |
| 4 | `mph_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v3.16.0] | — |
| 5 | `mph_origin` | Mood Participant History - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#mph_origin)) |
| 6 | `mph_via` | Mood Participant History - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#mph_via)) |
| 7 | `mph_language` | Mood Participant History - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#mph_language)) |
| | **Medical and Psychiatric comorbidities** | | | | | | | |
| 8 | `mph_active_psy_medical_problems` | Please list any active psychiatric problems and medical problems. | text | free text |  |  | [v3.18.0] | — |
| 9 | `mph_hist_psy_medical_problems` | Please list any historical psychiatric problems and medical problems. | text | free text |  |  | [v3.18.0] | — |
| | **Treatment Obtained** | | | | | | | |
| 10 | `mph_prescribed_medication` | Have you ever been prescribed medication for mental or emotional problems (e.g., antidepressants, anxiolytics, antipsychotics, mood stabili… | radio | yes=Yes · no=No |  |  | [v3.16.0] | — |
| 11 | `mph_current_medication` | Please list any current psychiatric medications (to the best of your recollection), including medication names, dosage, and how many times… | notes | free text (long) |  |  | [v3.16.0] | — |
| 12 | `mph_previous_medication` | Please list any previous psychiatric medications (to the best of your recollection), including medication names, approximate dates you were… | notes | free text (long) |  |  | [v3.16.0] | — |
| 13 | `mph_see_mental_health_professional` | Have you ever seen a mental health professional for talk therapy (could include social workers, psychiatrists, etc.)? | radio | yes=Yes · no=No |  |  | [v3.16.0] | — |
| 14 | `mph_describe_psychotherapy` | Please briefly describe your psychotherapy history (e.g., dates, reasons for seeking therapy, etc.). | notes | free text (long) |  |  | [v3.16.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `mph_origin`

<details><summary>Mood Participant History - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Participant History |
| [v4.8.0] | 2026-06-04 | Label | `Mood Participant History Origin` | `Mood Participant History - origin` |

</details>

### `mph_via`

<details><summary>Mood Participant History - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Participant History |
| [v4.8.0] | 2026-06-04 | Label | `Mood Participant History via` | `Mood Participant History - via` |

</details>

### `mph_language`

<details><summary>Mood Participant History - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Participant History |
| [v4.8.0] | 2026-06-04 | Label | `Mood Participant History Language` | `Mood Participant History - Language` |

</details>

### `mph_active_psy_med_problems`

<details><summary>Please select any active psychiatric problems and medical problems (select all that apply… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.16.0] | 2024-10-07 | 🆕 Introduced | | Participant History |
| [v3.18.0] | 2024-10-23 | ⚫ Removed | Participant History |  |

</details>

### `mph_active_psy_med_prob_other`

<details><summary>Please specify — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.16.0] | 2024-10-07 | 🆕 Introduced | | Participant History |
| [v3.18.0] | 2024-10-23 | ⚫ Removed | Participant History |  |

</details>

### `mph_hist_psy_med_problems`

<details><summary>Please select any historical psychiatric problems and medical problems (select all that a… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.16.0] | 2024-10-07 | 🆕 Introduced | | Participant History |
| [v3.18.0] | 2024-10-23 | ⚫ Removed | Participant History |  |

</details>

### `mph_hist_psy_med_prob_other`

<details><summary>Please specify — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.16.0] | 2024-10-07 | 🆕 Introduced | | Participant History |
| [v3.18.0] | 2024-10-23 | ⚫ Removed | Participant History |  |

</details>

## ⚫ Removed Fields

Variables that were once in this instrument and are no longer in the REDCap dictionary.

| # | Variable | Label (last known) | Type | Introduced | Removed | Replaced by |
| :-: | :-- | :-- | :-- | :-: | :-: | :-- |
| 1 | [`mph_active_psy_med_problems`](#mph_active_psy_med_problems) | Please select any active psychiatric problems and medical problems (select all that apply). | checkbox | [v3.16.0] | [v3.18.0] | — |
| 2 | [`mph_active_psy_med_prob_other`](#mph_active_psy_med_prob_other) | Please specify | text | [v3.16.0] | [v3.18.0] | — |
| 3 | [`mph_hist_psy_med_problems`](#mph_hist_psy_med_problems) | Please select any historical psychiatric problems and medical problems (select all that apply). | checkbox | [v3.16.0] | [v3.18.0] | — |
| 4 | [`mph_hist_psy_med_prob_other`](#mph_hist_psy_med_prob_other) | Please specify | text | [v3.16.0] | [v3.18.0] | — |

<!-- milestone links -->
[v3.16.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.16.0
[v3.18.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.18.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
