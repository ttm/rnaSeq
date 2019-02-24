# finds correlations and writes to file
import pandas as p, numpy as n, pickle

fnames = [
    'HER+ X CONTROL tudo.xls',
    'LUMINAL A X CONTROLE FINAL total.xls',
    'LUMINAL HER X CONTROL total.xls',
    'TN X CONTROLE total_.xls',
]
def mkMaxMin(fname):
    f1 = p.ExcelFile(fname)
    d1 = f1.parse(f1.sheet_names[0])
    return d1

ds = []
for fname in fnames:
    ds.append(mkMaxMin(fname))
    print(fname)

labs = []
for d in ds:
    labs.append(list(d.iloc[:,2]))

labs_ = n.array(labs)

i = 0
j = 0
rows_dont_match = []
for l in labs_.T:
    if not (l == l[0]).all():
        print(l, i)
        rows_dont_match.append((i+2, l))
        j += 1
    i += 1

data = []
for d in ds:
    data.append(list(d.iloc[:, 3]))

d = n.array(data).T
rdm = [i[0]-2 for i in rows_dont_match]

d_ = n.delete(d, rdm, axis=0)

cor = n.corrcoef(d_)
with open('correlation.pickle', 'wb') as f:
    pickle.dump(cor, f)

