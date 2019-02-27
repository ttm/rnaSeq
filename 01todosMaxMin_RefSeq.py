# finds max and min values and indexes for all files
import pandas as p, numpy as n

fnames = [
    'HER+ X CONTROL tudo.xls',
    'HER+ X LUMINAL HER tudo.xls',
    'LUMINAL A X CONTROLE FINAL total.xls',
    'LUMINAL HER X CONTROL total.xls',
    'LUMINAL HER X LUMINAL total.xls',
    'TN X CONTROLE total_.xls',
    'TN x HER tudo.xls'
]
def mkMaxMin(fname):
    f1 = p.ExcelFile(fname)
    d1 = f1.parse(f1.sheet_names[0])
    vals = n.array(d1.iloc[:,3])
    inds = vals.argsort()
    refseqs = n.array(d1.iloc[:,2])

    mins = inds[:20]
    maxs = inds[-20:][::-1]

    lines = [
        fname,
        '==> mins',
        refseqs[mins],
        vals[mins],
        '==> maxs',
        refseqs[maxs],
        vals[maxs]
    ]

    l = [str(i)+'\n' for i in lines]

    with open(fname+'_RefSeq.txt', "w") as f:
        f.writelines(l)
    return d1

ds = []
for fname in fnames:
    ds.append(mkMaxMin(fname))
    print(fname)
