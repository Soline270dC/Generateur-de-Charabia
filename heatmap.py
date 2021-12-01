import numpy as np
import matplotlib.pylab as plb
import seaborn as sns

Mat = np.load('Matrice_probas.npy')
alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

plb.style.use('seaborn')
plb.figure(figsize = (10,10))
heat_map = sns.heatmap(Mat, cmap = 'gnuplot')
plb.show()