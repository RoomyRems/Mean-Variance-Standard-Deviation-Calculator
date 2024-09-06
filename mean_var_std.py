import numpy as np

list = [0,1,2,3,4,5,6,7,8]

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    my_array = np.reshape(list, newshape=(3,3))
    calculations = {
        'mean': [np.mean(my_array, axis=0).tolist(), np.mean(my_array, axis=1).tolist(), np.mean(my_array)],
        'variance': [np.var(my_array, axis=0).tolist(), np.var(my_array, axis=1).tolist(), np.var(my_array)],
        'standard deviation': [np.std(my_array, axis=0).tolist(), np.std(my_array, axis=1).tolist(), np.std(my_array)],
        'max': [np.max(my_array, axis=0).tolist(), np.max(my_array, axis=1).tolist(), np.max(my_array)],
        'min': [np.min(my_array, axis=0).tolist(), np.min(my_array, axis=1).tolist(), np.min(my_array)],
        'sum': [np.sum(my_array, axis=0).tolist(), np.sum(my_array, axis=1).tolist(), np.sum(my_array)]
    }
    return calculations

print(calculate(list))