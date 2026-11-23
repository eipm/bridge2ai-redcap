<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Neuro — Amyotrophic Lateral Sclerosis (ALS)

**Form name:** `d_neuro_amyotrophic_lateral_sclerosis_als` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.0.0] (2023-12-08) · **Last changed:** [v4.1.0] (2025-09-17)  
**Fields:** 📋 28 in REDCap · ⚫ 0 removed · ✏️ 6 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `diagnosis_neurological_and_neurogenerative_di_5967` | `d_neuro_amyotrophic_lateral_sclerosis_als` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnosis_als_gsd` | Does the participant have Amyotrophic Lateral Sclerosis (ALS)? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.1.0] | — |
| 2 | `diagnosis_als_gsd_confirmation_method` | How was this diagnosis confirmed? (Check all that apply) | checkbox | progressive_motor_impairment=Progressive motor impairment documented… · presence_of_umn_lmn_signs=Presence of UMN and LMN signs in at lea… · investigations_excluding_disease_processes=Investigations excluding other disease… | ✔ |  | [v4.1.0] | — |
| | **Does the participant meet the diagnostic criteria for Amyotrophic Lateral Sclerosis (ALS) based on:** | | | | | | | |
| 3 | `diagnosis_als_gsd_category_1` | (1) Progressive motor impairment documented by history or repeated clinical assessment, preceded by normal motor function; | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_als_gsd_category_1)) |
| 4 | `diagnosis_als_gsd_category_2` | (2) presence of UMN and LMN signs in at least 1 body region (with UMN and LMN dysfunction noted in the same body region if only one body re… | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.0.0] | — |
| 5 | `diagnosis_als_gsd_category_3` | (3) investigations excluding other disease processes. | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.0.0] | — |
| 6 | `diagnosis_als_gsd_calculation` | Does the participant meet the diagnostic criteria for Amyotrophic Lateral Sclerosis (ALS) based on the criteria above? | text | free text |  |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_als_gsd_calculation)) |
| | **2. Type of ALS** | | | | | | | |
| 7 | `diagnosis_als_disease_subtype` | Specify the type of ALS in the participant: | radio | sporadicAls=Sporadic ALS · familialAls=Familial ALS · spinalAls=Spinal/limb-onset ALS · bulbarAls=Bulbar-onset ALS | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_als_disease_subtype)) |
| 8 | `diagnosis_als_disease_subtype_familial` | If you selected "Familial ALS", please specify the genetic mutation if known: | text | free text |  |  | [v3.0.0] | — |
| | **3. Etiology** | | | | | | | |
| 9 | `diagnosis_als_etiology` | What is the suspected or known etiology of ALS in the participant? | checkbox | genetic_factors=Genetic factors · environmental_factors=Environmental factors | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_als_etiology)) |
| 10 | `diagnosis_als_etiology_genetic_factors` | Genetic Factors | checkbox | c9orf72=C9orf72 mutation · sod1=SOD1 mutation · other=Other genetic factors | ✔ |  | [v3.0.0] | — |
| 11 | `diagnosis_als_etiology_genetic_factors_other` | If you selected "Other genetic factors", please specify: | text | free text | ✔ |  | [v3.0.0] | — |
| 12 | `diagnosis_als_etiology_environmental_factors` | If you selected "Environmental factors", please specify: | text | free text | ✔ |  | [v3.0.0] | — |
| | **4. Clinical Presentation** | | | | | | | |
| 13 | `diagnosis_als_cp` | Describe the clinical features and symptoms of ALS in the participant: | checkbox | upper_motor_neuron=Upper Motor Neuron Signs (e.g., spastic… · lower_motor_neuron=Lower Motor Neuron Signs (e.g., muscle… · bulbar_symptoms=Bulbar Symptoms (e.g., dysarthria, dysp… · respiratory_involvement=Respiratory Involvement | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_als_cp)) |
| | **5. Disease Progression** | | | | | | | |
| 14 | `diagnosis_als_dp` | Please provide information on the current stage and progression of ALS: | radio | earlyStage=Early Stage · intermediateStage=Intermediate Stage · advancedStage=Advanced Stage | ✔ |  | [v3.0.0] | — |
| | **6. Neurological Assessment Please provide results from relevant neurological assessments:** | | | | | | | |
| 15 | `diagnosis_als_na_alsfrs_r_score` | Revised ALS Functional Rating Scale (ALSFRS-R) score: | text | free text |  |  | [v3.0.0] | — |
| 16 | `diagnosis_als_na_fvc_percentage` | Forced Vital Capacity (FVC) percentage (if measured): | text | free text |  |  | [v3.0.0] | — |
| 17 | `diagnosis_als_na_other` | Other neurological assessment (please specify): | text | free text |  |  | [v3.0.0] | — |
| | **7. Imaging and Diagnostic Tests** | | | | | | | |
| 18 | `diagnosis_als_idt_emg_ncs` | Electromyography (EMG) and Nerve Conduction Studies (NCS): | text | free text |  |  | [v3.0.0] | — |
| 19 | `diagnosis_als_idt_mri` | Magnetic Resonance Imaging (MRI) of the brain and spinal cord: | file | file upload |  |  | [v3.0.0] | — |
| 20 | `diagnosis_als_idt_lumbar_puncture` | Lumbar Puncture (if performed, specify findings): | text | free text |  |  | [v3.0.0] | — |
| 21 | `diagnosis_als_idt_genetic_testing` | Genetic testing (if applicable, specify results): | text | free text |  |  | [v3.0.0] | — |
| 22 | `diagnosis_als_idt_other` | Other diagnostic tests (please specify): | text | free text |  |  | [v3.0.0] | — |
| | **8. Treatment and Management** | | | | | | | |
| 23 | `diagnosis_als_treatment_and_management` | Has the participant undergone any treatment or interventions for ALS? | radio | yes=Yes · no=No | ✔ |  | [v3.0.0] | [v4.1.0] ([1×](#diagnosis_als_treatment_and_management)) |
| 24 | `diagnosis_als_treatment_and_management_yes` | Yes | checkbox | medications=Medications · supportive_care=Supportive Care | ✔ |  | [v3.0.0] | — |
| 25 | `diagnosis_als_treatment_and_management_yes_medications` | Medications (if applicable): | checkbox | riluzole=Riluzole · edaravone=Edaravone · sodium=Sodium phenylbutyrate/taurursodiol · tofersen=Tofersen … (6 options) | ✔ |  | [v3.0.0] | — |
| 26 | `diagnosis_als_treatment_and_management_yes_medications_other` | If you selected "Other", please specify: | text | free text | ✔ |  | [v3.0.0] | — |
| 27 | `diagnosis_als_treatment_and_management_yes_supportive_care` | Supportive Care: | checkbox | physical_therapy=Physical therapy · occupational_therapy=Occupational therapy · speech_therapy=Speech therapy · respiratory_support=Respiratory support (e.g., non-invasive… … (7 options) | ✔ |  | [v3.0.0] | — |
| 28 | `diagnosis_als_treatment_and_management_yes_supportive_care_other` | If you selected "Other", please specify: | text | free text | ✔ |  | [v3.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_als_gsd_category_1`

