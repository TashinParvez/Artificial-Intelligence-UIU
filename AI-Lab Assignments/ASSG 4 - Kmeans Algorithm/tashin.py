import numpy as np
from matplotlib import pyplot as plt

X = np.loadtxt('/content/jain_feats.txt')
centroid_old = np.loadtxt('/content/jain_centers.txt')

centroid_new = np.zeros((2, 2))


plt.scatter(X[: , 0], X[: , 1], color="blue", s=10, marker='.')
plt.scatter(centroid_old[: , 0], centroid_old[: , 1], color="orange", s=120, marker='*')

plt.show()
plt.clf()

label = np.empty(len(X))
# print(label)

for e in range(100):
  for i in range(X.shape[0]):
    dist = np.empty(centroid_old.shape[0])

    for j in range(centroid_old.shape[0]): 
        dist[j] = np.sqrt((X[i, 0] - centroid_old[j, 0]) ** 2 + (X[i, 1] - centroid_old[j, 1]) ** 2)
    label[i] = np.argmin(dist)

  
  # Update centroid 
  for j in range(centroid_new.shape[0]):
    centroid_new[j] = np.average(X[label == j], axis=0)

  differences = np.abs(centroid_new - centroid_old)
  max_difference = np.max(differences)

  # Breaking condition check
  if max_difference < 1e-7:
    break
  else:
    centroid_old = np.copy(centroid_new)


plt.scatter(X[np.where(label == 0)[0], 0], X[np.where(label == 0)[0], 1], s=10, color='red')
plt.scatter(X[np.where(label == 1)[0], 0], X[np.where(label == 1)[0], 1], s=10, color='green')

plt.scatter(centroid_old[0, 0], centroid_old[0, 1], marker='*', s=200, color='red')
plt.scatter(centroid_old[1, 0], centroid_old[1, 1], marker='*', s=200, color='green')
plt.show()
