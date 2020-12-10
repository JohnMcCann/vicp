# Vaccine Injury Compensation Program (vicp)

The [National Vaccine Injury Compensation Program](https://www.hrsa.gov/vaccine-compensation/index.html) is a national fund that awards compensation to those who have been "injured by a VICP-covered vaccine." This project is for analyzing their [monthly report](https://www.hrsa.gov/sites/default/files/hrsa/vaccine-compensation/data/data-statistics-report.pdf).

A non-standard library is required, [tabula-py](https://tabula-py.readthedocs.io/en/latest/), for reading tables off the report (pdf).

## images

#### Inferred adverse rate of vaccines

This bar chart shows an inferred adverse incident rate for each vaccine. The bounds on the rates are arguable, as not all adverse incidents suffered from a vaccine will be process by the vicp, and on the other hand not all petitions have merit. Regardless, these rates should be representative of the rate of adverse effects for each vaccine.

*Deaths and Injuries are estimated from the larger 1988-2020 petition data, as the 2006-2020 data is not avaiable at a granular level. Total petition rate is still accurate, but breakdown between injury and death are subject to their stability between the two periods.

<img src="https://github.com/JohnMcCann/vicp/wiki/images/adverse_rate.png" alt="Vaccine Adverse Petition Rate per Dose" width="100%"/>

#### Average awards and fees relating to a petition found to have merit.

<p align="center">
<img src="https://github.com/JohnMcCann/vicp/wiki/images/victim_compensation.png" alt="Vaccine Adverse Petition Rate per Dose" width="49%"/><img src="https://github.com/JohnMcCann/vicp/wiki/images/legal_fees.png" alt="Benford confidence bounds for 1Mx1M log-normal distribution" width="47.3%"/>
</p>