<details><summary>(1) Progressive motor impairment documented by history or repeated clinical assessment, p… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Amyotrophic Lateral Sclerosis (ALS) |
| [v4.1.0] | 2025-09-17 | Section header | `1. Gold Standard Diagnosis Does the patient meet the diagnostic criteria for Amyotrophic Lateral Sclerosis (ALS) based on:` | `Does the participant meet the diagnostic criteria for Amyotrophic Lateral Sclerosis (ALS) based on:` |

</details>

### `diagnosis_als_gsd_calculation`

<details><summary>Does the participant meet the diagnostic criteria for Amyotrophic Lateral Sclerosis (ALS)… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Amyotrophic Lateral Sclerosis (ALS) |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient meet the diagnostic criteria for Amyotrophic Lateral Sclerosis (ALS) based on the criteria above?` | `Does the participant meet the diagnostic criteria for Amyotrophic Lateral Sclerosis (ALS) based on the criteria above?` |

</details>

### `diagnosis_als_disease_subtype`

<details><summary>Specify the type of ALS in the participant: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Amyotrophic Lateral Sclerosis (ALS) |
| [v4.1.0] | 2025-09-17 | Label | `Specify the type of ALS in the patient:` | `Specify the type of ALS in the participant:` |

</details>

### `diagnosis_als_etiology`

<details><summary>What is the suspected or known etiology of ALS in the participant? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Amyotrophic Lateral Sclerosis (ALS) |
| [v4.1.0] | 2025-09-17 | Label | `What is the suspected or known etiology of ALS in the patient?` | `What is the suspected or known etiology of ALS in the participant?` |

</details>

### `diagnosis_als_cp`

<details><summary>Describe the clinical features and symptoms of ALS in the participant: — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Amyotrophic Lateral Sclerosis (ALS) |
| [v4.1.0] | 2025-09-17 | Label | `Describe the clinical features and symptoms of ALS in the patient:` | `Describe the clinical features and symptoms of ALS in the participant:` |

</details>

### `diagnosis_als_treatment_and_management`

<details><summary>Has the participant undergone any treatment or interventions for ALS? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis - Neurological And Neurogenerative Disorders - Amyotrophic Lateral Sclerosis (ALS) |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment or interventions for ALS?` | `Has the participant undergone any treatment or interventions for ALS?` |

</details>

<!-- milestone links -->
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
