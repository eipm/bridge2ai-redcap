<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Contact Information

**Form name:** `subjectparticipant_contact_information` · **Category:** General · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.0.0] (2025-08-19)  
**Fields:** 📋 7 in REDCap · ⚫ 0 removed · ✏️ 6 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Contact Information** | | | | | | | |
| 1 | `participant_study_id` | Participant Study ID | text | free text |  | 🔒 | [v4.0.0] | — |
| 2 | `first_name` | First Name | text | free text |  | 🔒 | [v1.0.0] | [v4.0.0] ([1×](#first_name)) |
| 3 | `last_name` | Last Name | text | free text |  | 🔒 | [v1.0.0] | [v4.0.0] ([1×](#last_name)) |
| 4 | `dob` | What is your date of birth? | text | `date_ymd` |  | 🔒 | [v1.0.0] | [v4.0.0] ([1×](#dob)) |
| 5 | `phone_number` | Phone Number | text | free text |  | 🔒 | [v1.0.0] | [v3.25.0] ([2×](#phone_number)) |
| 6 | `email` | Email | text | `email` |  | 🔒 | [v1.0.0] | [v3.25.0] ([1×](#email)) |
| 7 | `contact_info_stored` | [DEPRECATED] I want my contact information to be kept in a repository for this study which can be used to contact me to ask me to enroll in… | yesno | 1=Yes · 0=No |  |  | [v1.0.0] | [v4.0.0] ([2×](#contact_info_stored)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `first_name`

<details><summary>First Name — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Contact Information |
| [v4.0.0] | 2025-08-19 | Section header | `Contact Information` | ∅ |
|  |  | Required | Yes | No |

</details>

### `last_name`

<details><summary>Last Name — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Contact Information |
| [v4.0.0] | 2025-08-19 | Required | Yes | No |

</details>

### `dob`

<details><summary>What is your date of birth? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Contact Information |
| [v4.0.0] | 2025-08-19 | Required | Yes | No |

</details>

### `phone_number`

<details><summary>Phone Number — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Contact Information |
| [v3.0.0] | 2023-12-08 | Validation | `phone` | ∅ |
| [v3.25.0] | 2025-04-29 | Required | Yes | No |

</details>

### `email`

<details><summary>Email — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Contact Information |
| [v3.25.0] | 2025-04-29 | Required | Yes | No |

</details>

### `contact_info_stored`

<details><summary>[DEPRECATED] I want my contact information to be kept in a repository for this study whic… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Contact Information |
| [v3.11.1] | 2024-07-30 | Label | `I want my contact information to be kept in a repository for this study which can be used to contact me to ask me to enroll in further studies or return import…` | `I want my contact information to be kept in a repository for this study which can be used to contact me to ask me to enroll in further studies or return import…` |
| [v4.0.0] | 2025-08-19 | Label | `I want my contact information to be kept in a repository for this study which can be used to contact me to ask me to enroll in further studies or return import…` | `[DEPRECATED] I want my contact information to be kept in a repository for this study which can be used to contact me to ask me to enroll in further studies or…` |
|  |  | Required | Yes | No |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.11.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.11.1
[v3.25.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.25.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
