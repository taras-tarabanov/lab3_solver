# lab3_solver
# Correlation and Linear Regression Analysis

This repository contains a Python script for performing correlation and linear regression analysis on two sets of data points. The code calculates the correlation coefficient, performs hypothesis testing, and fits a linear regression model to the data. The results are output in LaTeX format for easy integration into reports.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Example Output](#example-output)
4. [Interpretation of Results](#interpretation-of-results)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Install the required packages:**
    ```sh
    pip install numpy scipy matplotlib
    ```

## Usage

1. **Modify the input data:**
    Edit the `tsiferkiX` and `tsiferkiY` arrays with your data points.

    ```python
    tsiferkiX = np.array([9.7, 7.4, 18.5, 11.5, 8, 2.1, 16.8, 8.4, 6.8, 1.8])
    tsiferkiY = np.array([2.7, 7.7, 2.2, 4.2, 8.3, 5.9, 1.6, 5.9, 6.6, 9])
    ```

2. **Run the script:**
    ```sh
    python correlation_analysis.py
    ```

3. **View the results:**
    The output will be saved to `output.txt` in LaTeX format, and two scatter plots will be displayed—one with the data points and another with the linear regression line.

## Example Output

The script produces LaTeX formatted output for the correlation coefficient, hypothesis testing, and the linear regression equation.

Example output:
```latex
\begin{align}
r &= \frac{\mu_{1,1}}{\widetilde{S}_x\widetilde{S}_y}\\
\bar{x} &= \frac{1}{10} \left( 9.7 + 7.4 + 18.5 + 11.5 + 8 + 2.1 + 16.8 + 8.4 + 6.8 + 1.8 \right) = 9.30\\
\bar{y} &= \frac{1}{10} \left( 2.7 + 7.7 + 2.2 + 4.2 + 8.3 + 5.9 + 1.6 + 5.9 + 6.6 + 9 \right) = 5.41\\
\widetilde{\mu}_{1,1} &= \frac{1}{10} \left( (9.7 - 9.3)(2.7 - 5.4) + ... + (1.8 - 9.3)(9 - 5.4) \right) = -6.08\\
\tilde{S}_x^2 &= \frac{1}{10} \left( (9.7 - 9.3)^2 + ... + (1.8 - 9.3)^2 \right) = 26.56\\
\tilde{S}_y^2 &= \frac{1}{10} \left( (2.7 - 5.4)^2 + ... + (9 - 5.4)^2 \right) = 6.64\\
r &= -0.45\\
H_0: r &= 0\\
H_1: r \neq 0\\
K_{\text{cnoc}} &= \frac{r\sqrt{n - 2}}{\sqrt{1 - r^2}} = \frac{-0.45\sqrt{8}}{\sqrt{1 - (-0.45)^2}} = -1.42\\
K_{\text{kp}} &= t_{0.05}(8) = 2.90\\
&The~hypothesis~H0: r = 0~cannot~be~rejected.~The~correlation~coefficient~is~not~significant.\\
b_{yx} &= \frac{\tilde{\mu}_{1,1}}{\tilde{S}_x^2} = \frac{-6.08}{26.56} = -0.23\\
y_x &= b_{yx}x + \left( \bar{y} - b_{yx}\bar{x} \right) = -0.23x + \left( 5.41 - (-0.23)\cdot{9.30} \right) = -0.23x + 7.55\\
\end{align}
