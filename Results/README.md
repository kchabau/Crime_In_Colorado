# Dataset Findings & Discussion

## Age Group Analysis of Arrestees

Initial exploration of the dataset, focusing on the `age_num` column, revealed a wide age range among reported individuals—from as young as 1 year old to as old as 99. This unusual spread prompted further segmentation into defined age categories for more interpretable analysis. The defined `age_group` classifications are as follows:

- **Adolescent**: ≤ 15 years  
- **Young Adult**: 16–24 years  
- **Middle Aged Adult**: 25–39 years  
- **Adult**: 40–59 years  
- **Senior**: 60+ years

> **Note:** To address missing values in age and other columns, multiple imputations were performed using the `IterativeImputer` from **scikit-learn**, ensuring robust and statistically sound data recovery.

### Key Age-Based Insights:
- **Middle Aged Adults** accounted for **70.77%** of all offenses, representing the most involved demographic group in this dataset.
- **Young Adults** followed with **13.09%**, while **Adolescents** and **Seniors** contributed the least to crime totals (**3.12%** and **1.57%**, respectively).

These trends suggest that individuals in the 25–39 age range are significantly more active in reported offenses, potentially due to higher exposure to urban environments and socio-economic stressors.

---

## Top Offense Types (2016–2023)

An aggregated count of offense types over the period of 2016 to 2023 shows the most frequently reported crimes:

1. **Theft From Motor Vehicle** – 211,606 reports  
2. **Shoplifting** – 184,410 reports  
3. **Drug/Narcotic Violations** – 177,380 reports  
4. **Burglary/Breaking & Entering** – 174,015 reports  
5. **Aggravated Assault** – 113,418 reports  

These findings highlight property crimes and drug-related offenses as persistent areas of concern across Colorado.

![picture3](/Assets/tableau_screenshot_3.png)

---

## Top 5 Cities by Reported Crimes

The cities with the highest number of reported offenses include:

1. **Denver** – 437,383 reports  
2. **Colorado Springs** – 284,293 reports  
3. **Aurora** – 243,694 reports  
4. **Lakewood** – 128,775 reports  
5. **Pueblo** – 111,370 reports  

These figures correlate with urban population density. As of recent estimates, Colorado's population has been increasing by approximately **0.73% annually** (MacroTrends, 2021–2024). Growing populations, particularly in metropolitan areas, tend to elevate the risk and frequency of crime. Stakeholders should consider urban planning and community investment initiatives to address these rising risks.

---

## Year-over-Year Crime Trends (2016–2023)

