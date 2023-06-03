import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    array = np.array(list).reshape(3,3)

    calculations = {}
    mean = []
    mean.append(array.mean(axis=0).tolist())
    mean.append(array.mean(axis=1).tolist())
    mean.append(array.flatten().mean().tolist())
    calculations['mean'] = mean

    variance = []
    variance.append(array.var(axis=0).tolist())
    variance.append(array.var(axis=1).tolist())
    variance.append(array.flatten().var().tolist())
    calculations['variance'] = variance

    stdDeviation = []
    stdDeviation.append(array.std(axis=0).tolist())
    stdDeviation.append(array.std(axis=1).tolist())
    stdDeviation.append(array.flatten().std().tolist())
    calculations['standard deviation'] = stdDeviation

    maximum = []
    maximum.append(array.max(axis=0).tolist())
    maximum.append(array.max(axis=1).tolist())
    maximum.append(array.flatten().max().tolist())
    calculations['max'] = maximum

    minimum = []
    minimum.append(array.min(axis=0).tolist())
    minimum.append(array.min(axis=1).tolist())
    minimum.append(array.flatten().min().tolist())
    calculations['min'] = minimum

    sum = []
    sum.append(array.sum(axis=0).tolist())
    sum.append(array.sum(axis=1).tolist())
    sum.append(array.flatten().sum().tolist())
    calculations['sum'] = sum

    return calculations