<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Basic Information

**Form name:** `subjectparticipant_basic_information` · **Category:** General · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 19 in REDCap · ⚫ 0 removed · ✏️ 13 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| 1 | `record_id` | Record ID | text | free text |  |  | [v1.0.0] | — |
| 2 | `age` | Age | text | free text |  |  | [v3.3.0] | [v4.4.0] ([2×](#age)) |
| 3 | `selected_language` | Language | radio | 1=English · 2=French · 3=Spanish | ✔ |  | [v1.0.0] | [v3.11.1] ([1×](#selected_language)) |
| 4 | `selected_language_2` | Language | radio | en-US=English · fr-CA=French · es-419=Spanish |  |  | [v4.0.0] | — |
| 5 | `consent_status` | Consent Status | radio | 1=Pending · 2=Consented · 3=Withdrawn Consent · 4=Removed From Eligibility | ✔ |  | [v1.0.0] | [v4.0.0] ([1×](#consent_status)) |
| 6 | `contact_participant` | Contact participant re: incidental findings? | radio | yes=Yes · no=No |  |  | [v3.8.0] | [v4.0.0] ([1×](#contact_participant)) |
| 7 | `consent_date` | Consent Date | text | `date_mdy` | ✔ | 🔒 | [v4.3.0] | — |
| 8 | `consent_method` | Consent Method | radio | paper=Paper Consent · econsent=eConsent | ✔ |  | [v3.2.0] | [v4.3.0] ([1×](#consent_method)) |
| 9 | `withdrawn_consent_reason` | Withdrawn Consent Reason | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#withdrawn_consent_reason)) |
| 10 | `withdrawn_consent_date` | Withdrawn Consent Date | text | `date_mdy` | ✔ | 🔒 | [v1.0.0] | [v4.3.0] ([2×](#withdrawn_consent_date)) |
| 11 | `is_feasibility_participant` | Is Feasibility Participant? | radio | yes=Yes · no=No | ✔ |  | [v3.2.0] | — |
| 12 | `is_remote_data_collection_enabled` | Is Remote Data Collection Enabled? | radio | yes=Yes · no=No | ✔ |  | [v3.24.0] | [v3.27.0] ([1×](#is_remote_data_collection_enabled)) |
| | **Enrollment Details** | | | | | | | |
| 13 | `enrolled` | Enrolled | yesno | 1=Yes · 0=No | ✔ |  | [v1.0.0] | — |
| 14 | `enrollment_reason` | Enrollment Reason To be completed when enrolling a person that declined initially. | text | free text |  | 🔒 | [v1.0.0] | [v3.11.1] ([2×](#enrollment_reason)) |
| 15 | `enrollment_institution` | Enrollment Institution | radio | mit=MIT · mt_sinai=Mt. Sinai · sickkids=SickKids · usf=USF … (6 options) | ✔ |  | [v1.0.0] | [v3.6.0] ([3×](#enrollment_institution)) |
| 16 | `researcher_email` | Researcher Email | text | `email` |  | 🔒 | [v1.0.0] | [v4.7.0] ([2×](#researcher_email)) |
| | **Data Collection Details** | | | | | | | |
| 17 | `participant_data_collection_origins` | Data Collection - origin(s) | checkbox | app=Bridge2AI App · website=Bridge2AI Web App · reproschema=Bridge2AI Reproschema |  |  | [v4.7.0] | [v4.10.0] ([2×](#participant_data_collection_origins)) |
| 18 | `participant_data_collection_via` | Data Collection - via | checkbox | data_collector=Data Collector · participant=Participant |  |  | [v4.7.0] | [v4.8.0] ([1×](#participant_data_collection_via)) |
| 19 | `api_updates_on_behalf_of` | API Updates on behalf of | text | `email` |  | 🔒 | [v4.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `age`

<details><summary>Age — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.3.0] | 2024-03-13 | 🆕 Introduced | | Contact Information |
| [v3.15.0] | 2024-10-07 | Instrument | Contact Information | Basic Information |
| [v4.4.0] | 2026-03-02 | Type | `calc` | `text` |
|  |  | Choices / calculation | `rounddown((datediff([dob],"today","y","ymd")),0)` | ∅ |

</details>

### `selected_language`

<details><summary>Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Basic Information |
| [v3.11.1] | 2024-07-30 | Choices / calculation | 3 options | ✏️ `2`: Español → French; `3`: Français → Spanish |

</details>

### `consent_status`

<details><summary>Consent Status — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Basic Information |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 3 options | ➕ `4`=Removed From Eligibility |

</details>

### `contact_participant`

<details><summary>Contact participant re: incidental findings? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.8.0] | 2024-06-20 | 🆕 Introduced | | Basic Information |
| [v4.0.0] | 2025-08-19 | Required | Yes | No |

</details>

### `consent_method`

<details><summary>Consent Method — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.2.0] | 2024-02-07 | 🆕 Introduced | | Basic Information |
| [v4.3.0] | 2025-10-24 | Choices / calculation | 3 options | ➖ `e_video_consent`=Video Consent |

</details>

### `withdrawn_consent_reason`

<details><summary>Withdrawn Consent Reason — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Basic Information |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `withdrawn_consent_date`

<details><summary>Withdrawn Consent Date — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Basic Information |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |
| [v4.3.0] | 2025-10-24 | Required | No | Yes |

</details>

### `is_remote_data_collection_enabled`

<details><summary>Is Remote Data Collection Enabled? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.24.0] | 2025-04-29 | 🆕 Introduced | | Basic Information |
| [v3.27.0] | 2025-06-02 | Annotation | ∅ | `@READONLY` |

</details>

### `enrollment_reason`

<details><summary>Enrollment Reason To be completed when enrolling a person that declined initially. — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Basic Information |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |
| [v3.11.1] | 2024-07-30 | Label | `Enrollment Reason To be completed when enrolling a person that declined initially.` | `Enrollment Reason To be completed when enrolling a person that declined initially.` |

</details>

### `enrollment_institution`

<details><summary>Enrollment Institution — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Basic Information |
| [v2.0.0] | 2023-11-15 | Choices / calculation | 3 options | ➕ `BCH`=BCH, `mt_sinai`=Mt. Sinai, `VUMC`=VUMC |
| [v3.0.0] | 2023-12-08 | Choices / calculation | 6 options | ➕ `bch`=BCH, `mit`=MIT, `usf`=USF, `vumc`=VUMC, `wcm`=WCM<br>➖ `BCH`=BCH, `MIT`=MIT, `USF`=USF, `VUMC`=VUMC, `WCM`=WCM |
| [v3.6.0] | 2024-06-10 | Choices / calculation | 6 options | ➕ `sickkids`=SickKids<br>➖ `bch`=BCH |

</details>

### `researcher_email`

<details><summary>Researcher Email — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Basic Information |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |
| [v4.7.0] | 2026-05-04 | Required | Yes | No |

</details>

### `participant_data_collection_origins`

<details><summary>Data Collection - origin(s) — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Basic Information |
| [v4.8.0] | 2026-06-04 | Label | `Data Collection Origin(s)` | `Data Collection - origin(s)` |
| [v4.10.0] | 2026-08-27 | Choices / calculation | 2 options | ➕ `reproschema`=Bridge2AI Reproschema |

</details>

### `participant_data_collection_via`

<details><summary>Data Collection - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Basic Information |
| [v4.8.0] | 2026-06-04 | Label | `Data Collection via` | `Data Collection - via` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v2.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v2.0.0
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.2.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v3.6.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.6.0
[v3.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.8.0
[v3.11.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.11.1
[v3.15.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.15.0
[v3.24.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.24.0
[v3.27.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.27.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.3.0
[v4.4.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.4.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
