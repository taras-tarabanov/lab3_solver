import numpy as np
import sys
sys.stdout = open("output.txt", "w", encoding="utf-8")


##################################INPUT
tsiferkiX =np.array([9.7, 7.4, 18.5, 11.5, 8, 2.1, 16.8, 8.4, 6.8, 1.8])
tsiferkiY =np.array([2.7, 7.7, 2.2, 4.2, 8.3, 5.9, 1.6, 5.9, 6.6, 9])

#tsiferkiX = np.array([3.5, 7.1, 19.9, 10.3, 12.9, 15.0, 4.1, 3.0, 9.1, 8.7])
#tsiferkiY = np.array([1.7, 4.0, 8.2, 5.3, 6.8, 7.4, 0.8, 1.4, 3.4, 5.8])
##################################INPUT
x_ = round(np.mean(tsiferkiX),2)
#\widetilde{S}
print(fr"\begin{{align}}")
print(r"r &= \frac{\mu_{1,1}}{\widetilde{S}_x\widetilde{S}_y}\\")
x_bar = round(np.mean(tsiferkiX),2)
n = len(tsiferkiX)
sum_tsiferkiX = np.sum(tsiferkiX)

formatted_string = fr"\bar{{x}} &= \frac{{1}}{{{n}}} \left( {' + '.join(map(str, tsiferkiX))} \right) = {sum_tsiferkiX/n:.2f}\\"
print(formatted_string)

y_bar = round(np.mean(tsiferkiY),2)
sum_tsiferkiY = np.sum(tsiferkiY)
formatted_string = fr"\bar{{y}} &= \frac{{1}}{{{n}}} \left( {' + '.join(map(str, tsiferkiY))} \right) = {sum_tsiferkiY/n:.2f}\\"
print(formatted_string)

# Calculation of sample covariance
mu_11 = round(sum((tsiferkiX - x_bar) * (tsiferkiY - y_bar)) / n, 2)
formatted_string = fr"\widetilde{{\mu}}_{{1.1}} &= \frac{{1}}{{{n}}} \left( {' + '.join([f'({x} - {x_bar})({y} - {y_bar})' for x, y in zip(tsiferkiX, tsiferkiY)])} \right) = {mu_11:.2f}\\"
print(formatted_string)

# Calculation of sample variances
S_x_squared = round(sum((tsiferkiX - x_bar)**2) / n, 2)
formatted_string = fr"\tilde{{S}}_x^2 &= \frac{{1}}{{{n}}} \left( {' + '.join([f'({x} - {x_bar})^2' for x in tsiferkiX])} \right) = {S_x_squared:.2f}\\"
print(formatted_string)

S_y_squared = round(sum((tsiferkiY - y_bar)**2) / n, 2)
formatted_string = fr"\tilde{{S}}_y^2 &= \frac{{1}}{{{n}}} \left( {' + '.join([f'({y} - {y_bar})^2' for y in tsiferkiY])} \right) = {S_y_squared:.2f}\\"
print(formatted_string)

# Calculation of sample correlation coefficient
r = round(mu_11 / (np.sqrt(S_x_squared) * np.sqrt(S_y_squared)), 2)
print(fr"r &= {r:.2f}\\")

# Hypothesis testing for significance of correlation coefficient
from scipy.stats import t

t_stat = r * np.sqrt(n - 2) / np.sqrt(1 - r**2)
t_crit = t.ppf(0.995, n - 2)  # For a two-tailed test at 0.01 significance level
print(r"H_0: r &= 0\\")
print(r"H_1: r \neq 0\\")
print(fr"K_{{\text{{cnoc}}}} &= \frac{{r\sqrt{{n - 2}}}}{{\sqrt{{1 - r^2}}}} = \frac{{{r:.2f}\sqrt{{{n - 2}}}}}{{\sqrt{{1 - {r:.2f}^2}}}} = {t_stat:.2f}\\")
print(fr"K_{{\text{{kp}}}} &= t_{{0.05}}({n-2}) = {t_crit:.2f}\\")

if abs(t_stat) > t_crit:
    print(fr"&Перевіряємо~нерівність |{t_stat:.2f}| > {t_crit:.2f}.\\")
    print(fr"&Нерівність~перетворюється~на~істину.~Отже,~гіпотеза~H_0~відкидається,~тобто\\")
    print(fr"&приймається~припущення~про~значущість~відмінності~від~нуля~отриманого~у~п.~a)\\")
    print(fr"&коефіцієнта~кореляції.~Тобто~на~підставі~наявних~експериментальних~даних~можна\\")
    print(fr"&прийняти~припущення~про~лінійний~кореляційний~зв'язок~між~ознаками~X~та~Y.\\")
else:
    print(fr"&Перевіряємо~нерівність~|{t_stat:.2f}| > {t_crit:.2f}.\\")
    print(fr"&Нерівність~хибна,~то~в~цьому~випадку~робиться~висновок~про~те,~що\\")
    print(fr"&коефіцієнт~кореляції~випадковим~чином~не~дорівнює~нулю~і,~отже,~відсутні~підстави\\")
    print(fr"&припускати~наявність~лінійного~кореляційного~зв'язку~між~ознаками~X~і~Y.\\")
if abs(t_stat) > t_crit:
    print(fr"&The~hypothesis~H0: r = 0~is~rejected.~The~correlation~coefficient~is~significant.\\")
else:
    print(fr"&The~hypothesis~H0: r = 0~cannot~be~rejected.~The~correlation~coefficient~is~not~significant.\\")

import matplotlib.pyplot as plt



# Linear regression
b_yx = round(mu_11 / S_x_squared,2)
a_yx = round(y_bar - b_yx * x_bar,2)
x_range = np.linspace(min(tsiferkiX), max(tsiferkiX), 100)
y_reg = a_yx + b_yx * x_range

print(fr"&d)~У~припущенні,~що~між~ознаками~X~та~Y~існує~лінійна~залежність,~отримати~оцінку~коефіцієнта~регресії~Y~по~X.\\")
print(fr"b_{{yx}} &= \frac{{\tilde{{\mu}}_{1,1}}}{{\tilde{{S}}_x^2}} = \frac{{{mu_11:.2f}}}{{{S_x_squared:.2f}}} = {b_yx:.2f}\\")

print(fr"&Виразити~аналітично~рівняння~лінійної~регресії~Y~по~X.\\")
print(fr"y_x &= b_{{yx}}x + \left( \bar{{y}} - b_{{yx}}\bar{{x}} \right) = {b_yx:.2f}x + \left( {y_bar:.2f} - {b_yx:.2f}\cdot{x_bar:.2f} \right) = {b_yx:.2f}x - {y_bar - b_yx * x_bar:.2f}\\")
print(fr"\end{{align}}")
# Plot with regression line

sys.stdout.close()
# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(tsiferkiX, tsiferkiY)
plt.xlabel("Ознака X")
plt.ylabel("Ознака Y")
plt.title("Діаграма розсіювання")
plt.show()


plt.figure(figsize=(8, 6))
plt.scatter(tsiferkiX, tsiferkiY)
plt.plot(x_range, y_reg, 'r', label='Лінія регресії Y по X')
plt.xlabel("Ознака X")
plt.ylabel("Ознака Y")
plt.title("Діаграма розсіювання")
plt.legend()
plt.show()
