# A/B Test Analysis: Fast Food Marketing Campaign and Cookie Cats Game

## Overview

This repository contains the analysis of two A/B test datasets:
1. Fast Food Marketing Campaign
2. Cookie Cats Game

Each analysis is performed in a separate Jupyter Notebook, where we examine the effectiveness of different strategies to determine the best approach for maximizing sales and player retention.

## Notebooks

### 1. Fast Food Marketing Campaign A/B Test

**Notebook**: [wa_A_B.ipynb](./wa_A_B.ipynb)

#### Goal

The primary goal of this A/B test is to determine which of the three marketing campaigns has the greatest positive impact on sales of a new menu item.

#### Target Metric

The target metric is `SalesInThousands`, representing the weekly sales of the new item in thousands of dollars for each store location, promotion, and week.

#### Key Findings

- **Pairwise t-tests with Bonferroni correction**: Determined the statistical significance of differences in sales across different promotions.
- **Confidence Intervals**: Calculated both analytically and using bootstrap methods to validate the results.
- **Treatment Effect**: Compared the sales performance across different promotions.

### 2. Cookie Cats Game A/B Test

**Notebook**: [cookie_A_B.ipynb](./cookie_A_B.ipynb)

#### Goal

The goal is to evaluate the impact of moving the first gate in the game from level 30 to level 40 on player retention and engagement.

#### Target Metric

The target metrics are:
- `retention_1`: Player retention one day after installation.
- `retention_7`: Player retention seven days after installation.
- `sum_gamerounds`: Total number of game rounds played within the first 14 days.

#### Key Findings

- **1-Day Retention Analysis**: No significant difference in retention rates between gate_30 and gate_40.
- **7-Day Retention Analysis**: Significant difference in retention rates, with gate_40 showing lower retention.
- **Total Game Rounds Analysis**: No significant difference in the total number of game rounds played between gate_30 and gate_40.

## Dashboard

You can view the interactive dashboard for the analyses in Looker Studio [here](https://lookerstudio.google.com/s/sP20Xu7x9xQ).

## Conclusion

Based on the analyses, we provide recommendations for the best marketing strategy in the Fast Food Marketing Campaign and the optimal gate placement in the Cookie Cats game to maximize player retention and engagement.
