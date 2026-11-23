<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Resp — Airway Stenosis

**Form name:** `d_resp_airway_stenosis` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.0.0] (2023-12-08) · **Last changed:** [v4.9.0] (2026-07-21)  
**Fields:** 📋 29 in REDCap · ⚫ 1 removed · ✏️ 17 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `diagnosis_respiratory_disorders_airway_stenosis` | `d_resp_airway_stenosis` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnosis_as_gsd` | Does the participant have airway stenosis confirmed by a laryngoscopy, bronchoscopy or CT imaging? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.0.0] | [v4.1.0] ([2×](#diagnosis_as_gsd)) |
| 2 | `diagnosis_as_gsd_yes` | Confirmed by | checkbox | bronchoscopy=Confirmed by bronchoscopy or laryngosco… · ct=Confirmed by CT imaging | ✔ |  | [v3.0.0] | [v3.3.0] ([1×](#diagnosis_as_gsd_yes)) |
| 3 | `diagnosis_as_pft` | Has the participant had pulmonary function testing within the past 3 months? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.0.0] | [v4.1.0] ([3×](#diagnosis_as_pft)) |
| 4 | `diagnosis_as_pft_document` | Please upload the PFT document | file | file upload |  |  | [v3.0.0] | — |
| | **2. Disease Subtype** | | | | | | | |
| 5 | `diagnosis_as_ds` | Disease Subtype | radio | subglotticStenosis=Subglottic Stenosis · bilateralVocalFoldImmobilityGlotticStenosis=Bilateral Vocal fold immobility or Glot… · supraglotticStenosis=Supraglottic Stenosis · trachealStenosis=Tracheal Stenosis … (5 options) | ✔ |  | [v3.0.0] | [v3.3.0] ([1×](#diagnosis_as_ds)) |
| 6 | `diagnosis_as_ds_bvfi_gs`<br><sub>replaces [`diagnosis_as_ds_bvfi`](#diagnosis_as_ds_bvfi) ([v3.3.0])</sub> | Bilateral Vocal fold immobility or Glottic Stenosis Subtype | radio | posteriorGlotticStenosis=Posterior Glottic Stenosis · bilateralVocalFoldParalysis=Bilateral Vocal Fold Paralysis · anteriorGlotticWeb=Anterior glottic Web · tbd=Not certain or TBD … (5 options) | ✔ |  | [v3.3.0] | — |
| 7 | `diagnosis_as_ds_bvfi_gs_other` | Other, Please specify | text | free text |  |  | [v3.3.0] | — |
| | **3. Etiology** | | | | | | | |
| 8 | `diagnosis_as_etiology` | What is the etiology? | radio | tbd=Not certain or TBD · iatrogenic=Iatrogenic (surgery or intubation) · idiopathic=Idiopathic · autoImmune=Auto-immune or granulomatous disease … (9 options) | ✔ |  | [v3.0.0] | [v3.3.0] ([1×](#diagnosis_as_etiology)) |
| 9 | `diagnosis_as_etiology_other` | Other, Please specify | text | free text | ✔ |  | [v3.0.0] | [v3.3.0] ([1×](#diagnosis_as_etiology_other)) |
| 10 | `diagnosis_as_etiology_auto_immune` | Auto-immune or granulomatous disease Subcategory | radio | gpa=Granulomatosis with polyangiitis (GPA)… · relapsingPolychondritis=Relapsing Polychondritis · other=Other | ✔ |  | [v3.0.0] | [v3.3.0] ([1×](#diagnosis_as_etiology_auto_immune)) |
| | **4. Disease Severity** | | | | | | | |
| 11 | `diagnosis_as_ds_mcg` | Degree of Stenosis (Myer-Cotton Grade) | radio | gradeI=Grade I · gradeII=Grade II · gradeIII=Grade III · gradeIV=Grade IV | ✔ |  | [v3.0.0] | [v3.10.0] ([2×](#diagnosis_as_ds_mcg)) |
| 12 | `diagnosis_as_ds_mcg_ref` | Degree of Stenosis (Myer-Cotton Grade) Picture for reference | descriptive | _display only — no data_ |  |  | [v3.0.0] | [v3.3.0] ([1×](#diagnosis_as_ds_mcg_ref)) |
| 13 | `diagnosis_as_ds_bc` | Degree of Stenosis (Bogdasarian Classification) | radio | class1=(a) Class 1 · class2=(b) Class 2 · class3=(c) Class 3 · class4=(d) Class 4 | ✔ |  | [v3.0.0] | [v3.3.0] ([1×](#diagnosis_as_ds_bc)) |
| 14 | `diagnosis_as_ds_bc_ref` | Degree of Stenosis (Bogdasarian Classification) Picture for reference | descriptive | _display only — no data_ |  |  | [v3.0.0] | [v3.3.0] ([1×](#diagnosis_as_ds_bc_ref)) |
| 15 | `diagnosis_as_ds_agw` | Anterior Glottic Web classification (Cohen) | radio | grade1=Grade 1 (0-35% obstruction) · grade2=Grade 2 (35-50% obstruction) · grade3=Grade 3 (51-75% obstruction) · grade4=Grade 4 (76-100% obstruction) |  |  | [v3.3.0] | — |
| 16 | `diagnosis_as_ds_cc_ref` | Anterior Glottic Web classification (Cohen) Picture for reference | descriptive | _display only — no data_ |  |  | [v3.3.0] | — |
| 17 | `diagnosis_as_ds_ac` | Grade of Stenosis (Aziz Classification of Supraglottic Stenosis) | radio | grade1=Grade 1 · grade2=Grade 2 · grade3=Grade 3 · grade4=Grade 4 … (5 options) | ✔ |  | [v3.0.0] | — |
| 18 | `diagnosis_as_ds_ac_grade_4` | Grade of Stenosis (Aziz Classification of Supraglottic Stenosis) | radio | grade4t=Grade 4T · grade4g=Grade 4G · grade4tg=Grade 4TG | ✔ |  | [v3.0.0] | [v3.3.0] ([1×](#diagnosis_as_ds_ac_grade_4)) |
| 19 | `diagnosis_as_ds_ac_ref` | Grade of Stenosis (Aziz Classification of Supraglottic Stenosis) Picture for reference | descriptive | _display only — no data_ |  |  | [v3.0.0] | — |
| 20 | `diagnosis_as_ds_eps` | How would you subjectively estimate the percent of stenosis from 0 to 100? | slider | slider: 0 \| \| 100 |  |  | [v3.3.0] | [v4.9.0] ([2×](#diagnosis_as_ds_eps)) |
| 21 | `diagnosis_as_ds_ods` | How would you subjectively classify the overall degree of stenosis? | radio | mild=Mild · moderate=Moderate · severe=Severe | ✔ |  | [v3.0.0] | — |
| 22 | `diagnosis_as_as` | Does this participant have audible stridor at rest or when talking? | radio | no=No · yes=Yes · notCertain=Not certain | ✔ |  | [v3.12.0] | [v4.1.0] ([1×](#diagnosis_as_as)) |
| 23 | `diagnosis_as_as_s` | Can you subjectively classify the severity of the stridor? | radio | mild=Mild · moderate=Moderate · severe=Severe | ✔ |  | [v3.12.0] | — |
| 24 | `diagnosis_as_as_c` | Is the stridor: | radio | inspiratory=Inspiratory · expiratory=Expiratory · biphasic=Biphasic | ✔ |  | [v3.12.0] | — |
| 25 | `diagnosis_as_ds_mluas` | Please describe levels and severity of stenosis involved | notes | free text (long) |  |  | [v3.3.0] | — |
| | **5. Treatment obtained** | | | | | | | |
| 26 | `diagnosis_as_treatment` | What treatment has the participant undergone for their stenosis? | checkbox | no_treatment=No treatment · surgery=Surgery · in_office_treatment=In-office treatment | ✔ |  | [v3.0.0] | [v4.1.0] ([2×](#diagnosis_as_treatment)) |
| 27 | `diagnosis_as_treatment_surgery` | Surgery options | checkbox | endoscopic_intervention=Endoscopic intervention with Laser and… · endoscopic_excision=Endoscopic laser wedge excision with ba… · laryngotracheal_reconstruction=Open Laryngotracheal reconstruction · laryngotracheoplasty=Laryngotracheoplasty (Maddern procedure) … (6 options) | ✔ |  | [v3.0.0] | [v3.3.0] ([1×](#diagnosis_as_treatment_surgery)) |
| 28 | `diagnosis_as_treatment_surgery_other` | Other Surgery option, Please Specify | text | free text |  |  | [v3.3.0] | — |
| 29 | `diagnosis_as_treatment_in_office` | In-office/awake treatment options | checkbox | steroid_injections_sole=Awake Steroid injection(s) as sole trea… · steroid_injections_adjunct=Awake Steroid injection(s) as adjunct t… · dilation=In-office or awake dilation · laser=In-office or awake laser | ✔ |  | [v3.0.0] | [v3.3.0] ([1×](#diagnosis_as_treatment_in_office)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_as_gsd`