| year | offense_category_name | num_of_reports | ranking |
| ---- | --------------------- | -------------- | ------- |
| 2016 | Larceny/Theft Offenses | 109596 | 1 |
| 2016 | Assault Offenses | 46713 | 2 |
| 2016 | Destruction/Damage/Vandalism of Property | 42733 | 3 |
| 2016 | Drug/Narcotic Offenses | 37327 | 4 |
| 2016 | Fraud Offenses | 23935 | 5 |
| 2017 | Larceny/Theft Offenses | 108838 | 1 |
| 2017 | Assault Offenses | 49346 | 2 |
| 2017 | Destruction/Damage/Vandalism of Property | 42693 | 3 |
| 2017 | Drug/Narcotic Offenses | 40999 | 4 |
| 2017 | Fraud Offenses | 24405 | 5 |
| 2018 | Larceny/Theft Offenses | 110158 | 1 |
| 2018 | Assault Offenses | 51202 | 2 |
| 2018 | Drug/Narcotic Offenses | 42435 | 3 |
| 2018 | Destruction/Damage/Vandalism of Property | 40953 | 4 |
| 2018 | Fraud Offenses | 25616 | 5 |
| 2019 | Larceny/Theft Offenses | 101786 | 1 |
| 2019 | Assault Offenses | 47782 | 2 |
| 2019 | Destruction/Damage/Vandalism of Property | 37676 | 3 |
| 2019 | Drug/Narcotic Offenses | 37652 | 4 |
| 2019 | Fraud Offenses | 24210 | 5 |
| 2020 | Larceny/Theft Offenses | 108447 | 1 |
| 2020 | Assault Offenses | 51830 | 2 |
| 2020 | Destruction/Damage/Vandalism of Property | 47003 | 3 |
| 2020 | Fraud Offenses | 28313 | 4 |
| 2020 | Motor Vehicle Theft | 27900 | 5 |
| 2021 | Larceny/Theft Offenses | 112851 | 1 |
| 2021 | Assault Offenses | 56335 | 2 |
| 2021 | Destruction/Damage/Vandalism of Property | 52395 | 3 |
| 2021 | Motor Vehicle Theft | 35058 | 4 |
| 2021 | Fraud Offenses | 33699 | 5 |
| 2022 | Larceny/Theft Offenses | 112257 | 1 |
| 2022 | Assault Offenses | 57399 | 2 |
| 2022 | Destruction/Damage/Vandalism of Property | 54484 | 3 |
| 2022 | Motor Vehicle Theft | 37321 | 4 |
| 2022 | Drug/Narcotic Offenses | 32816 | 5 |
| 2023 | Larceny/Theft Offenses | 107143 | 1 |
| 2023 | Assault Offenses | 57879 | 2 |
| 2023 | Destruction/Damage/Vandalism of Property | 50157 | 3 |
| 2023 | Drug/Narcotic Offenses | 36392 | 4 |
| 2023 | Motor Vehicle Theft | 31911 | 5 |

**Larceny/Theft** has consistently ranked as the most reported offense across all years. This pattern reinforces the need for targeted prevention strategies such as improved neighborhood watch programs, better lighting, and enhanced vehicle security technologies.

---

## Crime Patterns by Age Group and Offense

### Age Category to Offense Type Distribution:

