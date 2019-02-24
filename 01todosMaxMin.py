# finds max and min values and indexes for all files
import pandas as p, numpy as n

fnames = [
    'HER+ X CONTROL tudo.xls',
    'HER+ X LUMINAL HER tudo.xls',
    'LUMINAL A X CONTROLE FINAL total.xls',
    'LUMINAL HER X CONTROL total.xls',
    'LUMINAL HER X LUMINAL total.xls',
    'TN X CONTROLE total .xls',
    'TN x HER tudo.xls'
]
def mkMaxMin(fname):
    f1 = p.ExcelFile(fname)
    d1 = f1.parse(f1.sheet_names[0])
    if fname != 'TN X CONTROLE total .xls':
        vals = n.array(d1.iloc[:,3])
    else:
        vals = n.array(d1.iloc[:,4])
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
    return d1

ds = []
for fname in fnames:
    ds.append(mkMaxMin(fname))
    print(fname)
