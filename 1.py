# 1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],

# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].

# Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy

# Полученные значения должны быть равны.

# Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков, а затем с использованием функций из библиотек numpy и pandas.

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

plt.scatter(zp, ks) 
plt.xlabel('Величина заработной платы')
plt.ylabel('Поведенческий кредитный скоринг', rotation=90)
plt.show()

# ковариация этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy

cov = np.mean(zp*ks) - np.mean(zp) * np.mean(ks)
print('ковариация двух величин с помощью элементарных действий', cov)

print('Ковариация cov', np.cov(zp, ks, ddof=0)[0, 1])

# коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков

cor_Pirs = cov / (np.std(zp) * np.std(ks))
print('коэффициент корреляции Пирсона с помощью ковариации', cor_Pirs)

cor_Pirs_avrg = cov / (np.std(zp, ddof=0) * np.std(ks, ddof=0))
print('коэффициент корреляции Пирсона с помощью среднеквадратичных отклонений двух признаков, формула', cor_Pirs_avrg) 

print('коэффициент корреляции Пирсона с помощью среднеквадратичных отклонений двух признаков, numpty', np.corrcoef(zp, ks)[0][1])

cor_pandas = pd.Series(zp).corr(pd.Series(ks), method='pearson')
print('коэффициент корреляции Пирсона с помощью среднеквадратичных отклонений двух признаков, pandas', cor_pandas)