import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Завдання 1
df = pd.read_excel('Результати обчислень.xlsx')
df = df.drop(columns=['Unnamed: 0'])

E  = 'Енергія фотона, еВ'
A  = 'Показник поглинання'
I2 = 'Товстий зразок, усереднена інтенсивність пройденого сигналу I2 без шумів, мВ'
I1 = 'Тонкий зразок, усереднена інтенсивність пройденого сигналу I1 без шумів, мВ'

# Завдання 2
df_linear = df[(df[E] >= 2.24) & (df[E] <= 2.28)]

# Завдання 3
res = sm.OLS(df_linear[A], sm.add_constant(df_linear[E])).fit()
C1 = res.params[E]
C2 = res.params['const']

# Завдання 4
E0 = -C2 / C1

idxmin = df[A].idxmin()
min_a = df.loc[idxmin][A]
min_e = df.loc[idxmin][E]

# Завдання 5
deltaE = abs(E0 - min_e)
print(f'delta E = { round(deltaE, 3) }')

plt.plot(df[E], df[A])
plt.xlabel(E)
plt.ylabel(A)
plt.plot(min_e, min_a, 'ro')
plt.text(2.24, -50, f'{ min_e } еВ')
plt.title('Спектр поглинання GaP')

# Завдання 6
plt.text(2.17, 1800, '\n'.join(
    [ f'$\\alpha$ = { round(C1) } * E - { round(abs(C2)) }'
    , f'E = { round(E0, 3) } еВ'
    , f'$\Delta$E = { round(deltaE, 3) } еВ'
    ]))

plt.savefig('Графік.png')
