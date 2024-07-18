# bridge2ai-redcap

REDCap Data Dictionary and Metadata for the Bridge2AI project.

[![Github](https://img.shields.io/badge/github-3.9.0-green?style=flat&logo=github)](https://github.com/eipm/bridge2ai-redcap) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![DOI](https://zenodo.org/badge/694816121.svg)](https://zenodo.org/doi/10.5281/zenodo.12760724)


| Version | Date YYYY-mm-dd | Data Dictionary | Metadata | Instrument PDF's |
| :---: | :---: | :---: | :---: | :---: |
| v3.10.0 | 2024-07-18 | [Data Dictionary](data/bridge2ai_voice_project_data_dictionary.csv) | [Metadata](data/bridge2ai_voice_project_metadata.xml) | [Files](data/instrument_pdfs/) |

## Protocol Overview

### Part A | Generic Protocol

| # | Protocol Name | # of Questionnaires | # of Acoustic Tasks | # of Recordings | Estimated time to complete (mm:ss) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Generic Protocol | 6 | 10 | 28 | 37:00 |

### Part B | Disease Specific Protocols

| # | Protocol Name | # of Questionnaires | # of Acoustic Tasks | # of Recordings | Estimated time to complete (mm:ss) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Voice Disorders Protocol | 1 | 3 | 8 | 04:00 | 
| 2 | Mood and Psychiatric Disorders Protocol | 5 | 2 | 2 | 18:30 |
| 3 | Respiratory Disorders | 2 | 2 | 2 | 06:30 |
| 4 | Neurological and Neurodegenerative Disorders | 1 | 4 | 9 | 12:00 |

### Part A & B | Total Metrics per Protocol

| # | Protocol Name | Total # of Questionnaires | Total # of Acoustic Tasks | Total # of Recordings | Estimated time to complete (mm:ss) | 
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Generic Protocol | 6 | 10 | 28 | 37:00 |
| 1 | Voice Disorders Protocol | 7 | 13 | 36 | 41:00 | 
| 2 | Mood and Psychiatric Disorders Protocol | 11 | 12 | 30 | 55:30 |
| 3 | Respiratory Disorders | 8 | 12 | 30 | 43:30 |
| 4 | Neurological and Neurodegenerative Disorders | 7 | 14 | 37 | 49:00 |


## Task Overview

| # | Task Name | Type | Estimated Time to Complete (mm:ss) | Protocol | Total # of Recordings (if Acoustic Task) | Questionnaire Form PDF Link / Acoustic Task Description Youtube Link | 
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Demographics | Questionnaire | 03:00 | Generic Protocol | - | [PDF](data/instrument_pdfs/Q%20Generic%20Demographics.pdf) |
| 2 | Confounders | Questionnaire | 12:00 | Generic Protocol | - | [PDF](data/instrument_pdfs/Q%20Generic%20Confounders.pdf) |
| 3 | Voice Perception | Questionnaire | 00:30 | Generic Protocol | - | [PDF](data/instrument_pdfs/Q%20Generic%20Voice%20Perception.pdf) |
| 4 | VHI-10 | Questionnaire | 01:00 | Generic Protocol | - | [PDF](data/instrument_pdfs/Q%20Generic%20Voice%20Handicap%20Index%20Vhi10.pdf) |
| 5 | Patient Health Questionnaire-9 | Questionnaire | 01:30 | Generic Protocol | - | [PDF](data/instrument_pdfs/Q%20Generic%20Patient%20Health%20Questionnaire9.pdf) |
| 6 | GAD-7 Anxiety | Questionnaire | 01:30 | Generic Protocol | - | [PDF](data/instrument_pdfs/Q%20-%20Generic%20-%20Gad7%20Anxiety.pdf) |
| 7 | Prolonged Vowel | Accoustic Task | 01:00 | Generic Protocol | 1 | [YouTube Link](https://www.youtube.com/watch?v=ZanjPvWkB3M) |
| 8 | Maximum Phonation Time | Accoustic Task | 02:00 | Generic Protocol | 3 | [YouTube Link](https://www.youtube.com/watch?v=1limRFPAtPE) |
| 9 | Rainbow Passage | Accoustic Task | 01:30 | Generic Protocol | 1 | [YouTube Link](https://www.youtube.com/watch?v=Syq_ryCNQKQ) |
| 10 | Glides | Accoustic Task | 01:00 | Generic Protocol | 2 | [YouTube Link](https://www.youtube.com/watch?v=xKBYdkwEOvU)|
| 11 | Loudness | Accoustic Task | 01:00 | Generic Protocol | 1 | [YouTube Link](https://www.youtube.com/watch?v=5ssCSqZPb7Y) |
| 12 | Didaochokinesis | Accoustic Task | 01:00 | Generic Protocol | 5 | [YouTube Link](https://www.youtube.com/watch?v=RlY5KMXtZ4o) |
| 13 | Free Speech | Accoustic Task | 02:00 | Generic Protocol | 10 | [YouTube Link](https://www.youtube.com/watch?v=FqK0WeGCAzg) |
| 14 | Respiration and cough | Accoustic Task | 03:00 | Generic Protocol | 3 | [YouTube Link](https://www.youtube.com/watch?v=Yb4bMj18Iqg) |
| 15 | Picture Description | Accoustic Task | 01:30 | Generic Protocol | 1 | [YouTube Link](https://www.youtube.com/watch?v=abjWJEN6jf8) |
| 16 | Story Recall | Accoustic Task | 03:30 | Generic Protocol | 1 | [YouTube Link](https://www.youtube.com/watch?v=cfkU-N5tWe4) |
| 17 | Voice Problem Severity | Questionnaire | 00:30 | Voice Disorders Protocol | - | [PDF](data/instrument_pdfs/Q%20-%20Voice%20-%20Voice%20Problem%20Severity.pdf) |
| 18 | Caterpillar Passage | Accoustic Task | 01:30 | Voice Disorders Protocol | 1 | [YouTube Link](https://www.youtube.com/watch?v=jN7bGT-PFXY) |
| 19 | Cape V Sentences | Accoustic Task | 01:00 | Voice Disorders Protocol | 6 | [YouTube Link](https://www.youtube.com/watch?v=1qbiCdWxuSY) |
| 20 | Free Speech | Accoustic Task | 01:00 | Voice Disorders Protocol | 1 | [YouTube Link](https://www.youtube.com/watch?v=5QMBSHNLRVI) |
| 21 | PANAS | Questionnaire | 01:00 | Mood and Psychiatric Disorders Protocol | - | [PDF](data/instrument_pdfs/Q%20-%20Mood%20-%20Panas.pdf) |
| 22 | Custom Affect Scale | Questionnaire | 01:30 | Mood and Psychiatric Disorders Protocol | - | [PDF](data/instrument_pdfs/Q%20-%20Mood%20-%20Custom%20Affect%20Scale.pdf) |
| 23 | DSM-5 Adult | Questionnaire | 06:00 | Mood and Psychiatric Disorders Protocol | - | [PDF](data/instrument_pdfs/Q%20-%20Mood%20-%20Dsm5%20Adult.pdf) |
| 24 | PTSD Adult | Questionnaire | 03:00 | Mood and Psychiatric Disorders Protocol | - | [PDF](data/instrument_pdfs/Q%20-%20Mood%20-%20Ptsd%20Adult.pdf) |
| 25 | ADHD Adult | Questionnaire | 03:00 | Mood and Psychiatric Disorders Protocol | - | [PDF](data/instrument_pdfs/Q%20-%20Mood%20-%20Adhd%20Adult.pdf) |
| 26 | Animal Fluency | Accoustic Task | 01:30 | Mood and Psychiatric Disorders Protocol | 1 | [YouTube Link](https://www.youtube.com/watch?v=4lkEAxDiEE8) |
| 27 | Open response questions | Accoustic Task | 02:30 | Mood and Psychiatric Disorders Protocol | 1 | [YouTube Link](https://www.youtube.com/watch?v=THfOnGCaALA) |
| 28 | Dyspnea Index (DI) | Questionnaire | 01:00 | Respiratory Disorders | - | [PDF](data/instrument_pdfs/Q%20-%20Resp%20-%20Dyspnea%20Index%20Di.pdf) |
| 29 | Leicester Cough Questionnaire (LCQ) | Questionnaire | 03:00 | Respiratory Disorders | - | [PDF](data/instrument_pdfs/Q%20-%20Resp%20-%20Leicester%20Cough%20Questionnaire%20Lcq.pdf) |
| 30 | Breath Sounds | Accoustic Task | 01:30 | Respiratory Disorders | 1 | [YouTube Link](https://www.youtube.com/watch?v=2rLMfMjS_R0) |
| 31 | Voluntary Cough | Accoustic Task | 01:00 | Respiratory Disorders | 1 | [YouTube Link](https://www.youtube.com/watch?v=i7BhlwNMk28) |
| 32 | Winograd Questionnaire | Questionnaire | 01:00 | Neurological and Neurodegenerative Disorders | - | [PDF](data/instrument_pdfs/Q%20-%20Neuro%20Winograd%20Schemas.pdf) |
| 33 | Word-color Stroop | Accoustic Task | 01:30 | Neurological and Neurodegenerative Disorders | 1 | [YouTube Link](https://www.youtube.com/watch?v=IzotHKbYh30)|
| 34 | Productive Vocabulary | Accoustic Task | 05:00 | Neurological and Neurodegenerative Disorders | 6 | [YouTube Link](https://www.youtube.com/watch?v=TEshcUAlfPA) |
| 35 | Random Item Generation | Accoustic Task | 02:30 | Neurological and Neurodegenerative Disorders | 1 | [YouTube Link](https://www.youtube.com/watch?v=ry__w1Mm2aE) |
| 36 | Cinderella Story | Accoustic Task | 05:00 | Neurological and Neurodegenerative Disorders | 1 | [YouTube Link](https://www.youtube.com/watch?v=eHx-vetG8Fk) |

## Clinically Validated Diagnosis Forms

| # | Protocol | Name | Form PDF Link |
| :---: | :---: | :---: | :---: |
| 1 | Voice Disorders Protocol | Benign Lessions | [PDF](data/instrument_pdfs/D%20Voice%20Benign%20Lesions.pdf) |
| 2 | Voice Disorders Protocol | Laryngeal Cancer | [PDF](data/instrument_pdfs/D%20Voice%20Laryngeal%20Cancer.pdf) |
| 3 | Voice Disorders Protocol | Laryngitis | [PDF](data/instrument_pdfs/D%20Voice%20Laryngitis.pdf) |
| 4 | Voice Disorders Protocol | Muscle Tension Dysphonia | [PDF](data/instrument_pdfs/D%20Voice%20Muscle%20Tension%20Dysphonia%20Mtd.pdf) |
| 5 | Voice Disorders Protocol | Precancerous Lessions | [PDF](data/instrument_pdfs/D%20Voice%20Precancerous%20Lesions.pdf) |
| 6 | Voice Disorders Protocol | Laryngeal Dystonia | [PDF](data/instrument_pdfs/D%20Voice%20Laryngeal%20Dystonia.pdf) |
| 7 | Voice Disorders Protocol | Unilateral vocal fold paralysis | [PDF](data/instrument_pdfs/D%20Voice%20Unilateral%20Vocal%20Fold%20Paralysis.pdf) |
| 8 | Mood and Psychiatric Disorders Protocol | Bipolar Disorder | [PDF](data/instrument_pdfs/D%20Mood%20Bipolar%20Disorder.pdf) |
| 9 | Mood and Psychiatric Disorders Protocol | Depression or Major Depressive Disorder | [PDF](data/instrument_pdfs/D%20Mood%20Depression%20Or%20Major%20Depressive%20Disorder.pdf) |
| 10 | Respiratoty Disorders | Airway Stenosis | [PDF](data/instrument_pdfs/D%20Resp%20Airway%20Stenosis.pdf) |
| 11 | Neurological and Neurodegenerative Disorders | Alzheimer's, dementia, or mild cognitive impairment | [PDF](data/instrument_pdfs/D%20Neuro%20Alzheimers%20Disease%20Mild%20Cognitive%20Impairment.pdf) |
| 12 | Neurological and Neurodegenerative Disorders | Amyotrophic Lateral Sclerosis (ALS) | [PDF](data/instrument_pdfs/D%20Neuro%20Amyotrophic%20Lateral%20Sclerosis%20Als.pdf) |
| 13 | Neurological and Neurodegenerative Disorders | Parkinson's disease | [PDF](data/instrument_pdfs/D%20Neuro%20Parkinsons%20Disease.pdf) |
| 14 | Control | Control | [PDF](data/instrument_pdfs/D%20Control.pdf) |