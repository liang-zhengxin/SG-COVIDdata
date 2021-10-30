# SG-COVIDdata
[![COVID Data Scraper](https://github.com/liang-zhengxin/SG-COVIDdata/actions/workflows/covidscraper.yml/badge.svg?branch=main)](https://github.com/liang-zhengxin/SG-COVIDdata/actions/workflows/covidscraper.yml)

This repository aims to provide machine readable SG COVID Data. Currently there isn't any repository i can find on GitHub the gives me the daily Locally Transmitted Cases in Singapore

This repository contains the following data:

1. [Locally Transmitted Cases](data/dailyLocalCases.json) (1 June 2021 onwards)

2. [Locally Transmitted Cases](data/dailyLocalCases-pre1jun21.json) (5 October 2020 to 30 May 2021)

3. [Vaccination](data/dailyVaxData.json) (28 June 2021 to 27 October 2021)

4. [Vaccination (Percentages)](data/dailyVaxDataPercent.json) (28 October 2021 onwards)


5. [Local Unlinked Cases](data/dailyLocalUnlinkCases.json) (29 June 2021 to 7 September 2021) 


6. [Missing Data](missing-data.json) which contains a list of dates that the data is missing from the repository. *updated manually*

*Note: Unlink cases may become link as contact tracing continues, however this data only tracks the number of unlink cases reported on that day's press release.*

# Quick Glance Dashboard

This data is presented in a simple format on this [website](https://liang-zhengxin.github.io/SG-COVIDdata). It offers an animated progress bar showing Singapore's vaccination progress which tracks the number of fully vaccinated individuals as a percentage of the population.

A [graph](https://liang-zhengxin.github.io/SG-COVIDdata/graph) showing the trend of locally transmitted cases is avaliable.


# Data Source

1. [MOH RSS Feed](https://www.moh.gov.sg/feeds/news-highlights) (Latest Press Release) *updated daily*
 
    * [Locally Transmitted Cases](data/dailyLocalCases.json) (1 June 2021 onwards)

    * [Vaccination](data/dailyVaxData.json) (28 June 2021 onwards)

2. [COVID-19-SG GitHub Repository](https://github.com/alphamodel/COVID-19-SG) (Archived Press Release)

    * [Locally Transmitted Cases](data/dailyLocalCases-pre1jun21.json) (5 October 2020 to 30 May 2021)




As the code assumes that MOH Press Releases follows a certain format, errors may occur if the MOH Press Release deviates from the standard template. Hence there are no guarrantte that the data here is accurate.