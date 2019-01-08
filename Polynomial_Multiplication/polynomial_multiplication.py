import numpy as np

def multiply_polynomials(A, B):
    """
    A and B are polynomials of degree-bound n
    represented as a numpy arrays
    """
    # 1 Double degree-bound
    A = double_degree_bound(A)
    B = double_degree_bound(B)
    # 2 Evaluate
    A = fast_fourier_transform(A)
    B = fast_fourier_transform(B)

    # Pointwise multiply
    # Interpolate

def double_degree_bound(A):
    """
    A is a polynomial of degree-bound n
    represented as a numpy array
    """
    return np.append([0] * len(A), A)

def fast_fourier_transform(A):
    """
    Input:
    A is a polynomial of degree-bound n
    represented as a numpy array

    Output:
    Result of evaluating A at nth roots of unity,
    where n is the degree-bound of A
    """
    n = len(A)
    if n == 1:
        return A
    else:
        root_of_unity_n = np.roots(np.insert([1, -1], 1, [0] * (n - 2)))[-1]
        root_of_unity = 1
        A0 = np.array([A[x] for x in range(0, n - 1, 2)])
        A1 = np.array([A[x] for x in range(1, n, 2)])
        y0 = fast_fourier_transform(A0)
        y1 = fast_fourier_transform(A1)
        y = np.empty(n, dtype=complex)
        for k in range(int(n / 2)):
            y[0] = y0[k] + root_of_unity * y1[k]
            y[k + int(n / 2)] = y0[k] - root_of_unity * y1[k]
            root_of_unity *= root_of_unity_n
        return y