<details><summary>Does the participant have airway stenosis confirmed by a laryngoscopy, bronchoscopy or CT… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Label | `Does the patient have airway stenosis confirmed by a laryngoscopy/bronchoscopy or CT imaging?` | `Does the patient have airway stenosis confirmed by a laryngoscopy, bronchoscopy or CT imaging?` |
| [v4.1.0] | 2025-09-17 | Section header | ∅ | `1. Gold Standard Diagnosis` |
|  |  | Label | `Does the patient have airway stenosis confirmed by a laryngoscopy, bronchoscopy or CT imaging?` | `Does the participant have airway stenosis confirmed by a laryngoscopy, bronchoscopy or CT imaging?` |
|  |  | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_as_gsd_yes`

<details><summary>Confirmed by — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Type | `radio` | `checkbox` |
|  |  | Choices / calculation | 2 options | ✏️ `bronchoscopy`: Confirmed by bronchoscopy/lar… → Confirmed by bronchoscopy or… |

</details>

### `diagnosis_as_pft`

<details><summary>Has the participant had pulmonary function testing within the past 3 months? — 3 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Section header | `1. Gold Standard Diagnosis` | `1. Gold Standard Diagnosis 4. Disease Severity` |
| [v3.10.0] | 2024-07-18 | Section header | `1. Gold Standard Diagnosis 4. Disease Severity` | `1. Gold Standard Diagnosis` |
| [v4.1.0] | 2025-09-17 | Section header | `1. Gold Standard Diagnosis` | ∅ |
|  |  | Label | `Has the patient had pulmonary function testing within the past 3 months?` | `Has the participant had pulmonary function testing within the past 3 months?` |
|  |  | Choices / calculation | 3 options | 🔀 reordered |

</details>

### `diagnosis_as_ds`

<details><summary>Disease Subtype — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Choices / calculation | 6 options | ➕ `subglotticStenosis`=Subglottic Stenosis, `bilateralVocalFoldImmobilityGlotticStenosis`=Bilateral Vocal fold immobility or Glot…<br>➖ `subgloticStenosis`=Subglottic Stenosis, `bilateralVocalFoldImmobility`=Bilateral Vocal fold immobility, `glotticStenosis`=Glottic Stenosis |

</details>

### `diagnosis_as_ds_bvfi_gs`

<details><summary>Bilateral Vocal fold immobility or Glottic Stenosis Subtype — introduced as a replacement</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.3.0] | 2024-03-13 | 🆕 Introduced | | Resp — Airway Stenosis<br>↪️ replaces [`diagnosis_as_ds_bvfi`](#diagnosis_as_ds_bvfi) — Subtype now covers bilateral vocal fold immobility or glottic stenosis |

</details>

### `diagnosis_as_etiology`

<details><summary>What is the etiology? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Choices / calculation | 6 options | ➕ `gerd`=GERD, `causticInjuryInhalationInjury`=Caustic Injury or Inhalation Injury, `infectious`=Infectious (Diphtheria, TB, Bacterial T…<br>✏️ `tbd`: Not certain / TBD → Not certain or TBD; `iatrogenic`: Iatrogenic (surgery/intubatio… → Iatrogenic (surgery or intuba…; `autoImmune`: Auto-immune / granulomatous d… → Auto-immune or granulomatous… |

</details>

### `diagnosis_as_etiology_other`

<details><summary>Other, Please specify — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Type | `radio` | `text` |
|  |  | Label | `Other Subcategory` | `Other, Please specify` |
|  |  | Choices / calculation | 5 options | ➖ `gerd`=GERD, `injury`=Caustic Injury/Inhalation Injury, `infectious`=Infectious (Diphteria, TB, Bacterial Tr…, `rrp`=Recurrent Respiratory Papillomatosis, `other`=Other |

</details>

### `diagnosis_as_etiology_auto_immune`

<details><summary>Auto-immune or granulomatous disease Subcategory — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Label | `Auto-immune / granulomatous disease Subcategory` | `Auto-immune or granulomatous disease Subcategory` |

</details>

### `diagnosis_as_ds_mcg`

<details><summary>Degree of Stenosis (Myer-Cotton Grade) — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Section header | `4. Disease Severity` | ∅ |
|  |  | Branching logic | `[diagnosis_as_ds] = 'subgloticStenosis'` | `[diagnosis_as_ds] = 'subglotticStenosis' or [diagnosis_as_ds] = 'trachealStenosis'` |
| [v3.10.0] | 2024-07-18 | Section header | ∅ | `4. Disease Severity` |

</details>

### `diagnosis_as_ds_mcg_ref`

<details><summary>Degree of Stenosis (Myer-Cotton Grade) Picture for reference — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Branching logic | `[diagnosis_as_ds] = 'subgloticStenosis'` | `[diagnosis_as_ds] = 'subglotticStenosis' or [diagnosis_as_ds] = 'trachealStenosis'` |

</details>

### `diagnosis_as_ds_bc`

<details><summary>Degree of Stenosis (Bogdasarian Classification) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Choices / calculation | 4 options | ✏️ `class1`: Class 1 → (a) Class 1; `class2`: Class 2 → (b) Class 2; `class3`: Class 3 → (c) Class 3; `class4`: Class 4 → (d) Class 4 |
|  |  | Branching logic | `[diagnosis_as_ds] = 'glotticStenosis' or [diagnosis_as_ds] = 'trachealStenosis'` | `[diagnosis_as_ds_bvfi_gs] = 'posteriorGlotticStenosis'` |

</details>

### `diagnosis_as_ds_bc_ref`

<details><summary>Degree of Stenosis (Bogdasarian Classification) Picture for reference — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Branching logic | `[diagnosis_as_ds] = 'glotticStenosis' or [diagnosis_as_ds] = 'trachealStenosis'` | `[diagnosis_as_ds_bvfi_gs] = 'posteriorGlotticStenosis'` |

</details>

### `diagnosis_as_ds_ac_grade_4`

<details><summary>Grade of Stenosis (Aziz Classification of Supraglottic Stenosis) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Branching logic | `[diagnosis_as_ds] = 'supraglotticStenosis' and [diagnosis_as_ds_ac] = 'gradeIV'` | `[diagnosis_as_ds_ac] = 'grade4'` |

</details>

### `diagnosis_as_ds_eps`

<details><summary>How would you subjectively estimate the percent of stenosis from 0 to 100? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.3.0] | 2024-03-13 | 🆕 Introduced | | Resp — Airway Stenosis |
| [v4.1.0] | 2025-09-17 | Choices / calculation | ∅ | `0 \| \| 100` |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_as_as`

