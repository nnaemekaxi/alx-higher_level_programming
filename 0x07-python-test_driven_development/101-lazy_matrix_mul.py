#!/usr/bin/python3
"""
a function that multiplies 2 matrices by using the module NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ calculates the matrix multiplication of two matrices"""
    return numpy.matmul(m_a, m_b)
