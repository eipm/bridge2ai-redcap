<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Neuro — Alzheimer's, MCI, and Other Dementias

**Form name:** `d_neuro_alzheimers_disease_mild_cognitive_impairme` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.0.0] (2023-12-08) · **Last changed:** [v4.1.0] (2025-09-17)  
**Fields:** 📋 29 in REDCap · ⚫ 0 removed · ✏️ 6 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `diagnosis_neurological_and_neurogenerative_disorde` | `d_neuro_alzheimers_disease_mild_cognitive_impairme` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnosis_alz_dementia_mci_gsd` | Does the participant have Major Neurocognitive Disorder - Alzheimer's Type, Mild Cognitive Impairment or other types of dementia? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.1.0] | — |
| 2 | `diagnosis_alz_dementia_mci_gsd_confirmation_method` | How was this diagnosis confirmed? (Check all that apply) | checkbox | clinical_history=Clinical History · functional_inventory=Functional Inventory · cognitive_testing=Cognitive Testing · blood_biomarkers=Blood Biomarkers … (5 options) | ✔ |  | [v4.1.0] | — |
| 3 | `diagnosis_alz_dementia_mci_gsd_confirmation_method_other` | Please specify: | text | free text | ✔ |  | [v4.1.0] | — |
| | **Does the participant have Major Neurocognitive Disorder - Alzheimer's Type, Mild Cognitive Impairment or other types of…** | | | | | | | |
| 4 | `diagnosis_alz_dementia_mci_gsd_clinical_history` | Clinical history: | text | free text |  |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_alz_dementia_mci_gsd_clinical_history)) |
| 5 | `diagnosis_alz_dementia_mci_gsd_functional_inventory` | Functional Inventory: | text | free text |  |  | [v3.0.0] | — |
| 6 | `diagnosis_alz_dementia_mci_gsd_cognitive_testing` | Cognitive Testing: | text | free text |  |  | [v3.0.0] | — |
| 7 | `diagnosis_alz_dementia_mci_gsd_other_investigations` | Other investigations: | text | free text |  |  | [v3.0.0] | — |
| 8 | `diagnosis_alz_dementia_mci_causes` | Have you excluded other causes of cognitive/functional changes (and/or other subtypes)? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_alz_dementia_mci_causes)) |
| | **2. Disease Type** | | | | | | | |
| 9 | `diagnosis_alz_dementia_mci_dt` | Specify the disease type in the participant: | radio | mci=Mild Cognitive Impairment (MCI) · ad=Typical Alzheimer's Disease (AD) · ftd=Frontotemporal Dementia (FTD) · lbd=Lewy Body Dementia (LBD) … (7 options) | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_alz_dementia_mci_dt)) |
| 10 | `diagnosis_alz_dementia_mci_dt_other` | If you selected "other", please specify: | text | free text | ✔ |  | [v3.0.0] | — |
| | **3. Etiology** | | | | | | | |
| 11 | `diagnosis_alz_dementia_mci_etiology` | What is the suspected or known etiology in the participant? | checkbox | genetic_factors=Genetic factors · age_related_changes=Age-related changes · other_medical_conditions=Other medical conditions (e.g., vascula… · substance_related=Substance-related (e.g., alcohol-induce… … (5 options) | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_alz_dementia_mci_etiology)) |
| 12 | `diagnosis_alz_dementia_mci_etiology_gf` | Genetic Factors Subcategory | checkbox | familial_alzheimers_disease=Familial Alzheimer's disease (e.g., mut… · apolipoprotein_e=Apolipoprotein E (APOE) ε4 allele · other_genetic_factors=Other genetic factors | ✔ |  | [v3.0.0] | — |
| 13 | `diagnosis_alz_dementia_mci_etiology_gf_other` | If you selected "Other genetic factors", please specify: | text | free text | ✔ |  | [v3.0.0] | — |
| 14 | `diagnosis_alz_dementia_mci_etiology_other_medical_conditions` | If you selected "other medical conditions", please specify: | text | free text | ✔ |  | [v3.0.0] | — |
| 15 | `diagnosis_alz_dementia_mci_etiology_other` | If you selected "other", please specify: | text | free text | ✔ |  | [v3.0.0] | — |
| | **4. Disease Severity** | | | | | | | |
| 16 | `diagnosis_alz_dementia_mci_ds` | What is the current stage/severity of cognitive impairment or dementia in the participant? | checkbox | mci=Mild cognitive impairment (MCI) · cdr=Clinical dementia rating (CDR) staging | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_alz_dementia_mci_ds)) |
| 17 | `diagnosis_alz_dementia_mci_ds_cdr` | Clinical dementia rating (CDR) staging subcategory: | radio | cdr0_5=CDR 0.5 (Very mild impairment) · cdr1=CDR 1 (Mild impairment) · cdr2=CDR 2 (Moderate impairment) · cdr3=CDR 3 (Severe impairment) | ✔ |  | [v3.0.0] | — |
| | **5. Cognitive Assessment (must fill at least one)** | | | | | | | |
| 18 | `diagnosis_alz_dementia_mci_ca_rudas_score` | Rowland Universal Dementia Assessment Scale (RUDAS) score: | text | free text |  |  | [v3.0.0] | — |
| 19 | `diagnosis_alz_dementia_mci_ca_mmse_score` | Mini-Mental State Examination (MMSE) score: | text | free text |  |  | [v3.0.0] | — |
| 20 | `diagnosis_alz_dementia_mci_ca_moca_score` | Montreal Cognitive Assessment (MoCA) score: | text | free text |  |  | [v3.0.0] | — |
| 21 | `diagnosis_alz_dementia_mci_ca_adas_cog_score` | Alzheimer's Disease Assessment Scale-Cognitive Subscale (ADAS-Cog) score: | text | free text |  |  | [v3.0.0] | — |
| 22 | `diagnosis_alz_dementia_mci_ca_other` | Other cognitive assessment tool (Please Specify): | text | free text |  |  | [v3.0.0] | — |
| 23 | `diagnosis_alz_dementia_mci_ca_other_score` | Other cognitive assessment tool score: | text | free text |  |  | [v3.0.0] | — |
| | **6. Treatment Obtained** | | | | | | | |
| 24 | `diagnosis_alz_dementia_mci_treatment_obtained` | Has the participant undergone any treatment for Alzheimer's disease or cognitive impairment or other types of dementia? | radio | yes=Yes · no=No | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_alz_dementia_mci_treatment_obtained)) |
| 25 | `diagnosis_alz_dementia_mci_treatment_obtained_yes` | Yes | checkbox | medications=Medications · npi=Non-pharmacological interventions | ✔ |  | [v3.0.0] | — |
| 26 | `diagnosis_alz_dementia_mci_treatment_obtained_yes_medications` | Medications: | checkbox | cholinesterase_inhibitors=Cholinesterase inhibitors (e.g., Donepe… · nmda_receptor_antagonist=NMDA receptor antagonist (e.g., Memanti… · other=Other | ✔ |  | [v3.0.0] | — |
| 27 | `diagnosis_alz_dementia_mci_treatment_obtained_yes_medications_other` | If you selected "Other", please specify: | text | free text | ✔ |  | [v3.0.0] | — |
| 28 | `diagnosis_alz_dementia_mci_treatment_obtained_yes_npi` | Non-pharmacological interventions: | checkbox | day_program=Day program · cognitive_simulation_therapy=Cognitive stimulation therapy · reality_orientation_therapy=Reality orientation therapy · reminiscence_therapy=Reminiscence therapy … (7 options) | ✔ |  | [v3.0.0] | — |
| 29 | `diagnosis_alz_dementia_mci_treatment_obtained_yes_npi_other` | If you selected "Other", please specify: | text | free text | ✔ |  | [v3.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_alz_dementia_mci_gsd_clinical_history`