<details><summary>Does this participant have audible stridor at rest or when talking? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.12.0] | 2024-08-06 | 🆕 Introduced | | Resp — Airway Stenosis |
| [v4.1.0] | 2025-09-17 | Label | `Does this patient have audible stridor at rest or when talking?` | `Does this participant have audible stridor at rest or when talking?` |

</details>

### `diagnosis_as_treatment`

<details><summary>What treatment has the participant undergone for their stenosis? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Type | `radio` | `checkbox` |
|  |  | Choices / calculation | 3 options | ➕ `no_treatment`=No treatment, `in_office_treatment`=In-office treatment<br>➖ `noTreatment`=No treatment, `inOfficeTreatment`=In-office treatment |
| [v4.1.0] | 2025-09-17 | Label | `What treatment has the patient undergone for their stenosis?` | `What treatment has the participant undergone for their stenosis?` |

</details>

### `diagnosis_as_treatment_surgery`

<details><summary>Surgery options — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Type | `radio` | `checkbox` |
|  |  | Choices / calculation | 5 options | ➕ `endoscopic_intervention`=Endoscopic intervention with Laser and…, `endoscopic_excision`=Endoscopic laser wedge excision with ba…, `laryngotracheal_reconstruction`=Open Laryngotracheal reconstruction, `other`=Other<br>➖ `endoscopicIntervention`=Endoscopic intervention with Laser and…, `endoscopicExcision`=Endoscopic laser wedge excision, `laryngotrachealReconstruction`=Laryngotracheal reconstruction |
|  |  | Branching logic | `[diagnosis_as_treatment] = 'surgery'` | `[diagnosis_as_treatment(surgery)] = "1"` |

