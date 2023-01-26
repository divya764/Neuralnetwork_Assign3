import numpy as np
a = np.random.uniform(1,20,20)
print(a)
r = np.reshape(a, (4,5))
max_index = np.argmax(r, axis = 1)
r[np.arange(len(max_index)), max_index] = 0
print(r)
