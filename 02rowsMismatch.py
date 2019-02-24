# finds rows in which RefSeq does not match
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

lines = ["%d => %s\n" % i for i in rows_dont_match]
lines = [' || '.join(fnames)+'\n\n', str(j) + ' rows dont match!\n\n'] + lines
with open('rows_mismatch.txt', 'w') as f:
    f.writelines(lines)



