<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Pediatric — Voice-Related QoL Survey

**Form name:** `pediatric_q_generic_voice_related_qol_survey` · **Category:** Pediatric · **Status:** 🟢 Active  
**Introduced:** [v3.15.0] (2024-10-07) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 16 in REDCap · ⚫ 0 removed · ✏️ 12 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `peds_qol_session_id` | Session ID | text | free text | ✔ |  | [v3.15.0] | — |
| 2 | `peds_qol_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v3.15.0] | — |
| 3 | `peds_qol_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v3.15.0] | — |
| 4 | `peds_qol_duration` | Questionnaire Duration (seconds) | text | free text |  |  | [v3.15.0] | — |
| 5 | `peds_qol_origin` | Peds Voice Related QoL Survey - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App · reproschema=Bridge2AI Reproschema | ✔ |  | [v4.7.0] | [v4.10.0] ([2×](#peds_qol_origin)) |
| 6 | `peds_qol_via` | Peds Voice Related QoL Survey - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#peds_qol_via)) |
| 7 | `peds_qol_language` | Peds Voice Related QoL Survey - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#peds_qol_language)) |
| | **Please answer these questions based on what your child's voice (your own voice if you are a teenage respondent) has bee…** | | | | | | | |
| 8 | `peds_qol_trouble_speaking_heard` | My child/ I has trouble speaking loudly or being heard in noisy situations. | radio | none=None, not a problem · aSmallAmount=A small amount · aModerateAmount=A moderate amount · aLot=A lot … (6 options) |  |  | [v3.15.0] | [v4.0.0] ([1×](#peds_qol_trouble_speaking_heard)) |
| 9 | `peds_qol_out_of_air` | My child/ I runs out of air and needs to take frequent breaths when talking. | radio | none=None, not a problem · aSmallAmount=A small amount · aModerateAmount=A moderate amount · aLot=A lot … (6 options) |  |  | [v3.15.0] | [v4.0.0] ([1×](#peds_qol_out_of_air)) |
| 10 | `peds_qol_come_out_speaking` | My child/ I sometimes does not know what will come out when they begin speaking. | radio | none=None, not a problem · aSmallAmount=A small amount · aModerateAmount=A moderate amount · aLot=A lot … (6 options) |  |  | [v3.15.0] | [v4.0.0] ([1×](#peds_qol_come_out_speaking)) |
| 11 | `peds_qol_anxious_frustrated` | My child/ I is sometimes anxious or frustrated (because of their voice). | radio | none=None, not a problem · aSmallAmount=A small amount · aModerateAmount=A moderate amount · aLot=A lot … (6 options) |  |  | [v3.15.0] | [v4.0.0] ([1×](#peds_qol_anxious_frustrated)) |
| 12 | `peds_qol_depressed` | My child/ I is sometimes depressed (because of their voice). | radio | none=None, not a problem · aSmallAmount=A small amount · aModerateAmount=A moderate amount · aLot=A lot … (6 options) |  |  | [v3.15.0] | [v4.0.0] ([1×](#peds_qol_depressed)) |
| 13 | `peds_qol_trouble_phone_speaking` | My child/ I has trouble using the phone or speaking with friends in person. | radio | none=None, not a problem · aSmallAmount=A small amount · aModerateAmount=A moderate amount · aLot=A lot … (6 options) |  |  | [v3.15.0] | [v4.0.0] ([1×](#peds_qol_trouble_phone_speaking)) |
| 14 | `peds_qol_trouble_doing_schoolwork` | My child/ I has trouble doing their schoolwork or job (because of their voice). | radio | none=None, not a problem · aSmallAmount=A small amount · aModerateAmount=A moderate amount · aLot=A lot … (6 options) |  |  | [v3.15.0] | [v4.0.0] ([1×](#peds_qol_trouble_doing_schoolwork)) |
| 15 | `peds_qol_repeat_understood` | My child/ I has to repeat themselves to be understood. | radio | none=None, not a problem · aSmallAmount=A small amount · aModerateAmount=A moderate amount · aLot=A lot … (6 options) |  |  | [v3.15.0] | [v4.0.0] ([1×](#peds_qol_repeat_understood)) |
| 16 | `peds_qol_less_outgoing` | My child has become less outgoing (because of their voice). | radio | none=None, not a problem · aSmallAmount=A small amount · aModerateAmount=A moderate amount · aLot=A lot … (6 options) |  |  | [v3.15.0] | [v4.0.0] ([1×](#peds_qol_less_outgoing)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `peds_qol_origin`

<details><summary>Peds Voice Related QoL Survey - origin — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — Voice-Related QoL Survey |
| [v4.8.0] | 2026-06-04 | Label | `Peds Voice Related QoL Survey Origin` | `Peds Voice Related QoL Survey - origin` |
| [v4.10.0] | 2026-08-27 | Choices / calculation | 2 options | ➕ `reproschema`=Bridge2AI Reproschema |

</details>

### `peds_qol_via`

<details><summary>Peds Voice Related QoL Survey - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — Voice-Related QoL Survey |
| [v4.8.0] | 2026-06-04 | Label | `Peds Voice Related QoL Survey via` | `Peds Voice Related QoL Survey - via` |

</details>

### `peds_qol_language`

<details><summary>Peds Voice Related QoL Survey - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Pediatric — Voice-Related QoL Survey |
| [v4.8.0] | 2026-06-04 | Label | `Peds Voice Related QoL Survey Language` | `Peds Voice Related QoL Survey - Language` |

</details>

### `peds_qol_trouble_speaking_heard`

<details><summary>My child/ I has trouble speaking loudly or being heard in noisy situations. — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Voice-Related QoL Survey |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 6 options | ✏️ `none`: None → None, not a problem |

</details>

### `peds_qol_out_of_air`

<details><summary>My child/ I runs out of air and needs to take frequent breaths when talking. — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Voice-Related QoL Survey |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 6 options | ✏️ `none`: None → None, not a problem |

</details>

### `peds_qol_come_out_speaking`

<details><summary>My child/ I sometimes does not know what will come out when they begin speaking. — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Voice-Related QoL Survey |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 6 options | ✏️ `none`: None → None, not a problem |

</details>

### `peds_qol_anxious_frustrated`

<details><summary>My child/ I is sometimes anxious or frustrated (because of their voice). — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Voice-Related QoL Survey |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 6 options | ✏️ `none`: None → None, not a problem |

</details>

### `peds_qol_depressed`

<details><summary>My child/ I is sometimes depressed (because of their voice). — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Voice-Related QoL Survey |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 6 options | ✏️ `none`: None → None, not a problem |

</details>

### `peds_qol_trouble_phone_speaking`

<details><summary>My child/ I has trouble using the phone or speaking with friends in person. — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Voice-Related QoL Survey |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 6 options | ✏️ `none`: None → None, not a problem |

</details>

### `peds_qol_trouble_doing_schoolwork`

<details><summary>My child/ I has trouble doing their schoolwork or job (because of their voice). — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Voice-Related QoL Survey |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 6 options | ✏️ `none`: None → None, not a problem |

</details>

### `peds_qol_repeat_understood`

<details><summary>My child/ I has to repeat themselves to be understood. — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Voice-Related QoL Survey |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 6 options | ✏️ `none`: None → None, not a problem |

</details>

### `peds_qol_less_outgoing`

<details><summary>My child has become less outgoing (because of their voice). — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.15.0] | 2024-10-07 | 🆕 Introduced | | Pediatric — Voice-Related QoL Survey |
| [v4.0.0] | 2025-08-19 | Choices / calculation | 6 options | ✏️ `none`: None → None, not a problem |

</details>

<!-- milestone links -->
[v3.15.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.15.0
[v4.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.0.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
