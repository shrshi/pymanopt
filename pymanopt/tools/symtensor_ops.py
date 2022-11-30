import tensorly
import numpy, itertools, more_itertools

def symmetrize(X):
    shape_tuple = tensorly.shape(X)
    r = shape_tuple[0]
    N = len(tensorly.shape(X))

    inds = itertools.combinations_with_replacement(numpy.arange(r), N)
    for i in inds:
        perms = list(more_itertools.distinct_permutations(i))
        val = 0
        for j in perms:
            val += X[j]
        val /= len(perms)
        for j in perms:
            X[j] = val

    #assert issymmetric(X) == True
    return X

def issymmetric(X, eps = 1e-8):
    shape_tuple = tensorly.shape(X)
    r = shape_tuple[0]
    N = len(tensorly.shape(X))

    inds = itertools.combinations_with_replacement(numpy.arange(r), N)
    for i in inds:
        perms = list(more_itertools.distinct_permutations(i))
        val = X[perms[0]]
        for j in range(1, len(perms)):
            if abs(X[perms[j]] - val) > eps:
                return False

    return True
