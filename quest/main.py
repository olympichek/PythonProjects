import numpy as np
import matplotlib.pyplot as plt
from functions import *

data_tuple = \
    ( read_data('Time 0.txt')
    , read_data('Time 21 hours.txt')
    , read_data('Time 48 hours.txt')
    )

print(tuple(map(len, data_tuple)))

data_tuple = tuple(map(clean_data, data_tuple))

print(tuple(map(len, data_tuple)))

step1, step2, step3 = map(get_step, data_tuple)
if not check_wavestep(step1, step2, step3):
    max_step = max(step1, step2, step3)
    data_tuple = tuple(map(normalize_wavestep(max_step), data_tuple))

print(tuple(map(len, data_tuple)))


for data, i in zip(data_tuple, range(len(data_tuple))):
    data_np = np.array(data)
    plt.plot(data_np[:, 0], data_np[:, 1], label='data ' + str(i + 1))
plt.grid(axis='both')
plt.legend()
plt.show()
