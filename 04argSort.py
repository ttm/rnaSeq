# find indexes of the ordered correlation values
import numpy as n, pickle

with open('correlation.pickle', 'rb') as f:
    cor = pickle.load(f)

for i in range(cor.shape[0]):
    cor[i][i] = 0

argsort = n.argsort(cor, None)

print('argsort')
with open('argsort.pickle', 'wb') as f:
    pickle.dump(argsort, f)

