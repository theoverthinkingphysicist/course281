
import numpy as np
import matplotlib.pyplot as plt

class Data:

    def __init__(self, x_data, y_data):

        self.x_label = x_data[0]
        self.y_label = y_data[0]
        self.x_values = np.array(x_data[1:])
        self.y_values = np.array(y_data[1:])

    def plot(self):

        plt.plot(self.x_values, self.y_values, 'mo-')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title('Experimental data')
        plt.grid(True)
        plt.show()

    def to_numpy(self, label):

        if label == self.x_label:
            return self.x_values
        elif label == self.y_label:
            return self.y_values
        else:
            raise ValueError('Hi')

falldata = Data(
    ['heights', 1.0, 0.8, 0.6], ['times', 0.332, 0.300, 0.251])

falldata.plot()
print(falldata.to_numpy('heights'))
print(falldata.to_numpy('times'))