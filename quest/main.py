import numpy as np
import matplotlib.pyplot as plt
from functions import *

data_tuple = tuple(map(read_data, 
    ( 'Time 0.txt'
    , 'Time 21 hours.txt'
    , 'Time 48 hours.txt'
#   , '181213_A1.sca'
    )))

print(tuple(map(len, data_tuple)))

data_tuple = tuple(map(clean_data, data_tuple))

print(tuple(map(len, data_tuple)))

steps = tuple(map(get_step, data_tuple))
if not check_wavestep(steps):
    max_step = max(steps)
    data_tuple = tuple(map(normalize_wavestep(max_step), data_tuple))

print(tuple(map(len, data_tuple)))

for data, i in zip(data_tuple, range(len(data_tuple))):
    data_np = np.array(data)
    plt.plot(data_np[:, 0], data_np[:, 1], label='data ' + str(i + 1))
plt.grid(axis='both')
plt.legend()
plt.show()
