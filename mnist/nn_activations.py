import numpy as np

class Activations:
    def __init__(self):
        pass

    def sigmoid(self,x):
        return 1 / (1 + np.exp(-x))

    def softmax(self,x):
        shift_x = x - np.max(x)
        exp_shifted = np.exp(shift_x)
        return exp_shifted / np.sum(exp_shifted, axis=0)


    def ReLU(self,x):
        return np.maximum(x,0)