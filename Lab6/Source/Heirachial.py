import numpy as np   # importing numpy
from scipy.cluster.hierarchy import linkage, dendrogram   # importing scipy.cluster for hierarchy
import matplotlib.pyplot as plt   # use of matplotlib for plotting

data = np.array([[2,4],[4.1,5],[5.4,3],[3,3],[6,6.5], [7.5,5.5]])   #  assigning the points to data
plt.scatter(data[:,0], data[:,1], s=40)  # scatter the values for s=40
# defining the matrix for linkage
linkage_matrix = linkage(data, "ward")
dendogram = dendrogram(linkage_matrix, truncate_mode='none')     # use of dendogram with truncate mode=none
# to show
plt.show()