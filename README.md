<p align="center">
    <img src="images/main_logo_black.svg#gh-light-mode-only" width="200" alt="B2Ai Voice Logo">
    <img src="images/main_logo_white.svg#gh-dark-mode-only" width="200" alt="B2Ai Voice Logo"><br>
    Voice as a Biomarker of Health
</p>

# bridge2ai-redcap

REDCap Data Dictionary and Metadata for the Bridge2AI project.

[![GitHub](https://img.shields.io/badge/github-4.6.0-green?style=flat&logo=github)](https://github.com/eipm/bridge2ai-redcap) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12760724.svg)](https://zenodo.org/doi/10.5281/zenodo.12760724)

| Version | Date YYYY-mm-dd |                           Data Dictionary                           |                       Metadata                        |   PDF's (English)    |    PDF's (Spanish)    |
| :-----: | :-------------: | :-----------------------------------------------------------------: | :---------------------------------------------------: | :------------------: | :-------------------: |
| v4.6.0  |   2026-04-01    | [Data Dictionary](data/bridge2ai_voice_project_data_dictionary.csv) | [Metadata](data/bridge2ai_voice_project_metadata.xml) | [Files](data/en-us/) | [Files](data/es-419/) |

## 🤝 License

See [LICENSE](./LICENSE)

## 📚 How to Cite

> Bensoussan, Y., Ghosh, S. S., Rameau, A., Boyer, M., Bahr, R., Watts, S., Rudzicz, F., Bolser, D., Lerner-Ellis, J., Awan, S., Powell, M. E., Belisle-Pipon, J.-C., Ravitsky, V., Johnson, A., Zisimopoulos, P., Tang, J., Sigaras, A., Elemento, O., Dorr, D., … Bridge2AI-Voice. (2024). eipm/bridge2ai-redcap. Zenodo. [https://zenodo.org/doi/10.5281/zenodo.12760724](https://zenodo.org/doi/10.5281/zenodo.12760724)

## Table of Contents

- [eConsent Forms](#econsent-forms)
- [Adult Protocols](#adult-protocols)
  - [Adult Generic Protocol (Controls)](<docs/adults/Generic%20Protocol%20(Controls).md>)
  - [Adult Voice Disorders Protocol](docs/adults/Voice%20Disorders%20Protocol.md)
  - [Adult Mood and Psychiatric Disorders Protocol](docs/adults/Mood%20and%20Psychiatric%20Disorders%20Protocol.md)
  - [Adult Respiratory Disorders Protocol](docs/adults/Respiratory%20Disorders%20Protocol.md)
  - [Adult Neurological and Neurodegenerative Disorders Protocol](docs/adults/Neurological%20and%20Neurodegenerative%20Disorders%20Protocol.md)
- [Pediatric Protocols](#pediatric-protocols)
  - [Pediatric Disorders - Ages \[2-4)](<docs/pediatrics/Pediatric%20Disorders%20-%20Ages%20[2-4).md>)
  - [Pediatric Disorders - Ages \[4-6)](<docs/pediatrics/Pediatric%20Disorders%20-%20Ages%20[4-6).md>)
  - [Pediatric Disorders - Ages \[6-10)](<docs/pediatrics/Pediatric%20Disorders%20-%20Ages%20[6-10).md>)
  - [Pediatric Disorders - Ages 10+](docs/pediatrics/Pediatric%20Disorders%20-%20Ages%2010%2B.md)

## eConsent Forms

|  #  | Site | Language |                                                     English PDF                                                      |                                                      Spanish PDF                                                      |
| :-: | :--- | :------- | :------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------: |
|  1  | USF  | English  | [Bridge2AI eConsent - USF - English](data/en-us/Consent%20-%20PDFs/Bridge2AI%20eConsent%20-%20USF%20-%20English.pdf) | [Bridge2AI eConsent - USF - Spanish](data/es-419/Consent%20-%20PDFs/Bridge2AI%20eConsent%20-%20USF%20-%20Spanish.pdf) |
|  2  | MIT  | English  | [Bridge2AI eConsent - MIT - English](data/en-us/Consent%20-%20PDFs/Bridge2AI%20eConsent%20-%20MIT%20-%20English.pdf) |                                                          NA                                                           |

## Adult Protocols

|  #  | 📓 Protocol Name                                                                                                                      | Clinical Diagnoses                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 📕 # of Questionnaires | 🎤 # of Acoustic Tasks | 🔊 # of Recordings | ⏳ Estimated time to complete (mm:ss) |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------: | :--------------------: | :----------------: | :-----------------------------------: |
|  1  | [Generic Protocol (Controls)](<docs/adults/Generic%20Protocol%20(Controls).md>)                                                       | <ul><li>[controls](data/en-us/Diagnosis%20-%20PDFs/Generic/D%20-%20Control.pdf)</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |           6            |           10           |         41         |                 38:45                 |
|  2  | [Voice Disorders Protocol](docs/adults/Voice%20Disorders%20Protocol.md)                                                               | <ul><li>[Benign Lesions](data/en-us/Diagnosis%20-%20PDFs/Voice/D%20-%20Voice%20-%20Benign%20Lesions.pdf)</li><li>[Voice Glottic Insufficiency / Presbyphonia](data/en-us/Diagnosis%20-%20PDFs/Voice/D%20-%20Voice%20-%20Glottic%20Insufficiency%20Presbyphonia.pdf)</li><li>[Laryngeal Cancer](data/en-us/Diagnosis%20-%20PDFs/Voice/D%20-%20Voice%20-%20Laryngeal%20Cancer.pdf)</li><li>[Laryngitis](data/en-us/Diagnosis%20-%20PDFs/Voice/D%20-%20Voice%20-%20Laryngitis.pdf)</li><li>[Muscle Tension Dysphonia (MTD)](<data/en-us/Diagnosis%20-%20PDFs/Voice/D%20-%20Voice%20-%20Muscle%20Tension%20Dysphonia%20(MTD).pdf>)</li><li>[Precancerous Lesions](data/en-us/Diagnosis%20-%20PDFs/Voice/D%20-%20Voice%20-%20Precancerous%20Lesions.pdf)</li><li>[Laryngeal Dystonia](data/en-us/Diagnosis%20-%20PDFs/Voice/D%20-%20Voice%20-%20Laryngeal%20Dystonia.pdf)</li><li>[Unilateral vocal fold paralysis](data/en-us/Diagnosis%20-%20PDFs/Voice/D%20-%20Voice%20-%20Unilateral%20Vocal%20Fold%20Paralysis.pdf)</li></ul> |           6            |           12           |         47         |                 42:25                 |
|  3  | [Mood and Psychiatric Disorders Protocol](docs/adults/Mood%20and%20Psychiatric%20Disorders%20Protocol.md)                             | <ul><li>[Anxiety Disorder](data/en-us/Diagnosis%20-%20PDFs/Mood/D%20-%20Mood%20-%20Anxiety%20Disorder.pdf)</li><li>[Bipolar Disorder](data/en-us/Diagnosis%20-%20PDFs/Mood/D%20-%20Mood%20-%20Bipolar%20Disorder.pdf)</li><li>[Depression or Major Depressive Disorder](data/en-us/Diagnosis%20-%20PDFs/Mood/D%20-%20Mood%20-%20Mood%20Depression%20Or%20Major%20Depressive%20Disorder.pdf)</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |           10           |           10           |         41         |                 46:00                 |
|  4  | [Respiratory Disorders Protocol](docs/adults/Respiratory%20Disorders%20Protocol.md)                                                   | <ul><li>[Airway Stenosis](data/en-us/Diagnosis%20-%20PDFs/Resp/D%20-%20Resp%20-%20Airway%20Stenosis.pdf)</li><li>[COPD and Asthma](data/en-us/Diagnosis%20-%20PDFs/Resp/D%20-%20Resp%20-%20COPD%20And%20Asthma.pdf)</li><li>[Unexplained Chronic Cough](data/en-us/Diagnosis%20-%20PDFs/Resp/D%20-%20Resp%20-%20Unexplained%20Chronic%20Cough.pdf)</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |           8            |           10           |         41         |                 42:05                 |
|  5  | [Neurological and Neurodegenerative Disorders Protocol](docs/adults/Neurological%20and%20Neurodegenerative%20Disorders%20Protocol.md) | <ul><li>[Alzheimer's, dementia, or mild cognitive impairment](data/en-us/Diagnosis%20-%20PDFs/Neuro/D%20-%20Neuro%20-%20Alzheimer's%20disease,%20Mild%20Cognitive%20Impairment%20and%20other%20types%20of%20Dementia.pdf)</li><li>[Amyotrophic Lateral Sclerosis (ALS)](<data/en-us/Diagnosis%20-%20PDFs/Neuro/D%20-%20Neuro%20-%20Amyotrophic%20Lateral%20Sclerosis%20(ALS).pdf>)</li><li>[Huntington's Disease](data/en-us/Diagnosis%20-%20PDFs/Neuro/D%20-%20Neuro%20-%20Huntington's%20Disease.pdf)</li><li>[Parkinson's Disease](data/en-us/Diagnosis%20-%20PDFs/Neuro/D%20-%20Neuro%20-%20Parkinson's%20Disease.pdf)</li></ul>                                                                                                                                                                                                                                                                                                                                                                                          |           6            |           13           |         44         |                 45:30                 |

## Pediatric Protocols

|  #  | 📓 Protocol Name                                                                                               | Clinical Diagnoses                                                                                                                                                                                     | 📕 # of Questionnaires | 🎤 # of Acoustic Tasks | 🔊 # of Recordings | ⏳ Estimated time to complete (mm:ss) |
| :-: | :------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------: | :--------------------: | :----------------: | :-----------------------------------: |
|  1  | [Pediatric Disorders - Ages \[2-4\) Protocol](<docs/pediatrics/Pediatric%20Disorders%20-%20Ages%20[2-4).md>)   | <ul><li>[Healthy Developmentally Typical Children](../../data/en-us/Diagnosis%20-%20PDFs/Pediatric%20-%20Generic/D%20-%20Pediatric%20-%20Healthy%20Developmentally%20Typical%20Children.pdf)</li></ul> |           6            |           4            |         50         |                  NA                   |
|  2  | [Pediatric Disorders - Ages \[4-6\) Protocol](<docs/pediatrics/Pediatric%20Disorders%20-%20Ages%20[4-6).md>)   | <ul><li>[Healthy Developmentally Typical Children](../../data/en-us/Diagnosis%20-%20PDFs/Pediatric%20-%20Generic/D%20-%20Pediatric%20-%20Healthy%20Developmentally%20Typical%20Children.pdf)</li></ul> |           6            |           8            |         87         |                  NA                   |
|  3  | [Pediatric Disorders - Ages \[6-10\) Protocol](<docs/pediatrics/Pediatric%20Disorders%20-%20Ages%20[6-10).md>) | <ul><li>[Healthy Developmentally Typical Children](../../data/en-us/Diagnosis%20-%20PDFs/Pediatric%20-%20Generic/D%20-%20Pediatric%20-%20Healthy%20Developmentally%20Typical%20Children.pdf)</li></ul> |           6            |           9            |         101         |                  NA                   |
|  4  | [Pediatric Disorders - Ages 10+ Protocol](docs/pediatrics/Pediatric%20Disorders%20-%20Ages%2010%2B.md)         | <ul><li>[Healthy Developmentally Typical Children](../../data/en-us/Diagnosis%20-%20PDFs/Pediatric%20-%20Generic/D%20-%20Pediatric%20-%20Healthy%20Developmentally%20Typical%20Children.pdf)</li></ul> |           6            |           9            |         92        |                  NA                   |

## Acknowledgements

This study was supported in part by the Weill Cornell Medicine Clinical and Translational Science Center (CTSC) grant (UL1 TR 002384).

Study data were collected and managed using REDCap electronic data capture tools hosted at Weill Cornell Medicine.<sup>1,2,3</sup> REDCap (Research Electronic Data Capture) is a secure, web-based software platform designed to support data capture for research studies, providing 1) an intuitive interface for validated data capture; 2) audit trails for tracking data manipulation and export procedures; 3) automated export procedures for seamless data downloads to common statistical packages; and 4) procedures for data integration and interoperability with external sources.

## Citations

<sup>1</sup>PA Harris, R Taylor, R Thielke, J Payne, N Gonzalez, JG. Conde, Research electronic data capture (REDCap) – A metadata-driven methodology and workflow process for providing translational research informatics support, J Biomed Inform. 2009 Apr;42(2):377-81.

<sup>2</sup>PA Harris, R Taylor, BL Minor, V Elliott, M Fernandez, L O’Neal, L McLeod, G Delacqua, F Delacqua, J Kirby, SN Duda, REDCap Consortium, The REDCap consortium: Building an international community of software partners, J Biomed Inform. 2019 May 9 [doi: 10.1016/j.jbi.2019.103208]

<sup>3</sup>Lawrence CE, Dunkel L, McEver M, Israel T, Taylor R, Chiriboga G, Goins KV, Rahn EJ, Mudano AS, Roberson ED, Chambless C, Wadley VG, Danila MI, Fischer MA, Joosten Y, Saag KG, Allison JJ, Lemon SC, Harris PA, "A REDCap-based model for electronic consent (eConsent): Moving toward a more personalized consent", J Clin Transl Sci. 2020 Apr 3;4(4):345-353. https://doi.org/10.1017/cts.2020.30

## Credits for Validated Questionnaires and Acoustic Tasks in the Bridge2AI-Voice Protocol.

### Copyrights
 
**Adult ADHD Self-Report Scale (ASRS v1.1)**

Copyright © 2003 World Health Organization. Reprinted with permission of WHO. All rights reserved. 

**Positive and Negative Affect Schedule (PANAS)**

© 1988 American Psychological Association (APA). Watson, D., Clark, L.A., & Tellegen, A. 

**WHODAS 2.0**

Copyright © 2012 World Health Organization. 

### References

<u><b>Mental Health Assessments</b></u>
- Kroenke K, Spitzer RL, Williams JB. The PHQ-9: validity of a brief depression severity measure. J Gen Intern Med. 2001;16(9):606-613. doi:10.1046/j.1525-1497.2001.016009606.x 
- Spitzer RL, Kroenke K, Williams JBW, Löwe B. A brief measure for assessing generalized anxiety disorder: the GAD-7. Arch Intern Med. 2006;166(10):1092-1097. doi:10.1001/archinte.166.10.1092 
- Kessler RC, Adler L, Ames M, et al. The World Health Organization Adult ADHD Self-Report Scale (ASRS): a short screening scale for use in the general population. Psychol Med. 2005;35(2):245-256. doi:10.1017/S0033291704002892 
- Watson D, Clark LA, Tellegen A. Development and validation of brief measures of positive and negative affect: the PANAS scales. J Pers Soc Psychol. 1988;54(6):1063-1070. doi:10.1037/0022-3514.54.6.1063 
- Üstün TB, Kostanjsek N, Chatterji S, Rehm J, eds. Measuring Health and Disability: Manual for WHO Disability Assessment Schedule (WHODAS 2.0). World Health Organization; 2010. 
- American Psychiatric Association. Diagnostic and Statistical Manual of Mental Disorders. 5th ed, text rev. American Psychiatric Association Publishing; 2022. 

<u><b>Voice and Speech Assessments</b></u>
- Jacobson BH, Johnson A, Grywalski C, et al. The Voice Handicap Index (VHI): development and validation. Am J Speech Lang Pathol. 1997;6(3):66-70. doi:10.1044/1058-0360.0603.66 
- Rosen CA, Lee AS, Osborne J, Zullo T, Murry T. Development and validation of the Voice Handicap Index-10. Laryngoscope. 2004;114(9):1549-1556. doi:10.1097/00005537-200409000-00009 
- Kempster GB, Gerratt BR, Verdolini Abbott K, Barkmeier-Kraemer J, Hillman RE. Consensus Auditory-Perceptual Evaluation of Voice: development of a standardized clinical protocol. Am J Speech Lang Pathol. 2009;18(2):124-132. doi:10.1044/1058-0360(2008/08-0017) 

Note: CAPE-V published under CC-BY 4.0 license. Supplemental materials: https://authors.elsevier.com/sd/article/S0892-1997(25)00021-9 
 
<u><b>Respiratory Assessments</b></u>
- Birring SS, Prudon B, Carr AJ, Singh SJ, Morgan MD, Pavord ID. Development of a symptom specific health status measure for patients with chronic cough: Leicester Cough Questionnaire (LCQ). Thorax. 2003;58(4):339-343. doi:10.1136/thorax.58.4.339 
- Mahler DA, Weinberg DH, Wells CK, Feinstein AR. The measurement of dyspnea. Contents, interobserver agreement, and physiologic correlates of two new clinical indexes. Chest. 1984;85(6):751-758. doi:10.1378/chest.85.6.751 
- Miller MR, Hankinson J, Brusasco V, et al. Standardisation of spirometry. Eur Respir J. 2005;26(2):319-338. doi:10.1183/09031936.05.00034805 

<u><b>Cognitive and Language Assessments</b></u>

- Nasreddine ZS, Phillips NA, Bédirian V, et al. The Montreal Cognitive Assessment, MoCA: a brief screening tool for mild cognitive impairment. J Am Geriatr Soc. 2005;53(4):695-699. doi:10.1111/j.1532-5415.2005.53221.x 
- Stroop JR. Studies of interference in serial verbal reactions. J Exp Psychol. 1935;18(6):643-662. doi:10.1037/h0054651 
- Fletcher SG. Time-by-count measurement of diadochokinetic syllable rate. J Speech Hear Res. 1972;15(4):763-770. doi:10.1044/jshr.1504.763 

<b>Picture Description</b>
- Berube S, Hillis AE, Faria AV, et al. Stealing cookies in the twenty-first century: measures of spoken narrative in healthy versus speakers with aphasia. Am J Speech Lang Pathol. 2019;28(1S):404-420. doi:10.1044/2018_AJSLP-17-0131 
- Revised Cookie Theft picture used with permission from Dr. Argye E. Hillis, Johns Hopkins University School of Medicine. Originally published under CC-BY 4.0 license. 

<b>Story Recall</b>
- Systematic Analysis of Language Transcripts (SALT) Software LLC. Frog, Where Are You? Available from: https://www.saltsoftware.com.  

<b>Reading Passages</b>
- IEEE Subcommittee on Subjective Measurements. IEEE recommended practice for speech quality measurements. IEEE Trans Audio Electroacoust. 1969;17(3):225-246. doi:10.1109/TAU.1969.1162058 

### Acknowledgments

<b>Permissions obtained from:</b>
- American Psychiatric Association (DSM-5 diagnostic criteria) 
- Dr. Argye E. Hillis, Johns Hopkins University (Revised Cookie Theft picture) 
- MAPI Research Trust (Voice Handicap Index-10) 
- SALT Software LLC (Frog, Where Are You? story script) 
- World Health Organization (ASRS v1.1, WHODAS 2.0) 
- Open access tools used under CC-BY 4.0 licenses: 
- CAPE-V (Consensus Auditory-Perceptual Evaluation of Voice) 
- Revised Cookie Theft picture description task 
