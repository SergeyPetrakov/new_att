import numpy as np
import pandas as pd
c = np.matrix([[1, 2], [3, 4]])
a = np.matrix([[1, 2], [4, -1]])
print(np.linalg.eig(c))
print(np.linalg.det(c))
print(np.linalg.inv(a))