</details>

### `diagnosis_as_treatment_in_office`

<details><summary>In-office/awake treatment options — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | Type | `radio` | `checkbox` |
|  |  | Label | `In-office treatment options` | `In-office/awake treatment options` |
|  |  | Choices / calculation | 3 options | ➕ `steroid_injections_sole`=Awake Steroid injection(s) as sole trea…, `steroid_injections_adjunct`=Awake Steroid injection(s) as adjunct t…<br>➖ `steroidInjection`=Steroid injection(s)<br>✏️ `dilation`: In-office dilation → In-office or awake dilation; `laser`: In-office laser → In-office or awake laser |
|  |  | Branching logic | `[diagnosis_as_treatment] = 'inOfficeTreatment'` | `[diagnosis_as_treatment(in_office_treatment)] = "1"` |

</details>

### `diagnosis_as_ds_bvfi`

<details><summary>Bilateral Vocal fold immobility Subtype — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.0.0] | 2023-12-08 | 🆕 Introduced | | Diagnosis Respiratory Disorders Airway Stenosis |
| [v3.3.0] | 2024-03-13 | ⚫ Removed | Resp — Airway Stenosis | ↪️ replaced by [`diagnosis_as_ds_bvfi_gs`](#diagnosis_as_ds_bvfi_gs) — Subtype now covers bilateral vocal fold immobility or glottic stenosis |

</details>

## ⚫ Removed Fields

Variables that were once in this instrument and are no longer in the REDCap dictionary.

| # | Variable | Label (last known) | Type | Introduced | Removed | Replaced by |
| :-: | :-- | :-- | :-- | :-: | :-: | :-- |
| 1 | [`diagnosis_as_ds_bvfi`](#diagnosis_as_ds_bvfi) | Bilateral Vocal fold immobility Subtype | radio | [v3.0.0] | [v3.3.0] | [`diagnosis_as_ds_bvfi_gs`](#diagnosis_as_ds_bvfi_gs) |

<!-- milestone links -->
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v3.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.10.0
[v3.12.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.12.0
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
