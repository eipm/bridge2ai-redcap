<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Resp — COPD and Asthma

**Form name:** `d_resp_copd_and_asthma` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v4.0.0] (2025-08-19) · **Last changed:** [v4.9.0] (2026-07-21)  
**Fields:** 📋 39 in REDCap · ⚫ 2 removed · ✏️ 29 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| 1 | `diagnosis_ca_copd_asthma` | Does the participant have COPD, asthma, or both? | radio | copd=COPD only · asthma=Asthma only · bothCopdAsthma=Both COPD and asthma · neitherCopdAsthma=Neither COPD nor asthma … (5 options) |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_copd_asthma)) |
| 2 | `diagnosis_ca_spirometry_test` | Has the participant had a spirometry test? | radio | yes=Yes · no=No |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_spirometry_test)) |
| | **1. Spirometry and diagnosis** | | | | | | | |
| 3 | `diagnosis_ca_spirometry_ce` | Does the participant have clinical evidence of obstruction as diagnosed by spirometry? | radio | yes=Yes · no=No |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_spirometry_ce)) |
| 4 | `diagnosis_ca_spirometry_verification` | Please select one of the two options below for verification of the spirometry test. If both are available, please select ATS/ERS | radio | atsErs=ATS/ERS criteria reported: FEV1/FVC < 5… · goldCriteria=GOLD criteria reported: FEV1/FVC < 0.7… |  |  | [v4.0.0] | [v4.1.0] ([2×](#diagnosis_ca_spirometry_verification)) |
| 5 | `diagnosis_ca_fev1` | What is the FEV1 (percent predicted) (if known)? | slider | slider: 0 \| \| 150 |  |  | [v4.0.0] | [v4.9.0] ([1×](#diagnosis_ca_fev1)) |
| 6 | `diagnosis_ca_ats_ers_criteria_fev1` | FEV1/FVC < 5th percentile OR z score ≤ -1.65 ? | radio | yes=Yes · no=No |  |  | [v4.0.0] | [v4.0.1] ([1×](#diagnosis_ca_ats_ers_criteria_fev1)) |
| 7 | `diagnosis_ca_ats_ers_criteria_fvc` | FVC < 0.7 OR z score ≤ -1.65 ? | radio | yes=Yes · no=No |  |  | [v4.0.0] | [v4.0.1] ([1×](#diagnosis_ca_ats_ers_criteria_fvc)) |
| 8 | `diagnosis_ca_pft_lung` | Is there a full PFT including lung volumes? | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 9 | `diagnosis_ca_restrictive` | Is there evidence of restrictive ventilatory defect (TLC < 5th percentile or z score ≤ -1.65)? | radio | yes=Yes · no=No |  |  | [v4.0.0] | — |
| 10 | `diagnosis_ca_responsiveness_criteria` | Did the participant meet the criteria for responsiveness on bronchodilator testing? (Increase in FEV1 or FVC by 200ml and 12 % from baselin… | radio | yes=Yes · no=No · notCertain=Not Certain |  |  | [v4.0.0] | [v4.1.0] ([2×](#diagnosis_ca_responsiveness_criteria)) |
| 11 | `diagnosis_ca_asthma` | Does the participant have a history of confirmed expiratory airflow variability? (Increase in FEV1 or FVC by ≥200ml and ≥12 % from baseline… | radio | yes=Yes · no=No · notCertain=Not Certain |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_asthma)) |
| | **2. Disease Subtype** | | | | | | | |
| 12 | `diagnosis_ca_copd` | Does the participant have disease subtype for COPD? | radio | yes=Yes · no=No · notCertain=Not Certain |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_copd)) |
| 13 | `diagnosis_ca_copd_subtype` | Please select all that apply: | checkbox | chronic_bronchitis=Chronic bronchitis · emphysema=Emphysema · eosinophilic=Eosinophilic (Type2high COPD) · aatd=Alpha-1 AntitrypsinDeficiency (AATD) |  |  | [v4.0.0] | — |
| 14 | `diagnosis_ca_mmrc_grade_score` | What is the mMRC grade score? | text | `integer` [0–4] |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_mmrc_grade_score)) |
| 15 | `diagnosis_ca_cat_score` | What is the CAT score? | text | `integer` [0–40] |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_cat_score)) |
| 16 | `diagnosis_ca_gold_group` | What is the GOLD Group? (A/B/E) | radio | a=A · b=B · e=E |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_gold_group)) |
| 17 | `diagnosis_ca_asthma_probability` | Is the clinical probability of asthma high (e.g. allergic or eosinophilic phenotype, variable respiratory symptoms including wheezing, coug… | radio | yes=Yes · no=No |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_asthma_probability)) |
| 18 | `diagnosis_ca_asthma_has_subtype` | Does the participant have disease subtype for asthma? | radio | yes=Yes · no=No · notCertain=Not Certain |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_asthma_has_subtype)) |
| 19 | `diagnosis_ca_asthma_subtype` | Please select all that apply: | checkbox | allergic=Allergic · eosinophilic=Eosinophilic · type_2_low=Type 2 low · obese=Obese … (5 options) |  |  | [v4.0.0] | — |
| 20 | `diagnosis_ca_asthma_subtype_other` | Please specify: | text | free text |  |  | [v4.0.1] | — |
| 21 | `diagnosis_ca_feno_within_12_months` | Is the FeNO value available within last 12 months? | radio | yes=Yes · no=No |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_feno_within_12_months)) |
| 22 | `diagnosis_ca_feno_value` | Provide value (ppb) | text | `number` [0–] |  |  | [v4.0.0] | — |
| 23 | `part_asthmaeosinop_hil` | [DEPRECATED] Absolute eosinophil count in last 12 months (highest value - cells per microliter (µL)? | text | `number` [0–] |  |  | [v4.0.0] | [v4.1.0] ([1×](#part_asthmaeosinop_hil)) |
| 24 | `diagnosis_ca_absolute_eosinophil_count` | Absolute eosinophil count in last 12 months (highest value - cells per microliter (µL)? | text | `number` [0–] |  |  | [v4.1.0] | — |
| 25 | `diagnosis_ca_act_score` | What is the ACT score on the most recent visit? | radio | controlled=Controlled (>20) · notControlled=Not controlled (15-19) · poorlyControlled=Poorly controlled (< 15) · notCertain=Not Certain |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_act_score)) |
| 26 | `diagnosis_ca_pft_within_6_months` | Has the participant had PFT within the past 6 months? | radio | yes=Yes · no=No |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_pft_within_6_months)) |
| 27 | `diagnosis_ca_pft_file` | Please upload results | file | file upload |  | 🔒 | [v4.0.0] | — |
| 28 | `diagnosis_ca_moderate_exacerbations_count` | How many moderate (requiring OCS course) exacerbations in prior 12 months? | text | `integer` |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_moderate_exacerbations_count)) |
| 29 | `diagnosis_ca_severe_exacerbations_count` | How many severe (requiring hospitalization) exacerbations in prior 12 months ? | text | `integer` |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_severe_exacerbations_count)) |
| | **3. Current symptoms and participant history** | | | | | | | |
| 30 | `diagnosis_ca_pulmonary_symptoms` | Does the participant have any of the following pulmonary symptoms? (Check all that apply) | checkbox | dyspnea=Dyspnea · chronic_cough=Chronic Cough · sputum_production=Sputum production · wheezing=Wheezing |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_pulmonary_symptoms)) |
| 31 | `part_copd` | Check all that are present: | checkbox | chest_ct=Chest CT - with emphysema changes, air… · cxr=CXR: with hyperlucency or hyperinflatio… · chrf=Chronic hypercapnic respiratory failure · hypoxia=Pulse oximetry with hypoxia/oxygen depe… … (12 options) |  |  | [v4.0.0] | — |
| 32 | `diagnosis_ca_current_smoker` | Is participant a current smoker? | radio | yes=Yes · no=No · notCertain=Not Certain |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_current_smoker)) |
| 33 | `diagnosis_ca_10_pack_year_tobacco_cigarette` | Does the participant have at least a 10 pack year tobacco cigarette history? | radio | yes=Yes · no=No · notCertain=Not Certain |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_10_pack_year_tobacco_cigarette)) |
| 34 | `diagnosis_ca_significant_inhalation_exposure_history` | Does the participant have any other significant inhalation exposure history? | radio | yes=Yes · no=No · notCertain=Not Certain |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_significant_inhalation_exposure_history)) |
| 35 | `diagnosis_ca_significant_inhalation_exposure_history_explanation` | Please select all that apply (optional): | checkbox | secondhand_smoke=Secondhand smoke · biomass_fuels=Biomass fuels · other=Other |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_significant_inhalation_exposure_history_explanation)) |
| 36 | `diagnosis_ca_significant_inhalation_exposure_history_explanation_other` | Please specify: | text | free text |  |  | [v4.1.0] | — |
| 37 | `diagnosis_ca_environmental_allergy_history`<br><sub>formerly `diagnosis_ca_enviromental_allergy_history` ([v4.1.0])</sub> | Does the participant have a strong environmental allergy history? | radio | yes=Yes · no=No · notCertain=Not Certain |  |  | [v4.0.0] | [v4.1.0] ([1×](#diagnosis_ca_environmental_allergy_history)) |
| | **4. Treatment obtained** | | | | | | | |
| 38 | `diagnosis_ca_pharmacologic_treatment` | What pharmacologic treatment is the participant currently receiving? (Select all that apply) | checkbox | laba=LABA · lama=LAMA · saba=SABA · sama=SAMA … (14 options) |  |  | [v4.0.0] | [v4.1.0] ([2×](#diagnosis_ca_pharmacologic_treatment)) |
| 39 | `diagnosis_ca_ics_dosage` | Is the participant on low, medium or high dose ICS? | radio | low=Low dose · medium=Medium dose · high=High dose · notCertain=Not Certain |  |  | [v4.0.0] | [v4.1.0] ([2×](#diagnosis_ca_ics_dosage)) |

## ✏️ Former Variable Names

Variables in this instrument that had a different name in earlier releases. Their history before the rename is included under the current name.

| # | Former name | Current name | Relation | Renamed in |
| :-: | :-- | :-- | :-- | :-: |
| 1 | `diagnosis_ca_enviromental_allergy_history` | [`diagnosis_ca_environmental_allergy_history`](#diagnosis_ca_environmental_allergy_history) | ✏️ Renamed | [v4.1.0] |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnosis_ca_copd_asthma`

<details><summary>Does the participant have COPD, asthma, or both? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have COPD, asthma, or both?` | `Does the participant have COPD, asthma, or both?` |

</details>

### `diagnosis_ca_spirometry_test`

<details><summary>Has the participant had a spirometry test? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient had a spirometry test?` | `Has the participant had a spirometry test?` |

</details>

### `diagnosis_ca_spirometry_ce`

<details><summary>Does the participant have clinical evidence of obstruction as diagnosed by spirometry? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have clinical evidence of obstruction as diagnosed by spirometry?` | `Does the participant have clinical evidence of obstruction as diagnosed by spirometry?` |

</details>

### `diagnosis_ca_spirometry_verification`

<details><summary>Please select one of the two options below for verification of the spirometry test. If bo… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.0.1] | 2025-08-28 | Label | `Please select one of the two options below forverification of the spirometry test. If both are available, please select ATS/ERS` | `Please select one of the two options below for verification of the spirometry test. If both are available, please select ATS/ERS` |
|  |  | Choices / calculation | 2 options | ✏️ `goldCriteria`: GOLD criteria reported: FEV1/… → GOLD criteria reported: FEV1/… |
| [v4.1.0] | 2025-09-17 | Choices / calculation | 2 options | ✏️ `goldCriteria`: GOLD criteria reported: FEV1/… → GOLD criteria reported: FEV1/… |

</details>

### `diagnosis_ca_fev1`

<details><summary>What is the FEV1 (percent predicted) (if known)? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |

</details>

### `diagnosis_ca_ats_ers_criteria_fev1`

<details><summary>FEV1/FVC < 5th percentile OR z score ≤ -1.65 ? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.0.1] | 2025-08-28 | Label | `FEV1/FVC < 5th percentile?` | `FEV1/FVC < 5th percentile OR z score ≤ -1.65 ?` |

</details>

### `diagnosis_ca_ats_ers_criteria_fvc`

<details><summary>FVC < 0.7 OR z score ≤ -1.65 ? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.0.1] | 2025-08-28 | Label | `FVC < 0.7?` | `FVC < 0.7 OR z score ≤ -1.65 ?` |

</details>

### `diagnosis_ca_responsiveness_criteria`

<details><summary>Did the participant meet the criteria for responsiveness on bronchodilator testing? (Incr… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.0.1] | 2025-08-28 | Label | `Did the patient meet the criteria forresponsiveness on bronchodilator testing?` | `Did the patient meet the criteria for responsiveness on bronchodilator testing? (Increase in FEV1 or FVC by 200ml and 12 % from baseline with bronchodilators)?` |
|  |  | Choices / calculation | 2 options | ➕ `notCertain`=Not Certain |
| [v4.1.0] | 2025-09-17 | Label | `Did the patient meet the criteria for responsiveness on bronchodilator testing? (Increase in FEV1 or FVC by 200ml and 12 % from baseline with bronchodilators)?` | `Did the participant meet the criteria for responsiveness on bronchodilator testing? (Increase in FEV1 or FVC by 200ml and 12 % from baseline with bronchodilato…` |

</details>

### `diagnosis_ca_asthma`

<details><summary>Does the participant have a history of confirmed expiratory airflow variability? (Increas… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have a history of confirmed expiratory airflow variability? (Increase in FEV1 or FVC by ≥200ml and ≥12 % from baseline with bronchodilators or…` | `Does the participant have a history of confirmed expiratory airflow variability? (Increase in FEV1 or FVC by ≥200ml and ≥12 % from baseline with bronchodilator…` |
|  |  | Branching logic | `([diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='both_asthma_copd' or ([diagnosis_ca_copd_asthma]='neither') and [diagnosis_ca_spirometry_ce…` | `([diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='bothCopdAsthma' or ([diagnosis_ca_copd_asthma]='neitherCopdAsthma') and [diagnosis_ca_spiro…` |

</details>

### `diagnosis_ca_copd`

<details><summary>Does the participant have disease subtype for COPD? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have disease subtype for COPD?` | `Does the participant have disease subtype for COPD?` |
|  |  | Branching logic | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='both_asthma_copd' or [diagnosis_ca_spirometry_ce]='yes'` | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='bothCopdAsthma' or [diagnosis_ca_spirometry_ce]='yes'` |

</details>

### `diagnosis_ca_mmrc_grade_score`

<details><summary>What is the mMRC grade score? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Branching logic | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='both_asthma_copd' or [diagnosis_ca_spirometry_ce]='yes'` | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='bothCopdAsthma' or [diagnosis_ca_spirometry_ce]='yes'` |

</details>

### `diagnosis_ca_cat_score`

<details><summary>What is the CAT score? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Branching logic | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='both_asthma_copd' or [diagnosis_ca_spirometry_ce]='yes'` | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='bothCopdAsthma' or [diagnosis_ca_spirometry_ce]='yes'` |

</details>

### `diagnosis_ca_gold_group`

<details><summary>What is the GOLD Group? (A/B/E) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Branching logic | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='both_asthma_copd' or [diagnosis_ca_spirometry_ce]='yes'` | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='bothCopdAsthma' or [diagnosis_ca_spirometry_ce]='yes'` |

</details>

### `diagnosis_ca_asthma_probability`

<details><summary>Is the clinical probability of asthma high (e.g. allergic or eosinophilic phenotype, vari… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Branching logic | `[diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='both_asthma_copd'` | `[diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='bothCopdAsthma'` |

</details>

### `diagnosis_ca_asthma_has_subtype`

<details><summary>Does the participant have disease subtype for asthma? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have disease subtype for asthma?` | `Does the participant have disease subtype for asthma?` |
|  |  | Branching logic | `[diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='both_asthma_copd'` | `[diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='bothCopdAsthma'` |

</details>

### `diagnosis_ca_feno_within_12_months`

<details><summary>Is the FeNO value available within last 12 months? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Branching logic | `[diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='both_asthma_copd'` | `[diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='bothCopdAsthma'` |

</details>

### `part_asthmaeosinop_hil`

<details><summary>[DEPRECATED] Absolute eosinophil count in last 12 months (highest value - cells per micro… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Label | `Absolute eosinophil count in last 12 months (highest value - cells per microliter (µL)?` | `[DEPRECATED] Absolute eosinophil count in last 12 months (highest value - cells per microliter (µL)?` |
|  |  | Branching logic | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='both_copd_asthma'` | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='bothCopdAsthma'` |
|  |  | Annotation | ∅ | `@HIDDEN` |

</details>

### `diagnosis_ca_act_score`

<details><summary>What is the ACT score on the most recent visit? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Branching logic | `[diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='both_copd_asthma'` | `[diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='bothCopdAsthma'` |

</details>

### `diagnosis_ca_pft_within_6_months`

<details><summary>Has the participant had PFT within the past 6 months? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient had PFT within the past 6 months?` | `Has the participant had PFT within the past 6 months?` |

</details>

### `diagnosis_ca_moderate_exacerbations_count`

<details><summary>How many moderate (requiring OCS course) exacerbations in prior 12 months? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Branching logic | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='both_copd_asthma' or [diagnosis_ca_spirometry_ce]='yes'` | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='bothCopdAsthma' or [diagnosis_ca_spirometry_ce]='yes'` |

</details>

### `diagnosis_ca_severe_exacerbations_count`

<details><summary>How many severe (requiring hospitalization) exacerbations in prior 12 months ? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Branching logic | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='both_copd_asthma' or [diagnosis_ca_spirometry_ce]='yes'` | `[diagnosis_ca_copd_asthma]='copd' or [diagnosis_ca_copd_asthma]='asthma' or [diagnosis_ca_copd_asthma]='bothCopdAsthma' or [diagnosis_ca_spirometry_ce]='yes'` |

</details>

### `diagnosis_ca_pulmonary_symptoms`

<details><summary>Does the participant have any of the following pulmonary symptoms? (Check all that apply) — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Section header | `3. Current symptoms and patient history` | `3. Current symptoms and participant history` |
|  |  | Label | `Does the patient have any of the following pulmonary symptoms? (Check all that apply)` | `Does the participant have any of the following pulmonary symptoms? (Check all that apply)` |
|  |  | Choices / calculation | 5 options | ➖ `none`=None |

</details>

### `diagnosis_ca_current_smoker`

<details><summary>Is participant a current smoker? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Label | `Is patient a current smoker?` | `Is participant a current smoker?` |
|  |  | Choices / calculation | 3 options | ➕ `notCertain`=Not Certain<br>➖ `not_certain`=Not Certain |

</details>

### `diagnosis_ca_10_pack_year_tobacco_cigarette`

<details><summary>Does the participant have at least a 10 pack year tobacco cigarette history? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have at least a 10 pack year tobacco cigarette history?` | `Does the participant have at least a 10 pack year tobacco cigarette history?` |
|  |  | Choices / calculation | 3 options | ➕ `notCertain`=Not Certain<br>➖ `not_certain`=Not Certain |

</details>

### `diagnosis_ca_significant_inhalation_exposure_history`

<details><summary>Does the participant have any other significant inhalation exposure history? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have any other significant inhalation exposure history?` | `Does the participant have any other significant inhalation exposure history?` |
|  |  | Choices / calculation | 3 options | ➕ `notCertain`=Not Certain<br>➖ `not_certain`=Not Certain |

</details>

### `diagnosis_ca_significant_inhalation_exposure_history_explanation`

<details><summary>Please select all that apply (optional): — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | Type | `text` | `checkbox` |
|  |  | Label | `Please explain (optional):` | `Please select all that apply (optional):` |
|  |  | Choices / calculation | 0 options | ➕ `secondhand_smoke`=Secondhand smoke, `biomass_fuels`=Biomass fuels, `other`=Other |
|  |  | Branching logic | `[diagnosis_ca_significant_inhalation_exposure_history]='yes'` | `[diagnosis_ca_significant_inhalation_exposure_history]="yes"` |

</details>

### `diagnosis_ca_environmental_allergy_history`

<details><summary>Does the participant have a strong environmental allergy history? — 1 change · formerly <code>diagnosis_ca_enviromental_allergy_history</code></summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | as `diagnosis_ca_enviromental_allergy_history` in Resp — COPD and Asthma |
| [v4.1.0] | 2025-09-17 | ✏️ Renamed | `diagnosis_ca_enviromental_allergy_history` | `diagnosis_ca_environmental_allergy_history`<br><sub>Spelling fix</sub> |
| | | Label | `Does the patient have a strong environmental allergy history?` | `Does the participant have a strong environmental allergy history?` |
| | | Choices / calculation | 3 options | ➕ `notCertain`=Not Certain<br>➖ `not_certain`=Not Certain |

</details>

### `diagnosis_ca_pharmacologic_treatment`

<details><summary>What pharmacologic treatment is the participant currently receiving? (Select all that app… — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.0.1] | 2025-08-28 | Choices / calculation | 12 options | ➕ `lama`=LAMA, `sama`=SAMA, `methylxanthines`=Methylxanthines, `leukotriene_inhibitors`=Leukotriene Inhibitors<br>➖ `methylxan`=Methylxan, `leukotrien_inhibitors`=Leukotrien Inhibitors<br>✏️ `pde_4`: PDE 4 inhib → PDE 4 inhibitor; `mucolytics`: Mycolitics → Mucolytics |
| [v4.1.0] | 2025-09-17 | Label | `What pharmacologic treatment is the patient currently receiving? (Select all that apply)` | `What pharmacologic treatment is the participant currently receiving? (Select all that apply)` |
|  |  | Choices / calculation | 14 options | ➕ `pde4`=PDE 4 inhibitor, `pde3`=PDE 3 and Inhibitor<br>➖ `pde_4`=PDE 4 inhibitor, `pde_3`=PDE 3 and Inhibitor |

</details>

### `diagnosis_ca_ics_dosage`

<details><summary>Is the participant on low, medium or high dose ICS? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.0.1] | 2025-08-28 | Choices / calculation | 3 options | ➕ `notCertain`=Not Certain |
| [v4.1.0] | 2025-09-17 | Type | `checkbox` | `radio` |
|  |  | Label | `Is the patient on low, medium or high dose ICS?` | `Is the participant on low, medium or high dose ICS?` |

</details>

### `diagnosis_ca_bronchodilator_testing_criteria`

<details><summary>Does the patient have a positive bronchial challenge testing (e.g. methacholine, mannitol… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.0.1] | 2025-08-28 | ⚫ Removed | Resp — COPD and Asthma |  |

</details>

### `diagnosis_ca_inhaler`

<details><summary>Which inhaler is the patient using, either on their own or in combination through combina… — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.0.0] | 2025-08-19 | 🆕 Introduced | | Resp — COPD and Asthma |
| [v4.0.1] | 2025-08-28 | ⚫ Removed | Resp — COPD and Asthma |  |

</details>

## ⚫ Removed Fields

Variables that were once in this instrument and are no longer in the REDCap dictionary.

| # | Variable | Label (last known) | Type | Introduced | Removed | Replaced by |
| :-: | :-- | :-- | :-- | :-: | :-: | :-- |
| 1 | [`diagnosis_ca_bronchodilator_testing_criteria`](#diagnosis_ca_bronchodilator_testing_criteria) | Does the patient have a positive bronchial challenge testing (e.g. methacholine, mannitol, etc)? | radio | [v4.0.0] | [v4.0.1] | — |
| 2 | [`diagnosis_ca_inhaler`](#diagnosis_ca_inhaler) | Which inhaler is the patient using, either on their own or in combination through combination inhaler therapy? (Select… | checkbox | [v4.0.0] | [v4.0.1] | — |

<!-- milestone links -->
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.0.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.1
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
