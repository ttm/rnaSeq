# compute the histograms of the correlations
import pylab as p, numpy as n, pickle

with open('correlation.pickle', 'rb') as f:
    cor = pickle.load(f)

cor_ = cor[n.triu_indices(cor.shape[0], 1)]

p.hist(cor_)
p.savefig('hist_cor_10.png')
p.clf()
p.hist(cor_, bins=100)
p.savefig('hist_cor_100.png')
p.clf()
p.hist(cor_, bins=1000)
p.savefig('hist_cor_1000.png')

p.clf()
p.hist(cor_, normed=True)
p.savefig('hist_cor_10_normed.png')
p.clf()
p.hist(cor_, bins=100, normed=True)
p.savefig('hist_cor_100_normed.png')
p.clf()
p.hist(cor_, bins=1000, normed=True)
p.savefig('hist_cor_1000_normed.png')
