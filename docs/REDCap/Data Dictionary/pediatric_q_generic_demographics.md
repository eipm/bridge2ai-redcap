<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Pediatric — Demographics

**Form name:** `pediatric_q_generic_demographics` · **Category:** Pediatric · **Status:** 🟢 Active  
**Introduced:** [v3.15.0] (2024-10-07) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 25 in REDCap · ⚫ 13 removed · ✏️ 6 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `peds_demographics_session_id` | Session ID | text | free text | ✔ |  | [v3.15.0] | — |
| 2 | `peds_demographics_started_at` | Questionnaire Started At | text | free text |  | 🔒 | [v3.15.0] | — |
| 3 | `peds_demographics_completed_at` | Questionnaire Completed At | text | free text |  | 🔒 | [v3.15.0] | — |
| 4 | `peds_demographics_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v3.15.0] | — |
| 5 | `peds_demographics_origin` | Peds Demographics - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App · reproschema=Bridge2AI Reproschema | ✔ |  | [v4.7.0] | [v4.10.0] ([2×](#peds_demographics_origin)) |
| 6 | `peds_demographics_via` | Peds Demographics - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#peds_demographics_via)) |
| 7 | `peds_demographics_language` | Peds Demographics - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#peds_demographics_language)) |
| | **Address Information** | | | | | | | |
| 8 | `peds_zipcode` | Zipcode | text | free text |  | 🔒 | [v3.15.0] | [v4.0.0] ([1×](#peds_zipcode)) |
| 9 | `peds_country` | Country | dropdown | 1=USA · 2=Canada | ✔ |  | [v3.15.0] | — |
| | **Patient Demographics** | | | | | | | |
| 10 | `peds_gender_identity` | What is your gender identity? | radio | female=Female gender identity · male=Male gender identity · other=Other |  |  | [v3.15.0] | [v4.0.0] ([1×](#peds_gender_identity)) |
| 11 | `peds_other_gender_identity` | If you selected "other" for gender identity, please specify: | text | free text |  |  | [v3.15.0] | — |
| 12 | `peds_race` | Which race category best describes you? Choose all that apply | checkbox | 1=American Indian or Alaska Native · 2=Asian · 3=Black or African American · 4=Native Hawaiian or other Pacific Island… … (8 options) |  |  | [v3.15.0] | — |
| 13 | `peds_other_race_specify` | If race not listed above, please specify: | text | free text |  |  | [v3.15.0] | — |
| | **Primary Language** | | | | | | | |
| 14 | `peds_primary_language` | What language do you primarily speak? | radio | english=English · french=French · mandarinChinese=Mandarin Chinese · punjabi=Punjabi … (10 options) | ✔ |  | [v4.0.0] | — |
| 15 | `peds_other_primary_language` | If you selected "other" for primary language, please specify: | text | free text | ✔ |  | [v4.0.0] | — |
| | **First Language** | | | | | | | |
| 16 | `peds_first_language` | What was your first language? | radio | english=English · french=French · mandarinChinese=Mandarin Chinese · punjabi=Punjabi … (10 options) | ✔ |  | [v4.0.0] | — |
| 17 | `peds_other_first_language` | If you selected "other" for first language, please specify: | text | free text | ✔ |  | [v4.0.0] | — |
| | **Education** | | | | | | | |
| 18 | `peds_edu_level` | What is your highest level of education? | radio | 1=No formal education · 2=Some elementary school · 3=Some secondary or high school education · 4=High School or secondary school degree… … (6 options) | ✔ | 🔒 | [v3.15.0] | [v4.0.0] ([1×](#peds_edu_level)) |
| 19 | `peds_other_edu_level` | If you selected "other" level of education, please specify: | text | free text |  |  | [v3.15.0] | — |
| | **Disability Questions** | | | | | | | |
| 20 | `peds_hearing` | Are you deaf or do you have serious difficulty hearing? | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v3.15.0] | — |
| 21 | `peds_vision` | Are you blind or do you have serious difficulty seeing, even when wearing glasses? | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v3.15.0] | — |
| 22 | `peds_cognition` | Because of a physical, mental, or emotional condition, do you have serious difficulty concentrating, remembering, or making decisions? | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v3.15.0] | — |
| 23 | `peds_mobility` | Do you have serious difficulty walking or climbing stairs? | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v3.15.0] | — |
| 24 | `peds_self_care` | Do you have difficulty dressing or bathing? | radio | no=No · yes=Yes · noAnswer=Prefer not to answer |  |  | [v3.15.0] | — |
| | **Deprecated Fields** | | | | | | | |
| 25 | `peds_state_province` | [DEPRECATED] State/Province | text | free text |  |  | [v3.15.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `peds_demographics_origin`

<details><summary>Peds Demographics - origin — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.8.0] | 2026-06-04 | Label | `Peds Demographics Origin` | `Peds Demographics - origin` |
| [v4.10.0] | 2026-08-27 | Choices / calculation | 2 options | ➕ `reproschema`=Bridge2AI Reproschema |

</details>

### `peds_demographics_via`

<details><summary>Peds Demographics - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.8.0] | 2026-06-04 | Label | `Peds Demographics via` | `Peds Demographics - via` |

</details>

### `peds_demographics_language`

<details><summary>Peds Demographics - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.8.0] | 2026-06-04 | Label | `Peds Demographics Language` | `Peds Demographics - Language` |

</details>

### `peds_zipcode`

<details><summary>Zipcode — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | Section header | ∅ | `Address Information` |
|  |  | Field note | ∅ | `5 Digit for USA and 3 Digit for Canada` |

</details>

### `peds_gender_identity`

<details><summary>What is your gender identity? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 5 options | ➖ `nonBinary`=Non-binary or genderqueer gender identi…, `noAnswer`=Prefer not to answer |

</details>

### `peds_edu_level`

<details><summary>What is your highest level of education? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 12 options | ➖ `5`=Some college education, `6`=Associate's or technical degree complete, `7`=College or baccalaureate degree complete, `8`=Some post-baccalaureate education, `9`=Graduate or professional degree complete, `10`=Doctoral or post graduate education |

</details>

### `peds_state_province`

<details><summary>[DEPRECATED] State/Province — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |
| [v4.4.0] | 2026-03-02 | ♻️ Re-introduced | | Pediatric — Demographics |

</details>

### `peds_demographics_completed_by`

<details><summary>Who is completing this survey? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

### `peds_city`

<details><summary>City — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

### `peds_specify_gender_identity`

<details><summary>Please specify gender identity — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

### `peds_sexual_orientation`

<details><summary>What is your sexual orientation? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

### `peds_other_sex_orientation`

<details><summary>If you selected "other" for sexual orientation, please specify: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

### `peds_native_american_race`

<details><summary>American Indian or Alaska Native — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

### `peds_asian_race`

<details><summary>Asian — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

### `peds_black_race`

<details><summary>Black or African American — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

### `peds_pacific_islander_race`

<details><summary>Native Hawaiian or other Pacific Islander — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

### `peds_white_race`

<details><summary>White — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

### `peds_canadian_race`

<details><summary>Canadian Indigenous or Aboriginal — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

### `peds_ethnicity`

<details><summary>What is your ethnic or cultural origin? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

### `peds_hispanic_latino_selection`

<details><summary>Check all that apply — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Demographics |
| [v4.0.0] | 2025-08-19 | ⚫ Removed | Pediatric — Demographics |  |

</details>

## ⚫ Removed Fields

Variables that were once in this instrument and are no longer in the REDCap dictionary.

| # | Variable | Label (last known) | Type | Introduced | Removed | Replaced by |
| :-: | :-- | :-- | :-- | :-: | :-: | :-- |
| 1 | [`peds_demographics_completed_by`](#peds_demographics_completed_by) | Who is completing this survey? | checkbox | [v3.15.0] | [v4.0.0] | — |
| 2 | [`peds_city`](#peds_city) | City | text | [v3.15.0] | [v4.0.0] | — |
| 3 | [`peds_specify_gender_identity`](#peds_specify_gender_identity) | Please specify gender identity | radio | [v3.15.0] | [v4.0.0] | — |
| 4 | [`peds_sexual_orientation`](#peds_sexual_orientation) | What is your sexual orientation? | radio | [v3.15.0] | [v4.0.0] | — |
| 5 | [`peds_other_sex_orientation`](#peds_other_sex_orientation) | If you selected "other" for sexual orientation, please specify: | text | [v3.15.0] | [v4.0.0] | — |
| 6 | [`peds_native_american_race`](#peds_native_american_race) | American Indian or Alaska Native | checkbox | [v3.15.0] | [v4.0.0] | — |
| 7 | [`peds_asian_race`](#peds_asian_race) | Asian | checkbox | [v3.15.0] | [v4.0.0] | — |
| 8 | [`peds_black_race`](#peds_black_race) | Black or African American | checkbox | [v3.15.0] | [v4.0.0] | — |
| 9 | [`peds_pacific_islander_race`](#peds_pacific_islander_race) | Native Hawaiian or other Pacific Islander | checkbox | [v3.15.0] | [v4.0.0] | — |
| 10 | [`peds_white_race`](#peds_white_race) | White | checkbox | [v3.15.0] | [v4.0.0] | — |
| 11 | [`peds_canadian_race`](#peds_canadian_race) | Canadian Indigenous or Aboriginal | checkbox | [v3.15.0] | [v4.0.0] | — |
| 12 | [`peds_ethnicity`](#peds_ethnicity) | What is your ethnic or cultural origin? | radio | [v3.15.0] | [v4.0.0] | — |
| 13 | [`peds_hispanic_latino_selection`](#peds_hispanic_latino_selection) | Check all that apply | checkbox | [v3.15.0] | [v4.0.0] | — |

<!-- milestone links -->
[v3.15.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.15.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.4.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
