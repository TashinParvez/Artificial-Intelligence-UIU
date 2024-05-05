import numpy as np
import pandas as pd
import math

df = pd.read_csv('iris.csv')  # CSV

data_array = df.values

x = np.array(data_array[:, 2:])
y = np.array(data_array[:, 0], dtype=int)

length = len(x)
arr = np.arange(length)
np.random.shuffle(arr)

k = 5
m = int(length * 0.8)

x_train = x[arr[:m]]
y_train = y[arr[:m]]
x_test = x[arr[m:]]
y_test = y[arr[m:]]

M_prime = length - m

y_test_predicted = np.zeros(M_prime)

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

for i in range(len(x_test)):
    distances = np.zeros(m)
    for j in range(m):
        distances[j] = euclidean_distance(x_test[i], x_train[j])
        
    min_dist_indices = np.argsort(distances)[:k]
    y_neighbor = y_train[min_dist_indices]
    y_test_predicted[i] = np.bincount(y_neighbor).argmax()


# Metrics Calculation
accuracy = np.sum(y_test_predicted == y_test) / len(y_test)
print(accuracy)