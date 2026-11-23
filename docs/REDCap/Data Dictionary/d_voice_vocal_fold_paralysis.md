<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# D Voice Vocal Fold Paralysis

> ⚫ **Removed** from the REDCap dictionary in [v3.5.0] (2024-05-24). None of these variables exist in the current project; they are listed for data collected before then.

**Form name:** `d_voice_vocal_fold_paralysis` · **Category:** Adult Diagnoses · **Status:** ⚫ Removed  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v3.5.0] (2024-05-24)  
**Fields:** 📋 0 in REDCap · ⚫ 1 removed · ✏️ 0 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `diagnosis_voice_disorders_vocal_fold_paralysis` | `d_voice_vocal_fold_paralysis` |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_vfp_treatment`

<details><summary>Has the patient undergone any treatment for his condition? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Diagnosis - Voice Disorders - Vocal Fold Paralysis |
| [v3.5.0] | 2024-05-24 | ⚫ Removed | D Voice Vocal Fold Paralysis | ↪️ replaced by [`diagnosis_uvfp_treatment`](d_voice_unilateral_vocal_fold_paralysis.md#diagnosis_uvfp_treatment) — Was treatment type (surgery / speech therapy / none); now a yes/no question |

</details>

## ⚫ Removed Fields

Variables that were once in this instrument and are no longer in the REDCap dictionary.

| # | Variable | Label (last known) | Type | Introduced | Removed | Replaced by |
| :-: | :-- | :-- | :-- | :-: | :-: | :-- |
| 1 | [`diagnosis_vfp_treatment`](#diagnosis_vfp_treatment) | Has the patient undergone any treatment for his condition? | radio | [v1.0.0] | [v3.5.0] | [`diagnosis_uvfp_treatment`](d_voice_unilateral_vocal_fold_paralysis.md#diagnosis_uvfp_treatment) |

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.5.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.5.0
