<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Data Dissemination

**Form name:** `data_dissemination` · **Category:** General · **Status:** 🟢 Active  
**Introduced:** [v3.15.0] (2024-10-07) · **Last changed:** [v4.3.0] (2025-10-24)  
**Fields:** 📋 5 in REDCap · ⚫ 0 removed · ✏️ 1 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| 1 | `exclude_participant` | Exclude Participant and their data from Bridge2AI Data Dissemination? | radio | yes=Yes · no=No | ✔ |  | [v3.15.0] | — |
| 2 | `exclude_reason` | Check all that apply | checkbox | missing_consent=Re-consent required · incomplete_data_collection_acoustic_tasks=Incomplete Data Collection - Acoustic T… · incomplete_data_collection_questionnaire_tasks=Incomplete Data Collection - Questionna… · missing_diagnosis=Missing Diagnosis … (9 options) | ✔ |  | [v3.15.0] | [v4.3.0] ([2×](#exclude_reason)) |
| 3 | `exclude_reason_other` | Please specify: | text | free text | ✔ |  | [v3.15.0] | — |
| 4 | `exclusion_date` | Date Data Exclusion was requested | text | `date_mdy` | ✔ |  | [v3.15.0] | — |
| 5 | `inclusion_date` | Date Data Inclusion was requested | text | `date_mdy` | ✔ |  | [v4.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `exclude_reason`

<details><summary>Check all that apply — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Data Dissemination |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 5 options | ✏️ `missing_consent`: Missing Consent Form → Missing Consent/Reconsent Form |
| [v4.3.0] | 2025-10-24 | Choices / calculation | 5 options | ➕ `incomplete_data_collection_acoustic_tasks`=Incomplete Data Collection - Acoustic T…, `incomplete_data_collection_questionnaire_tasks`=Incomplete Data Collection - Questionna…, `participant_lost_to_follow_up`=Participant lost to follow up, `participant_removed_from_eligibility`=Participant removed from Eligibility<br>✏️ `missing_consent`: Missing Consent/Reconsent Form → Re-consent required |

</details>

<!-- milestone links -->
[v3.15.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.15.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.3.0
