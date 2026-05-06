import numpy as np

from .utils import euclid_dist

class KNN:
    X = None
    y = None
    
    def __init__(self, k):
        self.k = k
    
    def fit(self, X, y):
        self.X = X
        self.y = y
    
    def predict(self, X_hat):
        y_hat = [-1] * len(X_hat)
        for n in range(0, len(X_hat)):
            x1 = X_hat[n]
            
            #calculating distances to training data
            distances = np.zeros(len(self.X))
            for i in range(0, len(self.X)):
                x2 = self.X[i]
                dist = euclid_dist(x1, x2)
                distances[i] = dist
            sorted_dist_ind = np.argsort(distances)
            
            #finding best label
            counts = {}
            best_lab = -1
            max_count = 0
            for j in range(0, self.k):
                lab = self.y[sorted_dist_ind[j]]
                if lab not in counts.keys():
                    counts[lab] = 1
                else:
                    counts[lab] += 1
                if counts[lab] > max_count:
                    best_lab = lab
                    max_count = counts[lab]
            y_hat[n] = best_lab
                    
        return y_hat