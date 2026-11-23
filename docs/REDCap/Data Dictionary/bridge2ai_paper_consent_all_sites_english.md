<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Bridge2AI Paper Consent — All Sites (English)

**Form name:** `bridge2ai_paper_consent_all_sites_english` · **Category:** Consents · **Status:** 🟢 Active  
**Introduced:** [v2.0.0] (2023-11-15) · **Last changed:** [v3.6.0] (2024-06-10)  
**Fields:** 📋 4 in REDCap · ⚫ 0 removed · ✏️ 3 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Paper Consent Form for all Sites** | | | | | | | |
| 1 | `paper_consent_notes` | Fill out Instructions 1. Upload the .pdf of the paper consent. 2. Select the Enrollment Institution. 3. Paper Consent Uploaded By is automa… | descriptive | _display only — no data_ |  |  | [v2.0.0] | — |
| 2 | `paper_consent_pdf_all_sites` | Paper Consent PDF - All Sites | file | file upload | ✔ | 🔒 | [v2.0.0] | [v3.3.0] ([1×](#paper_consent_pdf_all_sites)) |
| 3 | `paper_consent_enrollment_institution` | Enrollment Institution | dropdown | bch=BCH · mit=MIT · mt_sinai=Mt. Sinai · sickkids=SickKids … (7 options) | ✔ |  | [v2.0.0] | [v3.6.0] ([2×](#paper_consent_enrollment_institution)) |
| 4 | `paper_consent_uploaded_by` | Paper Consent Uploaded By | text | free text | ✔ | 🔒 | [v2.0.0] | [v3.3.0] ([1×](#paper_consent_uploaded_by)) |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `paper_consent_pdf_all_sites`

<details><summary>Paper Consent PDF - All Sites — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Bridge2AI Paper Consent — All Sites (English) |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `paper_consent_enrollment_institution`

<details><summary>Enrollment Institution — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Bridge2AI Paper Consent — All Sites (English) |
| [v3.0.0] | 2023-12-08 | Choices / calculation | 6 options | ➕ `bch`=BCH, `mit`=MIT, `usf`=USF, `vumc`=VUMC, `wcm`=WCM<br>➖ `BCH`=BCH, `MIT`=MIT, `USF`=USF, `VUMC`=VUMC, `WCM`=WCM |
| [v3.6.0] | 2024-06-10 | Choices / calculation | 6 options | ➕ `sickkids`=SickKids |

</details>

### `paper_consent_uploaded_by`

<details><summary>Paper Consent Uploaded By — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v2.0.0] | 2023-11-15 | 🆕 Introduced | | Bridge2AI Paper Consent — All Sites (English) |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

<!-- milestone links -->
[v2.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v2.0.0
[v3.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.0.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v3.6.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.6.0
