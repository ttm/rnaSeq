# just opens one file and finds max and min values and indexes
import pandas as p, numpy as n

fname = 'HER+ X CONTROL tudo.xls'
f1 = p.ExcelFile(fname)
d1 = f1.parse(f1.sheet_names[0])
vals = n.array(d1.iloc[:,3])
inds = vals.argsort()

mins = inds[:20]
maxs = inds[-20:][::-1]

lines = [
    fname,
    '==> mins',
    mins,
    vals[mins],
    '==> maxs',
    maxs,
    vals[maxs]
]

l = [str(i)+'\n' for i in lines]

with open(fname+'.txt', "w") as f:
    f.writelines(l)


