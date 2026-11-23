<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Resp — Unexplained Chronic Cough

**Form name:** `d_resp_unexplained_chronic_cough` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.11.0] (2024-07-22) · **Last changed:** [v4.1.0] (2025-09-17)  
**Fields:** 📋 17 in REDCap · ⚫ 0 removed · ✏️ 13 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Initial screening criteria** | | | | | | | |
| 1 | `diagnosis_ucc_persisted` | Does the participant have Unxeplained Chronic Cough for longer than eight weeks? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.11.0] | [v4.1.0] ([1×](#diagnosis_ucc_persisted)) |
| 2 | `diagnosis_ucc_hsoe` | Does the participant have a history of smoking or occupational exposures? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.11.0] | [v4.1.0] ([1×](#diagnosis_ucc_hsoe)) |
| 3 | `diagnosis_ucc_hspd` | Does the participant have a history of pulmonary disease? (Select all that apply) | checkbox | lung_cancer=Lung cancer · copd=COPD · asthma=Asthma · tb_infection=TB infection … (8 options) |  |  | [v3.11.0] | [v4.1.0] ([2×](#diagnosis_ucc_hspd)) |
| 4 | `diagnosis_ucc_cuae` | Has the chronic cough remained unexplained after evaluation and therapeutic intervention? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.11.0] | [v4.1.0] ([1×](#diagnosis_ucc_cuae)) |
| 5 | `diagnosis_ucc_hcxob` | Has the participant had a chest x-ray, CT chest or bronchoscopy? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.11.0] | [v4.1.0] ([1×](#diagnosis_ucc_hcxob)) |
| 6 | `diagnosis_ucc_cxcob` | Select all that apply | checkbox | chest_xray=Chest X-ray · ct_chest=CT Chest · bronchoscopy=Bronchoscopy | ✔ |  | [v3.11.0] | — |
| 7 | `diagnosis_ucc_huse` | Has the participant undergone spirometry evaluation (pulmonary function tests)? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.11.0] | [v4.1.0] ([1×](#diagnosis_ucc_huse)) |
| 8 | `diagnosis_ucc_oai` | Is the participant on ACE-inhibitors (example: lisinopril; captopril)? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.11.0] | [v4.1.0] ([1×](#diagnosis_ucc_oai)) |
| 9 | `diagnosis_ucc_pdapc` | Has postnasal drainage been addressed as a potential cause of the cough (through nasal sprays and antihistamines)? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.11.0] | [v4.1.0] ([1×](#diagnosis_ucc_pdapc)) |
| 10 | `diagnosis_ucc_gediapc` | Has gastro-esophageal disease been investigated as a possible cause of the cough? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.11.0] | [v4.1.0] ([1×](#diagnosis_ucc_gediapc)) |
| 11 | `diagnosis_ucc_atot` | How was it investigated? (Select all that apply) | checkbox | trial_of_proton_pump_inhibitor=Trial of proton pump inhibitor · phimpedance_probe_or_bravo_probe=pH-impedance probe or Bravo probe · egd_or_tne=EGD/TNE · other=Other (H2-blocker, lifestyle change, al… | ✔ |  | [v3.11.0] | [v3.20.0] ([1×](#diagnosis_ucc_atot)) |
| 12 | `diagnosis_ucc_huatot` | Has the participant undergone allergy testing or allergy therapy? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.11.0] | [v4.1.0] ([1×](#diagnosis_ucc_huatot)) |
| 13 | `diagnosis_ucc_hurada` | Has the participant undergone assessment that includes bronchial hyperresponsiveness and eosinophilic bronchitis (sputum eosinophilia or ex… | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.11.0] | [v4.1.0] ([1×](#diagnosis_ucc_hurada)) |
| 14 | `diagnosis_ucc_rada` | Result | radio | positive=Positive for reactive airway disease · negative=Negative for reactive airway disease | ✔ |  | [v3.11.0] | — |
| | **2. Treatment obtained** | | | | | | | |
| 15 | `diagnosis_ucc_at` | Has the participant undergone any treatment for this condition? | radio | yes=Yes · no=No · notCertain=Not Certain | ✔ |  | [v3.11.0] | [v4.1.0] ([1×](#diagnosis_ucc_at)) |
| 16 | `diagnosis_ucc_at_s` | Select all that apply | checkbox | multimodality_speech_pathology_therapy=Therapeutic trial of multimodality spee… · neuromodulator=Therapeutic trial of gabapentin/amitrip… · superior_laryngeal_nerve_block=Unilateral or bilateral superior laryng… · other=Other | ✔ |  | [v3.11.0] | — |
| 17 | `diagnosis_ucc_at_s_other` | Please Specify | text | free text |  |  | [v3.11.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_ucc_persisted`

<details><summary>Does the participant have Unxeplained Chronic Cough for longer than eight weeks? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v4.1.0] | 2025-09-17 | Label | `Has the cough persisted longer than eight weeks?` | `Does the participant have Unxeplained Chronic Cough for longer than eight weeks?` |
|  |  | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_ucc_hsoe`

<details><summary>Does the participant have a history of smoking or occupational exposures? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have a history of smoking or occupational exposures?` | `Does the participant have a history of smoking or occupational exposures?` |
|  |  | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_ucc_hspd`

<details><summary>Does the participant have a history of pulmonary disease? (Select all that apply) — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v3.13.0] | 2024-08-16 | Required | Yes | No |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have a history of pulmonary disease? (Select all that apply)` | `Does the participant have a history of pulmonary disease? (Select all that apply)` |

</details>

### `diagnosis_ucc_cuae`

<details><summary>Has the chronic cough remained unexplained after evaluation and therapeutic intervention? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v4.1.0] | 2025-09-17 | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_ucc_hcxob`

<details><summary>Has the participant had a chest x-ray, CT chest or bronchoscopy? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient had a chest x-ray, CT chest or bronchoscopy?` | `Has the participant had a chest x-ray, CT chest or bronchoscopy?` |
|  |  | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_ucc_huse`

<details><summary>Has the participant undergone spirometry evaluation (pulmonary function tests)? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone spirometry evaluation (pulmonary function tests)?` | `Has the participant undergone spirometry evaluation (pulmonary function tests)?` |
|  |  | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_ucc_oai`

<details><summary>Is the participant on ACE-inhibitors (example: lisinopril; captopril)? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v4.1.0] | 2025-09-17 | Label | `Is the patient on ACE-inhibitors (example: lisinopril; captopril)?` | `Is the participant on ACE-inhibitors (example: lisinopril; captopril)?` |
|  |  | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_ucc_pdapc`

<details><summary>Has postnasal drainage been addressed as a potential cause of the cough (through nasal sp… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v4.1.0] | 2025-09-17 | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_ucc_gediapc`

<details><summary>Has gastro-esophageal disease been investigated as a possible cause of the cough? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v4.1.0] | 2025-09-17 | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_ucc_atot`

<details><summary>How was it investigated? (Select all that apply) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v3.20.0] | 2024-11-13 | Branching logic | `[diagnosis_ucc_huatot] = "yes"` | `[diagnosis_ucc_gediapc] = "yes"` |

</details>

### `diagnosis_ucc_huatot`

<details><summary>Has the participant undergone allergy testing or allergy therapy? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone allergy testing or allergy therapy?` | `Has the participant undergone allergy testing or allergy therapy?` |
|  |  | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_ucc_hurada`

<details><summary>Has the participant undergone assessment that includes bronchial hyperresponsiveness and… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone assessment that includes bronchial hyperresponsiveness and eosinophilic bronchitis (sputum eosinophilia or exhaled nitric oxide), or…` | `Has the participant undergone assessment that includes bronchial hyperresponsiveness and eosinophilic bronchitis (sputum eosinophilia or exhaled nitric oxide),…` |
|  |  | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_ucc_at`

<details><summary>Has the participant undergone any treatment for this condition? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.11.0] | 2024-07-22 | 🆕 Introduced | | Resp — Unexplained Chronic Cough |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment for this condition?` | `Has the participant undergone any treatment for this condition?` |

</details>

<!-- milestone links -->
[v3.11.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.11.0
[v3.13.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.13.0
[v3.20.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.20.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
