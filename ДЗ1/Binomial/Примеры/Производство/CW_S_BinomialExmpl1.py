import pandas as pd
import math

binrow = []
for x in range(88):
    num = (((math.factorial(87))/(math.factorial(x) * math.factorial((87 - x)))) * (0.6 ** x) * (0.4 ** (87 - x)))
    resnum = f'{num:.15f}'
    binrow.append(resnum)

# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)

# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)

dict = {'Pi':binrow}
table = pd.DataFrame(data=dict)
print(table)