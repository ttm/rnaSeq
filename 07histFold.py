# compute the histograms of the correlations
import pylab as p, pandas as pd, numpy as n, pickle

# make hist for each xls and for all of them together
fnames = [
    'HER+ X CONTROL tudo.xls',
    'HER+ X LUMINAL HER tudo.xls',
    'LUMINAL A X CONTROLE FINAL total.xls',
    'LUMINAL HER X CONTROL total.xls',
    'LUMINAL HER X LUMINAL total.xls',
    'TN X CONTROLE total_.xls',
    'TN x HER tudo.xls'
]

def mkHistFold(fname, bins):
    f1 = pd.ExcelFile(fname)
    d1 = f1.parse(f1.sheet_names[0])
    vals = n.array(d1.iloc[:,3])

    p.clf()
    p.hist(vals, bins=bins)
    p.savefig('%s_hist_fold_%d.png' % (fname, bins))
    p.clf()
    p.hist(vals, bins=bins, normed=True)
    p.savefig('%s_hist_fold_%d_normed.png' % (fname, bins))

for fname in fnames:
    mkHistFold(fname, 10)
    mkHistFold(fname, 100)
    mkHistFold(fname, 1000)
    print(fname)
