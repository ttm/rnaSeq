# initial considerations about the greatest absolute values of correlation
import numpy as n, pickle

with open('correlation.pickle', 'rb') as f:
    cor = pickle.load(f)

for i in range(cor.shape[0]):
    cor[i][i] = 0

with open('argsort.pickle', 'rb') as f:
    argsort = pickle.load(f)

def findIndex(num):
    """return the tuple with indexes of the correlation matrix,
    given the argsort number of the flatened array"""
    row = int(num / cor.shape[0])
    col = num % cor.shape[0]
    return [row, col]

def correctIndex(ii):
    ii[0] = ii[0] + (rdm <= ii[0]).sum()
    ii[1] = ii[1] + (rdm <= ii[1]).sum()
    return ii

mins = argsort[:10000000][::2]
maxs = argsort[-10000000:][::-1][::2]

mins_ = []
for i in mins:
    ii = findIndex(i)
    val = cor[ii[0]][ii[1]]
    ii_ = correctIndex(ii[:])
    mins_.append((ii, ii_, val))

maxs_ = []
for i in maxs:
    ii = findIndex(i)
    val = cor[ii[0]][ii[1]]
    ii_ = correctIndex(ii[:])
    maxs_.append((ii, ii_, val))

with open('rows_rdm.pickle', 'rb') as f:
    rdm = n.array(pickle.load(f))

maxs__ = ['apenas com os 4 arquivos com grupo de controle\n\n'] + [str(i)+'\n' for i in maxs_]

with open('correlacoes_max.txt', 'w') as f:
    f.writelines(maxs__)

mins__ = ['apenas com os 4 arquivos com grupo de controle\n\n'] + [str(i)+'\n' for i in mins_]

with open('correlacoes_min.txt', 'w') as f:
    f.writelines(mins__)
