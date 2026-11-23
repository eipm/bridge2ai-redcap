<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# MoCA

**Form name:** `q_neuro_moca` · **Category:** Adult Questionnaires (Neurological & Neurodegenerative) · **Status:** 🟢 Active  
**Introduced:** [v3.2.0] (2024-02-07) · **Last changed:** [v3.3.0] (2024-03-13)  
**Fields:** 📋 3 in REDCap · ⚫ 0 removed · ✏️ 2 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **MoCA Test Questionnaire** | | | | | | | |
| 1 | `moca_notes` | Steps to download MoCA test results from the DUO app and upload them here: Export MoCA test results in .pdf format to your Sinai email ID f… | descriptive | _display only — no data_ |  |  | [v3.2.0] | — |
| 2 | `moca_duo_pdf` | MoCA DUO PDF | file | file upload | ✔ | 🔒 | [v3.2.0] | [v3.3.0] ([1×](#moca_duo_pdf)) |
| 3 | `moca_pdf_uploaded_by` | MoCA DUO PDF Uploaded By | text | free text | ✔ | 🔒 | [v3.2.0] | [v3.3.0] ([1×](#moca_pdf_uploaded_by)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `moca_duo_pdf`

<details><summary>MoCA DUO PDF — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.2.0] | 2024-02-07 | 🆕 Introduced | | MoCA |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `moca_pdf_uploaded_by`

<details><summary>MoCA DUO PDF Uploaded By — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v3.2.0] | 2024-02-07 | 🆕 Introduced | | MoCA |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

<!-- milestone links -->
[v3.2.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.2.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
