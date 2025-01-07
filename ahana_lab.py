import numpy as np

def dominance(arr):
    dominance_x = 0
    dominance_o = 0
    if np.count_nonzero(arr == 'x') == 3:
        dominance_x = 100
    elif np.count_nonzero(arr == 'o') == 3:
        dominance_o = 100
    elif np.count_nonzero(arr == 'x') > np.count_nonzero(arr == 'o'):
        dominance_x += np.count_nonzero(arr == 'x')
    elif np.count_nonzero(arr == 'x') < np.count_nonzero(arr == 'o'):
        dominance_o += np.count_nonzero(arr == 'o')
    elif np.count_nonzero(arr == 'x') == np.count_nonzero(arr == 'o'):
        dominance_x = 0
        dominance_o = 0

    return [dominance_x, dominance_o]

def strength(array):
    strength_x = 0
    strength_o = 0
    domin_x = 0
    domin_o = 0

    #for rows
    for i in range(array.shape[0]):
        dom = dominance(array[i])
        total_dominance_x = 0
        total_dominance_o = 0
        if dom[0] == 100:
            strength_x = dom[0]
            return [strength_x, strength_o]
        elif dom[1] == 100:
            strength_o = dom[1]
            return [strength_x, strength_o]
        elif dom[0] > dom[1]:
            total_dominance_x += dom[0]
            total_dominance_o = 0
        elif dom[0] < dom[1]:
            total_dominance_x = 0
            total_dominance_o += dom[1]
        elif dom[0] == 0 and dom[1] == 0:
            total_dominance_x = 0
            total_dominance_o = 0
        domin_x += total_dominance_x
        domin_o += total_dominance_o
        
    for i in range(array.shape[1]):
        dom = dominance(array[:, i])
        total_dominance_x = 0
        total_dominance_o = 0
        if dom[0] == 100:
            strength_x = dom[0]
            return [strength_x, strength_o]
        elif dom[1] == 100:
            strength_o = dom[1]
            return [strength_x, strength_o]
        elif dom[0] > dom[1]:
            total_dominance_x += dom[0]
            total_dominance_o = 0
        elif dom[0] < dom[1]:
            total_dominance_x = 0
            total_dominance_o += dom[1]
        elif dom[0] == 0 and dom[1] == 0:
            total_dominance_x = 0
            total_dominance_o = 0
        domin_x += total_dominance_x
        domin_o += total_dominance_o
        
        diag1 = [array[i][i] for i in range(3)]
        dom1 = dominance(diag1)
        total_dom_x = 0
        total_dom_o = 0
        if dom[0] == 100:
            strength_x = dom[0]
            return [strength_x, strength_o]
        elif dom[1] == 100:
            strength_o = dom[1]
            return [strength_x, strength_o]
        elif dom[0] > dom[1]:
            total_dom_x += dom[0]
            total_dom_o = 0
        elif dom[0] < dom[1]:
            total_dom_x = 0
            total_dom_o += dom[1]
        elif dom[0] == 0 and dom[1] == 0:
            total_dom_x = 0
            total_dom_o = 0
        domin_x += total_dom_x
        domin_o += total_dom_o
        
    
        diag2 = [array[i][2-i] for i in range(3)]
        dom2 = dominance(diag1)
        total_dom_x1 = 0
        total_dom_o1 = 0
        if dom[0] == 100:
            strength_x = dom[0]
            return [strength_x, strength_o]
        elif dom[1] == 100:
            strength_o = dom[1]
            return [strength_x, strength_o]
        elif dom[0] > dom[1]:
            total_dom_x1 += dom[0]
            total_dom_o1 = 0
        elif dom[0] < dom[1]:
            total_dom_x1 = 0
            total_dom_o1 += dom[1]
        elif dom[0] == 0 and dom[1] == 0:
            total_dom_x1 = 0
            total_dom_o1 = 0
        domin_x += total_dom_x1
        domin_o += total_dom_o1
        
    strength_x = domin_x - domin_o
    strength_o = -strength_x

    return [strength_x, strength_o]


tictac = np.array([['x', 'b', 'b'],['b', 'x', 'b'], ['o', 'b', 'b']])
print(strength(tictac))
