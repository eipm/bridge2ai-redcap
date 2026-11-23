<p align="center">
    <img src="../../../images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="../../../images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

[![Back to Data Dictionary](https://img.shields.io/badge/back%20to%20data%20dictionary-8A2BE2)](Data%20Dictionary.md)

# Custom Affect Scale

**Form name:** `q_mood_custom_affect_scale` · **Category:** Adult Questionnaires (Mood & Psychiatric) · **Status:** 🟢 Active  
**Introduced:** [v1.0.0] (2023-09-21) · **Last changed:** [v4.8.0] (2026-06-04)  
**Fields:** 📋 20 in REDCap · ⚫ 0 removed · ✏️ 5 changed since introduction

**Instrument renames** (field variables were unchanged):

| Milestone | Date | Previous form name | New form name |
| :-: | :-: | :-- | :-- |
| [v3.1.0] | 2024-01-24 | `questionnaire_mood_disorders_custom_affect_scale` | `q_mood_custom_affect_scale` |

## 📋 Fields

| # | Variable | Label | Type | Values | Req. | PHI | Introduced | Last changed |
| :-: | :-- | :-- | :-- | :-- | :-: | :-: | :-: | :-: |
| | **Questionnaire - Metadata** | | | | | | | |
| 1 | `custom_affect_scale_session_id` | Session ID | text | free text | ✔ |  | [v1.0.0] | — |
| 2 | `custom_affect_scale_started_at` | Questionnaire Started At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#custom_affect_scale_started_at)) |
| 3 | `custom_affect_scale_completed_at` | Questionnaire Completed At | text | free text | ✔ | 🔒 | [v1.0.0] | [v3.3.0] ([1×](#custom_affect_scale_completed_at)) |
| 4 | `custom_affect_scale_duration` | Questionnaire Duration (seconds) | text | `number` [0–] |  |  | [v1.0.0] | — |
| 5 | `custom_affect_scale_origin` | Custom Affect Scale - origin | radio | app=Bridge2AI App · website=Bridge2AI Web App | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#custom_affect_scale_origin)) |
| 6 | `custom_affect_scale_via` | Custom Affect Scale - via | radio | dataCollector=Data Collector · participant=Participant | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#custom_affect_scale_via)) |
| 7 | `custom_affect_scale_language` | Custom Affect Scale - Language | radio | 1=English · 3=Spanish | ✔ |  | [v4.7.0] | [v4.8.0] ([1×](#custom_affect_scale_language)) |
| | **Thinking about yourself and how you normally feel, to what extent do you generally feel? 0=Not at all, 10=Extremely** | | | | | | | |
| 8 | `sad_or_down` | Sad or down | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |
| 9 | `joyful` | Joyful | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |
| 10 | `motivated` | Motivated or interested | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |
| 11 | `lack_of_pleasure` | Lack of pleasure (in things you tend to enjoy) | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |
| 12 | `tired` | Tired or fatigued | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |
| 13 | `energetic` | Energetic | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |
| 14 | `agitated` | Agitated (restless, fidgety, pacing, cannot sit still) | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |
| 15 | `irritated` | Irritated or angry (towards something or someone) | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |
| 16 | `lonely` | Lonely or isolated | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |
| 17 | `concentrated` | Concentrated (not distracted or inattentive) | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |
| 18 | `relaxed` | Relaxed or calm | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |
| 19 | `worried` | Worried or anxious | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |
| 20 | `desire_to_escape` | Desire to escape (your thoughts and/or feelings) | radio | 0=0 · 1=1 · 2=2 · 3=3 … (11 options) | ✔ |  | [v1.0.0] | — |

## 🕘 Change History

Fields listed in dictionary order. Each entry shows every release where that field changed.

### `custom_affect_scale_started_at`

<details><summary>Questionnaire Started At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - Custom Affect Scale |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `custom_affect_scale_completed_at`

<details><summary>Questionnaire Completed At — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v1.0.0] | 2023-09-21 | 🆕 Introduced | | Questionnaire - Mood Disorders - Custom Affect Scale |
| [v3.3.0] | 2024-03-13 | Identifier (PHI) | No | Yes |

</details>

### `custom_affect_scale_origin`

<details><summary>Custom Affect Scale - origin — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Custom Affect Scale |
| [v4.8.0] | 2026-06-04 | Label | `Custom Affect Scale Origin` | `Custom Affect Scale - origin` |

</details>

### `custom_affect_scale_via`

<details><summary>Custom Affect Scale - via — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Custom Affect Scale |
| [v4.8.0] | 2026-06-04 | Label | `Custom Affect Scale via` | `Custom Affect Scale - via` |

</details>

### `custom_affect_scale_language`

<details><summary>Custom Affect Scale - Language — 1 change</summary>

| Milestone | Date | What changed | Before | After |
| :-: | :-: | :-- | :-- | :-- |
| [v4.7.0] | 2026-05-04 | 🆕 Introduced | | Custom Affect Scale |
| [v4.8.0] | 2026-06-04 | Label | `Custom Affect Scale Language` | `Custom Affect Scale - Language` |

</details>

<!-- milestone links -->
[v1.0.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v1.0.0
[v3.1.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.1.0
[v3.3.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v3.3.0
[v4.7.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.7.0
[v4.8.0]: https://github.com/eipm/bridge2ai-redcap/releases/tag/v4.8.0
