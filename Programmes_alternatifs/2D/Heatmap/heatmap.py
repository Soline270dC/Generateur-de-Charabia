import numpy as np
import matplotlib.pylab as plb
import seaborn as sns

Mat = np.load('Matrice_probas_3D_Miserables.npy')
alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

plb.style.use('seaborn')
plb.figure(figsize = (10,10))
heat_map = sns.heatmap(Mat[28], cmap = 'gnuplot')
plb.show()

