import numpy, tensorly
from tensorly import random
from tensorly.tenalg import inner
from scipy.special import comb
from pymanopt.manifolds.manifold import RiemannianSubmanifold
import pymanopt.tools.symtensor_ops as symops

class Symtensor(RiemannianSubmanifold):
    def __init__(self, length, order):
        self.r = length
        self.N = order
        name = f"Order-{order} symmetric tensor with each dimension of length {length}"
        dimension = comb(order + length - 1, length, exact = True)
        super().__init__(name, dimension)

    def inner_product(self, point, tangent_vector_a, tangent_vector_b):
        #return tensorly.sum(tensorly.dot(tangent_vector_a, tangent_vector_b))
        return inner(tangent_vector_a, tangent_vector_b)

    def projection(self, point, vector):
        return symops.symmetrize(vector)

    def norm(self, point, tangent_vector):
        return tensorly.norm(tangent_vector)

    def random_point(self):
        X = random.random_tensor((self.r, ) * self.N)
        return symops.symmetrize(X)

    def random_tangent_vector(self, point):
        X = self.random_point()
        return X/tensorly.norm(X)

    def zero_vector(self, point):
        return tensorly.zeros((self.r, ) * self.N)

    def dist(self, point_a, point_b):
        return tensorly.norm(point_a - point_b)

    def euclidean_to_riemannian_gradient(self, point, euclidean_gradient):
        return self.projection(point, euclidean_gradient)

    def retraction(self, point, tangent_vector):
        return self.exp(point, tangent_vector)

    def exp(self, point, tangent_vector):
        return point + tangent_vector

    def transport(self, point_a, point_b, tangent_vector_a):
        return tangent_vector_a

    to_tangent_space = projection 
