# Living Planet Index Data Analysis
## About project
Exploratory data analysis of global biodiversity trends using the Living Planet Index dataset.
Covers data cleaning, time series visualization, regional comparison, smoothing, and correlation analysis. 
 

## Dataset
**Source**: [Living Planet Index](https://ourworldindata.org/grapher/living-planet-index-by-region) - Our World in Data
**Publisher**: WWF / Zoological Society of London
**Description**: Global and regional biodiversity index tracking vertebrate 
  population trends from 1970 to 2020
**License**: Public Domain

## Project Structure
* global-living-planet-index.csv
* living_planet.ipynb
* living_planet.py
* living_planet_index_clean.csv 

## Project Goals
* Data cleaning and type conversion (Year, LPI, confidence intervals)
* Tracking global biodiversity trends from 1970 to 2020
* Comparing LPI across world regions
* Visualizing confidence intervals and uncertainty over time
* Applying data smoothing (rolling average) to reveal long-term trends
* Correlation analysis between LPI and confidence interval bounds
* Building visualizations (line plots, boxplots, barplots, heatmaps)

## Key Findings
**Living Planet Index by Region (1970–2020)**: 
All regions show a consistent decline in the Living Planet Index since 1970. The most critical drop is observed in Latin America and the Caribbean - LPI fell from ~100 to ~6 by 2020, indicating a loss of approximately 94% of animal populations. Africa and freshwater ecosystems also show significant declines (~27 and ~16 respectively). The only exception is Europe and Central Asia - the region showed growth up to ~130 by 1990, followed by a decline reaching ~65 by 2020. North America shows the slowest decline among all regions (~65 by 2020).

**Global LPI Trend (1970–2020)**:
The global Living Planet Index shows a continuous decline from 1970 to 2020 - from the baseline of 100 to ~27, representing a loss of approximately 73% of vertebrate animal populations worldwide over 50 years. The steepest decline occurred between 1970 and 1980. After 2010 the rate of decline slowed but stabilization has not been achieved.

**Distribution of LPI by Region**:
The boxplot reveals significant differences in LPI distribution across regions over the 1970-2020 period. Europe and Central Asia has the highest median LPI (~102) and the widest box (85-112) - reflecting the initial rise and subsequent decline of the index. Latin America and the Caribbean shows the lowest median (~25) with wide spread (10-100) - the greatest overall decline. North America has the narrowest spread (~72-90) - the most stable region. The global (World) indicator has a median of ~50 with wide spread and a long upper whisker, reflecting data heterogeneity across regions.

**Smoothed Global LPI Trend**:
The chart compares the original LPI trend with a smoothed version (5-year rolling average). Both lines nearly overlap throughout the entire observation period - indicating that the original data is already smooth without sharp year-to-year fluctuations. Smoothing confirms the steady and continuous nature of global biodiversity decline from 1970 to 2020 with no temporary recoveries.

**LPI by Region in 2020**:
As of 2020, the highest LPI values are retained in Europe and Central Asia (~65) and North America (~61) - these regions experienced the least biodiversity loss relative to the 1970 baseline. The worst situation is in Latin America and the Caribbean (~6) and freshwater ecosystems (~15) - animal populations in these regions declined most critically. The global (World) indicator stands at ~27, representing a 73% loss of global biodiversity over 50 years.

**Correlation Matrix**:
The correlation matrix shows strong positive relationships between LPI and its confidence bounds - LPI and LPI_lower (r = 0.98), LPI and LPI_upper (r = 0.94). This is an expected result as the upper and lower interval bounds are derived from the main LPI value and change alongside it. This matrix carries no analytical value for identifying external factors affecting biodiversity - additional variables such as temperature, deforestation rates, or CO₂ levels would be needed for deeper analysis.

## Conclusions
Between 1970 and 2020, the global Living Planet Index declined by 73% - from a baseline of 100 to ~27. The most critical losses are observed in Latin America and the Caribbean (~94%) and freshwater ecosystems, while Europe and North America show the smallest declines. However, this dataset contains only index values without data on underlying causes - identifying factors driving biodiversity loss is not possible from the available data alone. Possible contributing factors may include increasing environmental pollution, rising CO₂ emissions, and expanding deforestation. Enriching the dataset with ecological and climate variables would be necessary for a deeper analysis.

## Limitations
* The dataset contains only LPI values without data on underlying causes - identifying factors driving biodiversity loss is not possible from available data alone
* No environmental or climate variables (CO₂ levels, deforestation rates, temperature) - key factors for explaining biodiversity decline
* Correlation matrix is limited to LPI and its confidence bounds - no external variables available for meaningful correlation analysis
* Confidence intervals widen toward 2020 - uncertainty in recent data is growing, limiting the reliability of modern estimates

## Next Steps
* Enrich the dataset with climate and environmental variables (CO₂, deforestation, temperature) to identify drivers of biodiversity loss
* Add species-level or habitat-level data for more granular analysis
* Apply time series forecasting models to predict future LPI trends
* Compare LPI trends with human activity indicators (population growth, land use)

## How to Run
1. Clone the repository
2. Install dependencies:
   pip install pandas numpy seaborn matplotlib
3. Open project.ipynb in Jupyter Notebook and run all cells

## Technologies
![Python](https://img.shields.io/badge/Python-blue)
![pandas](https://img.shields.io/badge/pandas-lightgrey)
![numpy](https://img.shields.io/badge/numpy-blue)
![seaborn](https://img.shields.io/badge/seaborn-teal)
![matplotlib](https://img.shields.io/badge/matplotlib-orange)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)

## Author
[vaslinx] · [GitHub]( https://github.com/vaslinx)