<details><summary>Clinical history: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological and Neurogenerative Disorders - Alzheimer's disease, Mild Cognitive Impairment and other types of Dementia |
| [v4.1.0] | 2025-09-17 | Section header | `1. Gold Standard Diagnosis Does the patient have Major Neurocognitive Disorder - Alzheimer's Type, Mild Cognitive Impairment or other types of dementia confirm…` | `Does the participant have Major Neurocognitive Disorder - Alzheimer's Type, Mild Cognitive Impairment or other types of dementia confirmed by going through (mu…` |

</details>

### `diagnosis_alz_dementia_mci_causes`

<details><summary>Have you excluded other causes of cognitive/functional changes (and/or other subtypes)? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological and Neurogenerative Disorders - Alzheimer's disease, Mild Cognitive Impairment and other types of Dementia |
| [v4.1.0] | 2025-09-17 | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_alz_dementia_mci_dt`

<details><summary>Specify the disease type in the participant: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological and Neurogenerative Disorders - Alzheimer's disease, Mild Cognitive Impairment and other types of Dementia |
| [v4.1.0] | 2025-09-17 | Label | `Specify the disease type in the patient:` | `Specify the disease type in the participant:` |

</details>

### `diagnosis_alz_dementia_mci_etiology`

<details><summary>What is the suspected or known etiology in the participant? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological and Neurogenerative Disorders - Alzheimer's disease, Mild Cognitive Impairment and other types of Dementia |
| [v4.1.0] | 2025-09-17 | Label | `What is the suspected or known etiology in the patient?` | `What is the suspected or known etiology in the participant?` |

</details>

### `diagnosis_alz_dementia_mci_ds`

<details><summary>What is the current stage/severity of cognitive impairment or dementia in the participant? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological and Neurogenerative Disorders - Alzheimer's disease, Mild Cognitive Impairment and other types of Dementia |
| [v4.1.0] | 2025-09-17 | Label | `What is the current stage/severity of cognitive impairment or dementia in the patient?` | `What is the current stage/severity of cognitive impairment or dementia in the participant?` |

</details>

### `diagnosis_alz_dementia_mci_treatment_obtained`

<details><summary>Has the participant undergone any treatment for Alzheimer's disease or cognitive impairme… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological and Neurogenerative Disorders - Alzheimer's disease, Mild Cognitive Impairment and other types of Dementia |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment for Alzheimer's disease or cognitive impairment or other types of dementia?` | `Has the participant undergone any treatment for Alzheimer's disease or cognitive impairment or other types of dementia?` |

</details>

<!-- milestone links -->
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
