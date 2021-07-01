# SG-COVIDdata

This repository aims to provide machine readable SG COVID Data. Currently there isn't any repository i can find on GitHub the gives me the daily Locally Transmitted Cases in Singapore

This repository contains the following data

1. [Locally Transmitted Cases](data/dailyLocalCases.json) (1 June 2021 onwards)

2. [Locally Transmitted Cases](data/pre1jun21.json) (5 October 2020 to 1 June 2021)

3. [Missing Data](missing-data.json) which contains a list of dates that the data is missing from the repository. Updated manually.


# Data Source

1. [MOH RSS Feed](https://www.moh.gov.sg/feeds/news-highlights) 

2. [COVID-19-SG GitHub Repository](https://github.com/alphamodel/COVID-19-SG)


Data in [dailyLocalCases.json](data/dailyLocalCases.json) are scraped from MOH RSS Feed that provides that latest press release.
Data in [pre1jun21.json](data/pre1jun21.json) are scraped from the GitHub Repository that stored past moh press releases. 

As the code assumes that MOH Press Releases follows a certain format, errors may occur if the MOH Press Release deviates from the standard template. Hence there are no guarrantte that the data here is accurate.