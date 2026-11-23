<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Controls (healthy adults)

**Form name:** `d_control` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.8.0] (2024-06-20) · **Last changed:** [v4.1.0] (2025-09-17)  
**Fields:** 📋 2 in REDCap · ⚫ 0 removed · ✏️ 1 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| 1 | `diagnosis_c_ac` | Based on the assessment you made of the participant, and by hearing their voice, do you think this participant has any condition affecting… | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.8.0] | [v4.1.0] ([1×](#diagnosis_c_ac)) |
| 2 | `diagnosis_c_ac_specified` | Please specify: | text | free text |  |  | [v3.8.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_c_ac`

<details><summary>Based on the assessment you made of the participant, and by hearing their voice, do you t… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.8.0] | 2024-06-20 | 🆕 Introduced | | Controls (healthy adults) |
| [v4.1.0] | 2025-09-17 | Label | `Based on the assessment you made of the patient, and by hearing their voice, do you think this patient has any condition affecting their speech or voice?` | `Based on the assessment you made of the participant, and by hearing their voice, do you think this participant has any condition affecting their speech or voic…` |

</details>

<!-- milestone links -->
[v3.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.8.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
