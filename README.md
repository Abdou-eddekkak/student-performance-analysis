# Statistical Analysis of Student Performance

##  Project Overview
This project investigates the impact of socio-economic factors and behavioral habits on student academic performance. Utilizing a hybrid analytical pipeline, the project demonstrates end-to-end data processing, formal hypothesis testing, and publication-quality visualization.

**Author:** Abderahmane Eddekkak  
**Tech Stack:** R Software, IBM SPSS, Python (Pandas, Matplotlib, NumPy)

## Objectives
* To generate and clean a dataset containing academic, demographic, and attendance variables.
* To apply multiple linear regression to identify the strongest predictors of final grades.
* To conduct formal hypothesis testing (T-Tests and ANOVA) to determine the statistical significance of internet access and parental education.
* To visualize key findings using Python.

##  Methodology & Tools
1. **Data Wrangling (Python):** Generated a realistic dataset of 500 students with built-in statistical correlations using `numpy` and `pandas`.
2. **Statistical Modeling (R):** Conducted descriptive statistics, correlation matrices, and built a Multiple Linear Regression model predicting the Final Grade (G3).
3. **Hypothesis Testing (IBM SPSS):** 
   * **Independent Samples T-Test:** Evaluated the impact of home internet access on grades.
   * **One-Way ANOVA:** Analyzed the variance in grades across different levels of mother's education.
4. **Data Visualization (Python):** Developed custom, high-resolution visual evidence using `matplotlib` to support the statistical findings.

## Key Findings
* **The "Absence Penalty":** Regression modeling revealed a strong negative correlation between total days absent and final grades.
* **The Study Time Advantage:** Students categorized in the highest weekly study time bracket consistently outperformed their peers, as shown in the bar chart analysis.
* **Digital Divide:** The independent samples T-Test confirmed a statistically significant difference (p < 0.05) in performance between students with and without home internet access.

##  How to Run the Project
1. Clone the repository: `git clone https://github.com/yourusername/student-performance-analysis.git`
2. The `data/` folder contains the cleaned CSV used for all analyses.
3. Run `DataSet.py` to see the data simulation.
4. Open `R_Commands.txt` to copy commands in RStudio to view the regression outputs.
5. Run `Visualization_Script.py` to regenerate the charts.