| offense_name | age_group | count | % of Incident Reports (per age_group and offense_name) |
| ------------ | --------- | ----- | ------------------------------------------------------ |
| Destruction/Damage/Vandalism of Property | Middle Age Adult | 288460 | 78.37 |
| All Other Larceny | Middle Age Adult | 243505 | 83.04 |
| Theft From Motor Vehicle | Middle Age Adult | 196846 | 93.02 |
| Motor Vehicle Theft | Middle Age Adult | 183313 | 85.30 |
| Burglary/Breaking & Entering | Middle Age Adult | 143283 | 82.34 |
| Simple Assault | Middle Age Adult | 124078 | 46.82 |
| Shoplifting | Middle Age Adult | 105924 | 57.53 |
| Theft of Motor Vehicle Parts or Accessories | Middle Age Adult | 93413 | 97.42 |
| Drug/Narcotic Violations | Middle Age Adult | 82246 | 46.37 |
| Aggravated Assault | Middle Age Adult | 62055 | 54.71 |
| Theft From Building | Middle Age Adult | 61868 | 77.92 |
| Simple Assault | Adult | 57974 | 21.87 |
| Identity Theft | Middle Age Adult | 53121 | 88.75 |
| Simple Assault | Young Adult | 52450 | 19.79 |
| Drug Equipment Violations | Middle Age Adult | 50128 | 47.26 |
| Drug/Narcotic Violations | Young Adult | 44816 | 25.27 |
| False Pretenses/Swindle/Confidence Game | Middle Age Adult | 43983 | 78.97 |
| Destruction/Damage/Vandalism of Property | Young Adult | 38098 | 10.35 |
| Credit Card/Automated Teller Machine Fraud | Middle Age Adult | 37591 | 85.22 |
| Drug/Narcotic Violations | Adult | 37565 | 21.18 |
| Shoplifting | Young Adult | 36989 | 20.09 |
| Weapon Law Violations | Middle Age Adult | 34477 | 56.91 |
| Shoplifting | Adult | 31079 | 16.88 |
| Impersonation | Middle Age Adult | 29778 | 75.77 |
| Counterfeiting/Forgery | Middle Age Adult | 27851 | 71.64 |
| Destruction/Damage/Vandalism of Property | Adult | 26768 | 7.27 |
| Drug Equipment Violations | Young Adult | 25738 | 24.27 |
| Robbery | Middle Age Adult | 24661 | 62.74 |
| Drug Equipment Violations | Adult | 23497 | 22.15 |
| Aggravated Assault | Young Adult | 22553 | 19.88 |
| All Other Larceny | Adult | 21759 | 7.42 |
| Aggravated Assault | Adult | 21252 | 18.74 |
| All Other Larceny | Young Adult | 20225 | 6.90 |
| Intimidation | Middle Age Adult | 19645 | 49.06 |
| Simple Assault | Adolescent | 18080 | 6.82 |
| Stolen Property Offenses | Middle Age Adult | 17692 | 59.64 |
| Motor Vehicle Theft | Young Adult | 17415 | 8.10 |
| Burglary/Breaking & Entering | Young Adult | 15083 | 8.67 |
| Weapon Law Violations | Young Adult | 14064 | 23.21 |
| Simple Assault | Senior | 12446 | 4.70 |
| Burglary/Breaking & Entering | Adult | 11416 | 6.56 |
| Destruction/Damage/Vandalism of Property | Adolescent | 11413 | 3.10 |
| Motor Vehicle Theft | Adult | 10377 | 4.83 |
| Intimidation | Adult | 10280 | 25.67 |
| Rape | Middle Age Adult | 10160 | 49.44 |
| Robbery | Young Adult | 9818 | 24.98 |
| Kidnapping/Abduction | Middle Age Adult | 9784 | 54.27 |
| Drug/Narcotic Violations | Adolescent | 9723 | 5.48 |
| Theft From Motor Vehicle | Young Adult | 9646 | 4.56 |
| Weapon Law Violations | Adult | 8190 | 13.52 |
| Theft From Building | Young Adult | 7483 | 9.42 |
| Theft From Building | Adult | 7142 | 8.99 |
| Shoplifting | Adolescent | 6967 | 3.78 |
| Arson | Middle Age Adult | 6484 | 66.78 |
| Intimidation | Young Adult | 6171 | 15.41 |
| False Pretenses/Swindle/Confidence Game | Adult | 6049 | 10.86 |
| Stolen Property Offenses | Young Adult | 5695 | 19.20 |

> Shortened for brevity. To see your own results, clone this repo and run the ETL code after setting up your cursor and connection to your MySQL server

A detailed matrix linking `offense_name` with `age_group` shows that **Middle Aged Adults** consistently represent the highest proportion across most crime categories—ranging from property crimes to narcotics and fraud. For example:

- **93.02%** of "Theft From Motor Vehicle" reports involved Middle Aged Adults  
- **88.75%** of "Identity Theft" reports also fell within the same group  
- In contrast, **Adolescents** and **Seniors** had minimal involvement across most offenses  

These insights can inform policy-making and age-targeted interventions, such as job programs, addiction support services, or youth engagement initiatives.

> **Note:** For the full offense-to-age-group matrix, please see the extended CSV documentation in the `/data/exports` directory.

---

## Temporal Trends in Crime Activity

![tableau_screenshot_2](/Assets/tableau_screenshot_2.png)

Time-series and time-of-day exploration revealed:

- **Higher crime rates during summer months** (June–August), suggesting a potential link to seasonal activities and outdoor exposure.
- **Weekends**, particularly **Friday and Saturday evenings**, saw elevated assault-related reports.
- **Drug-related offenses** exhibited dual peaks—once in the **midday** and again in the **late evening**, with city-specific variations.

These temporal trends offer actionable insights for law enforcement scheduling, public safety alerts, and preventive community measures.

---

## Further Analysis

For additional exploration into age-specific crime distributions by county and interactive dashboards, refer to the project repository’s documentation and visual assets.

> To replicate or extend this analysis, clone the repository and run the ETL pipeline, ensuring your database connection is properly configured in the script.

