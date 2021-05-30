import pandas as pd
import numpy as np
from scipy.constants import Planck as h, c, e
import matplotlib.pyplot as plt

# Завдання 1
df = pd.read_excel('Завдання Pandas.xlsx')

x2 = df.loc[0]['Товстий зразок, товщина х2, мм']
x1 = df.loc[0]['Тонкий зразок, товщина х1, мм']
noise = df.loc[0]['Рівень шумів, мВ']
df = df.drop(columns=df.columns[-3:])

# Завдання 2
df = df.drop(columns=['Поділка на барабані'])

L  = 'Довжина хвилі'
E  = 'Енергія фотона, еВ'
A  = 'Показник поглинання'
I2 = 'Товстий зразок, усереднена інтенсивність пройденого сигналу I2 без шумів, мВ'
I1 = 'Тонкий зразок, усереднена інтенсивність пройденого сигналу I1 без шумів, мВ'

# Завдання 3
df[L] = round(h * c / (df[L] * 1e-9 * e), 3)
df = df.rename(columns={L: E})

# Завдання 4
df[I2] = df[df.columns[1:5]].sum(axis=1) / 4 - noise
df[I1] = df[df.columns[5:9]].sum(axis=1) / 4 - noise
df = df.drop(columns=df.columns[1:9])

# Завдання 5
absorption = np.log(df[I1] / df[I2]) / (x2 - x1)
df[A] = round(absorption * 1e3, 1)

# Завдання 6
plt.plot(df[E], df[A])
plt.xlabel(E)
plt.ylabel(A)

# Завдання 7
idxmin = df[A].idxmin()
min_a = df.loc[idxmin][A]
min_e = df.loc[idxmin][E]
plt.plot(min_e, min_a, 'ro')
plt.text(2.24, -50, f'{ min_e } еВ')

# Завдання 8
# Енергія фотона, що відповідає мінімальному показнику поглинання: 2.237 еВ
# Згідно з таблицею, це відповідає ширині забороненої зони напівпровідника GaP
plt.title('Спектр поглинання GaP')

# Завдання 9
plt.savefig('Графік.png')
df.to_excel('Результати обчислень.xlsx')  
