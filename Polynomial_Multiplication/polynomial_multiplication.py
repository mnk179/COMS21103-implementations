import numpy as np

def multiply_polynomials(A, B):
    """
    A and B are polynomials of degree-bound n
    represented as numpy arrays

    Assume n is a power of two
    """
    # 1 Double degree-bound
    A = double_degree_bound(A)
    B = double_degree_bound(B)
    # 2 Evaluate
    A = fast_fourier_transform(A)
    B = fast_fourier_transform(B)
    # 3 Pointwise multiply
    C = A * B
    # 4 Interpolate

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
        root_of_unity_n = np.e ** (2 * np.pi * 1j /n)
        root_of_unity = 1
        A0 = np.array([A[x] for x in range(0, n - 1, 2)])
        A1 = np.array([A[x] for x in range(1, n, 2)])
        y0 = fast_fourier_transform(A0)
        y1 = fast_fourier_transform(A1)
        y = np.empty(n, dtype=complex)
        for k in range(int(n / 2)):
            y[k] = y0[k] + root_of_unity * y1[k]
            y[k + int(n / 2)] = y0[k] - root_of_unity * y1[k]
            root_of_unity *= root_of_unity_n
        return y

def inverse_fast_fourier_transform(y):
    def inner_inv_fft(y):
        n = len(y)
        if n == 1:
            return y
        else:
            root_of_unity_n = np.e ** (-2 * np.pi * 1j / n)
            root_of_unity = 1
            y0 = np.array([y[x] for x in range(0, n - 1, 2)])
            y1 = np.array([y[x] for x in range(1, n, 2)])
            A0 = inner_inv_fft(y0)
            A1 = inner_inv_fft(y1)
            A = np.empty(n, dtype=complex)
            for k in range(int(n / 2)):
                A[k] = A0[k] + root_of_unity * A1[k]
                A[k + int(n / 2)] = A0[k] - root_of_unity * A1[k]
                root_of_unity *= root_of_unity_n
            return A
    return inner_inv_fft(y) / len(y)

def naive_dft(A):
    n = len(A)
    roots_of_unity_n = np.roots(np.insert([1, -1], 1, [0] * (n - 2)))
    return np.polyval(A, roots_of_unity_n)