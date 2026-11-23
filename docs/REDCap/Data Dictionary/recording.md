<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Recording

**Form name:** `recording` · **Category:** Sessions and Recordings · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.10.0] (2026-08-27)  
**Fields:** 📋 27 in REDCap · ⚫ 0 removed · ✏️ 8 changed since introduction

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| 1 | `recording_id` | Recording ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `recording_acoustic_task_id` | Acoustic Task ID | text | free text | ✔ |  | [v1.0.0] | — |
| 3 | `recording_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 4 | `recording_name` | Recording Name | text | free text | ✔ |  | [v1.0.0] | — |
| 5 | `recording_filepath` | Recording Filepath | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([2×](#recording_filepath)) |
| 6 | `recording_storage_account` | Storage Account | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#recording_storage_account)) |
| 7 | `recording_file_share` | File Share | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#recording_file_share)) |
| 8 | `recording_duration` | Duration (Seconds) | text | free text | ✔ |  | [v1.0.0] | — |
| 9 | `recording_size` | Recording Size (KiB) | text | free text | ✔ |  | [v1.0.0] | — |
| 10 | `recording_created_at` | File Created At | text | free text |  | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#recording_created_at)) |
| 11 | `recording_profile_name` | Recording Profile Name | radio | speech=Speech · breathe=Breathe · cough=Cough | ✔ |  | [v2.0.0] | — |
| 12 | `recording_profile_version`<br><sub>formerly `recording_profile` ([v2.0.0])</sub> | Recording Profile Version | radio | 1=v1.0.0 | ✔ |  | [v1.0.0] | [v2.0.0] ([1×](#recording_profile_version)) |
| 13 | `recording_input_gain` | Recording Input Gain | text | free text | ✔ |  | [v2.0.0] | — |
| 14 | `recording_microphone` | Recording Microphone | text | free text | ✔ |  | [v2.0.0] | — |
| 15 | `recording_origin` | Recording - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App · reproschema=Bridge2AI Reproschema | ✔ |  | [v4.7.0] | [v4.10.0] ([2×](#recording_origin)) |
| 16 | `recording_via` | Recording - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#recording_via)) |
| 17 | `recording_language` | Recording - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#recording_language)) |
| | **Device Metadata** | | | | | | | |
| 18 | `recording_platform` | Recording - Platform | text | free text | ✔ |  | [v4.8.0] | — |
| 19 | `recording_platform_version` | Recording - Platform Version | text | free text | ✔ |  | [v4.8.0] | — |
| 20 | `recording_platform_architecture` | Recording - Platform Architecture | text | free text | ✔ |  | [v4.8.0] | — |
| 21 | `recording_browser` | Recording - Browser | text | free text | ✔ |  | [v4.8.0] | — |
| 22 | `recording_browser_version` | Recording - Browser Version | text | free text | ✔ |  | [v4.8.0] | — |
| 23 | `recording_screen_resolution` | Recording - Screen Resolution | text | free text | ✔ |  | [v4.8.0] | — |
| 24 | `recording_window_resolution` | Recording - Window Resolution | text | free text | ✔ |  | [v4.8.0] | — |
| 25 | `recording_device_info` | Recording - Device Info | text | free text | ✔ |  | [v4.8.0] | — |
| 26 | `recording_device_type` | Recording - Device Type | text | free text | ✔ |  | [v4.8.0] | — |
| 27 | `recording_touch_screen` | Recording - Touch Screen | radio | yes=Yes · no=No · notCertain=Not certain | ✔ |  | [v4.8.0] | — |

## ✏️ Former Variable Names

Variables in this instrument that had a different name in earlier releases. Their history before the rename is included under the current name.

| # | Former name | Current name | Relation | Renamed in |
| :-: | :-- | :-- | :-- | :-: |
| 1 | `recording_profile` | [`recording_profile_version`](#recording_profile_version) | ✏️ Renamed | [v2.0.0] |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `recording_filepath`

<details><summary>Recording Filepath — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Recording |
| [v2.0.0] | 2023-11-15 | Annotation | ∅ | `@READONLY` |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `recording_storage_account`

<details><summary>Storage Account — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Recording |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `recording_file_share`

<details><summary>File Share — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Recording |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `recording_created_at`

<details><summary>File Created At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Recording |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `recording_profile_version`

<details><summary>Recording Profile Version — 1 change · formerly <code>recording_profile</code></summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | as `recording_profile` in Recording |
| [v2.0.0] | 2023-11-15 | ✏️ Renamed | `recording_profile` | `recording_profile_version` |

</details>

### `recording_origin`

<details><summary>Recording - origin — 2 changes</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Recording |
| [v4.8.0] | 2026-06-04 | Label | `Recording Origin` | `Recording - origin` |
| [v4.10.0] | 2026-08-27 | Choices / calculation | 2 options | ➕ `reproschema`=Bridge2AI Reproschema |

</details>

### `recording_via`

<details><summary>Recording - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Recording |
| [v4.8.0] | 2026-06-04 | Label | `Recording via` | `Recording - via` |

</details>

### `recording_language`

<details><summary>Recording - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Recording |
| [v4.8.0] | 2026-06-04 | Label | `Recording Language` | `Recording - Language` |
|  |  | Annotation | ∅ | `@READONLY` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v2.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v2.0.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
[v4.10.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.10.0
