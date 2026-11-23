<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Voice — Glottic Insufficiency / Presbyphonia

**Form name:** `d_voice_glottic_insufficiency_presbyphonia` · **Category:** Adult Diagnoses · **Status:** 🟢 Active  
**Introduced:** [v3.20.0] (2024-11-13) · **Last changed:** [v4.9.0] (2026-07-21)  
**Fields:** 📋 29 in REDCap · ⚫ 0 removed · ✏️ 8 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **1. Gold Standard Diagnosis** | | | | | | | |
| 1 | `diagnois_gi_gsd` | Does the participant have glottic insufficiency confirmed by laryngoscopy/stroboscopy? | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v3.20.0] | [v4.1.0] ([2×](#diagnois_gi_gsd)) |
| | **2. Disease Subtype/etiology** | | | | | | | |
| 2 | `diagnosis_gi_d` | What is the glottic insufficiency diagnosis? | radio | vocalFoldAtrophyRelatedToAging=Vocal fold atrophy related to aging (Pr… · vocalFoldAtrophyRelatedToOtherCause=Vocal fold atrophy related to other cau… · bilateralSulcus=Bilateral sulcus · other=Other | ✔ |  | [v3.20.0] | — |
| 3 | `diagnosis_gi_d_other` | Please specify | text | free text |  |  | [v3.20.0] | — |
| 4 | `diagnosis_gi_d_aoc` | What is the glottic insufficiency diagnosis? | radio | severeIllness=Severe illness · rapidWeightLoss=Rapid weight loss · hormonalChanges=Hormonal changes · other=Other | ✔ |  | [v3.20.0] | — |
| 5 | `diagnosis_gi_d_aoc_other` | Please specify | text | free text |  |  | [v3.20.0] | — |
| | **3. Disease Severity** | | | | | | | |
| 6 | `diagnosis_gi_dogg` | Please assess degree of glottic gap: | radio | small=Small · moderate=Moderate · large=Large | ✔ |  | [v3.20.0] | — |
| 7 | `diagnosis_gi_slogg` | Please assess shape/location of glottic gap. Choose all that apply. | checkbox | spindle_shaped=Spindle shaped · anterior_glottic_gap=Anterior Glottic gap · posterior_glottic_gap=Posterior glottic gap · asymmetric=Asymmetric | ✔ |  | [v3.20.0] | — |
| 8 | `diagnosis_gi_degree_text` | Degree of dysphonia CAPE-V scale | descriptive | _display only — no data_ |  |  | [v3.20.0] | — |
| 9 | `diagnosis_gi_degree_legend` | Legend: C- Sonsistent I = Intermittent MI = Mildly Deviant MO = Moderately Deviant SE = Severely Deviant | descriptive | _display only — no data_ |  |  | [v3.20.0] | — |
| 10 | `diagnosis_gi_degree_os_1` | Overall Severity | slider | slider: MI \| MO \| SE |  |  | [v3.20.0] | [v4.9.0] ([1×](#diagnosis_gi_degree_os_1)) |
| 11 | `diagnosis_gi_degree_os_2` | Overall Severity | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.20.0] | — |
| 12 | `diagnosis_gi_degree_r_1` | Roughness | slider | slider: MI \| MO \| SE |  |  | [v3.20.0] | [v4.9.0] ([1×](#diagnosis_gi_degree_r_1)) |
| 13 | `diagnosis_gi_degree_r_2` | Roughness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.20.0] | — |
| 14 | `diagnosis_gi_degree_b_1` | Breathiness | slider | slider: MI \| MO \| SE |  |  | [v3.20.0] | [v4.9.0] ([1×](#diagnosis_gi_degree_b_1)) |
| 15 | `diagnosis_gi_degree_b_2` | Breathiness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.20.0] | — |
| 16 | `diagnosis_gi_degree_s_1` | Strain | slider | slider: MI \| MO \| SE |  |  | [v3.20.0] | [v4.9.0] ([1×](#diagnosis_gi_degree_s_1)) |
| 17 | `diagnosis_gi_degree_s_2` | Strain | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.20.0] | — |
| 18 | `diagnosis_gi_degree_p_1` | Pitch | slider | slider: MI \| MO \| SE |  |  | [v3.20.0] | [v4.9.0] ([1×](#diagnosis_gi_degree_p_1)) |
| 19 | `diagnosis_gi_degree_p_nature` | Pitch (Indicate the nature of the abnormality): | text | free text |  |  | [v3.20.0] | — |
| 20 | `diagnosis_gi_degree_p_2` | Pitch | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.20.0] | — |
| 21 | `diagnosis_gi_degree_l_1` | Loudness | slider | slider: MI \| MO \| SE |  |  | [v3.20.0] | [v4.9.0] ([1×](#diagnosis_gi_degree_l_1)) |
| 22 | `diagnosis_gi_degree_l_nature` | Loudness (Indicate the nature of the abnormality): | text | free text |  |  | [v3.20.0] | — |
| 23 | `diagnosis_gi_degree_l_2` | Loudness | radio | consistent=Consistent · intermittent=Intermittent |  |  | [v3.20.0] | — |
| 24 | `diagnosis_gi_degree_comments` | Comments about resonance | radio | normal=Normal · other=Other |  |  | [v3.20.0] | — |
| 25 | `diagnosis_gi_degree_comments_other` | Please specify | text | free text |  |  | [v3.20.0] | — |
| 26 | `diagnosis_gi_degree_comments_other_2` | Additional Features (for example, diplophonia, fry, falsetto, asthenia, aphonia, pitch instability, tremor, wet/gurgly, or other relevant t… | text | free text |  |  | [v3.20.0] | — |
| | **4. Treatment obtained** | | | | | | | |
| 27 | `diagnosis_gi_treatment` | Has the participant undergone any treatment for their condition? | radio | yes=Yes · no=No | ✔ |  | [v3.20.0] | [v4.1.0] ([1×](#diagnosis_gi_treatment)) |
| 28 | `diagnosis_gi_treatment_select` | Select all that apply: | checkbox | voice_or_speech_therapy=Voice/speech therapy · injection_laryngoplasty=Injection laryngoplasty · bilateral_medialization_thyroplasty=Bilateral medialization thyroplasty · other=Other | ✔ |  | [v3.20.0] | — |
| 29 | `diagnosis_gi_treatment_other` | Other, please specify | text | free text | ✔ |  | [v3.20.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `diagnois_gi_gsd`

<details><summary>Does the participant have glottic insufficiency confirmed by laryngoscopy/stroboscopy? — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.20.0] | 2024-11-13 | 🆕 Introduced | | Voice — Glottic Insufficiency / Presbyphonia |
| [v4.0.1] | 2025-08-28 | Label | `Does the patient have a benign lesion confirmed by laryngoscopy/stroboscopy?` | `Does the patient have glottic insufficiency confirmed by laryngoscopy/stroboscopy?` |
| [v4.1.0] | 2025-09-17 | Label | `Does the patient have glottic insufficiency confirmed by laryngoscopy/stroboscopy?` | `Does the participant have glottic insufficiency confirmed by laryngoscopy/stroboscopy?` |

</details>

### `diagnosis_gi_degree_os_1`

<details><summary>Overall Severity — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.20.0] | 2024-11-13 | 🆕 Introduced | | Voice — Glottic Insufficiency / Presbyphonia |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_gi_degree_r_1`

<details><summary>Roughness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.20.0] | 2024-11-13 | 🆕 Introduced | | Voice — Glottic Insufficiency / Presbyphonia |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_gi_degree_b_1`

<details><summary>Breathiness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.20.0] | 2024-11-13 | 🆕 Introduced | | Voice — Glottic Insufficiency / Presbyphonia |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_gi_degree_s_1`

<details><summary>Strain — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.20.0] | 2024-11-13 | 🆕 Introduced | | Voice — Glottic Insufficiency / Presbyphonia |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_gi_degree_p_1`

<details><summary>Pitch — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.20.0] | 2024-11-13 | 🆕 Introduced | | Voice — Glottic Insufficiency / Presbyphonia |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_gi_degree_l_1`

<details><summary>Loudness — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.20.0] | 2024-11-13 | 🆕 Introduced | | Voice — Glottic Insufficiency / Presbyphonia |
| [v4.9.0] | 2026-07-21 | Min | ∅ | `0` |
|  |  | Max | ∅ | `100` |

</details>

### `diagnosis_gi_treatment`

<details><summary>Has the participant undergone any treatment for their condition? — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.20.0] | 2024-11-13 | 🆕 Introduced | | Voice — Glottic Insufficiency / Presbyphonia |
| [v4.1.0] | 2025-09-17 | Label | `Has the patient undergone any treatment for his condition?` | `Has the participant undergone any treatment for their condition?` |

</details>

<!-- milestone links -->
[v3.20.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.20.0
[v4.0.1]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.1
[v4.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.1.0
[v4.9.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.9.0
