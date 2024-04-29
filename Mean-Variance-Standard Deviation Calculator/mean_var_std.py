import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        mat = np.array(list).reshape(3,3)
        calculations = {}
        calculations['mean'] = [np.mean(mat, 0).tolist(), np.mean(mat, 1).tolist(), np.mean(mat)]
        calculations['variance'] = [np.var(mat, 0).tolist(), np.var(mat, 1).tolist(), np.var(mat)]
        calculations['standard deviation'] = [np.std(mat, 0).tolist(), np.std(mat, 1).tolist(), np.std(mat)]
        calculations['max'] = [np.max(mat, 0).tolist(), np.max(mat, 1).tolist(), np.max(mat)]
        calculations['min'] = [np.min(mat, 0).tolist(), np.min(mat, 1).tolist(), np.min(mat)]
        calculations['sum'] = [np.sum(mat, 0).tolist(), np.sum(mat, 1).tolist(), np.sum(mat)]

    return calculations