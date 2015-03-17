"""
Homework 2b.
Module for polynomial interpolation.
"""

import numpy as np
import matplotlib.pyplot as plt

def quad_interp(xi, yi):
    """
    Quadratic interpolation. Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2.
    Returns C, an array containing the coefficients of
      p(x) = C[0] + C[1] * x + C[2] * x**2.
    """ 
    
    # Check inputs and print error message if not valid:    
    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message
    error_message = "xi and yi should have length 3"
    assert len(xi)==3 and len(yi)==3, error_message

    # Set up linear system to interpolate through data points:        
    A = np.vstack([np.ones(3), xi, xi**2]).T
    b = yi
    
    # Solve the system of linear equations
    C = np.linalg.solve(A, yi)
    return C    


def cubic_interp(xi, yi):
    """
    Cubic interpolation. Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2,3.
    Returns C, an array containing the coefficients of
    p(x) = C[0] + C[1] * x + C[2] * x**2 + C[3] * x**3.
    """ 
    
    # Check inputs and print error message if not valid:    
    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message
    error_message = "xi and yi should have length 4"
    assert len(xi)==4 and len(yi)==4, error_message

    # Set up linear system to interpolate through data points:        
    A = np.vstack([np.ones(4), xi, xi**2, xi**3]).T
    b = yi
    
    # Solve the system of linear equations
    C = np.linalg.solve(A, yi)
    return C    

    
def poly_interp(xi, yi):
    """
    General polynomial interpolation. Compute the coefficients of the
    polynomial interpolating the points (xi[i],yi[i]) for i = 0,1,..,n-1.
    Returns C, an array containing the coefficients of
    p(x) = C[0] + C[1] * x + ... + C[n-1] * x**(n-1).
    """ 
    
    # Check inputs and print error message if not valid:    
    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message
    error_message = "xi and yi should have equal length"
    assert len(xi) == len(yi), error_message

    # Set up linear system to interpolate through data points:        
    n = len(xi)
    A = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = xi[i] ** j
    b = yi
    
    # Solve the system of linear equations
    C = np.linalg.solve(A, yi)
    return C
    
    
def plot_quad(xi, yi):
    """
    Perform quadratic interpolation and plot the function along with the data 
    points that it interpolates.
    """
    
    # Compute the coefficients:
    C = quad_interp(xi, yi)
    
    # Plot the resulting polynomial:
    x = np.linspace(xi.min() - 1, xi.max() + 1, 1000)
    y = C[0] + C[1] * x + C[2] * x**2

    plt.figure(1)
    plt.clf()
    plt.plot(x, y, "b-")
    
    # Add data points
    plt.plot(xi, yi, "ro")
    
    plt.ylim(yi.min() - 1, yi.max() + 1)
    plt.title("Data points and interpolating polynomial")
    plt.savefig('quadratic.png') 


def plot_cubic(xi, yi):
    """
    Perform cubic interpolation and plot the function along with the data 
    points that it interpolates.
    """
    
    # Compute the coefficients:
    C = cubic_interp(xi, yi)
    
    # Plot the resulting polynomial:
    x = np.linspace(xi.min() - 1, xi.max() + 1, 1000)
    y = C[0] + C[1] * x + C[2] * x**2 + C[3] * x**3

    plt.figure(1)
    plt.clf()
    plt.plot(x, y, "b-")
    
    # Add data points    
    plt.plot(xi, yi, "ro")
    
    plt.ylim(yi.min() - 1, yi.max() + 1)
    plt.title("Data points and interpolating polynomial")
    plt.savefig('cubic.png')  

    
def plot_poly(xi, yi):
    """
    Perform polynomial interpolation and plot the function along with the data 
    points that it interpolates.
    """
    
    # Compute the coefficients:
    C = poly_interp(xi, yi)
    
    # Plot the resulting polynomial:
    x = np.linspace(xi.min() - 1, xi.max() + 1, 1000)
    
    # Use Horner's rule:
    n = len(xi)
    y = C[n-1]
    for j in range(n-1, 0, -1):
        y = y*x + C[j-1]

    plt.figure(1)
    plt.clf()
    plt.plot(x, y, "b-")
    
    # Add data points
    plt.plot(xi, yi, "ro")
    
    plt.ylim(yi.min() - 5, yi.max() + 5)
    plt.title("Data points and interpolating polynomial")
    plt.savefig('poly.png')    

    
def test_quad1():
    """
    Test code, no return value or exception if test runs properly.
    """
    
    xi = np.array([-1., 0., 2.])
    yi = np.array([1., -1., 7.])
    C = quad_interp(xi, yi)
    C_true = np.array([-1., 0., 2.])
    print "C =      ", C
    print "C_true = ", C_true
    
    # Test that all elements have small error:
    assert np.allclose(C, C_true), \
        "Incorrect result, C = %s, Expected: C = %s" % (C, C_true)
        
    # Create a plot:
    plot_quad(xi, yi)


def test_quad2():
    """
    Test code, no return value or exception if test runs properly.
    """
    
    C_true = np.array([-12., 8., -1.])
    xi = np.array([2., 3., 4.])
    yi = C_true[0] + C_true[1] * xi + C_true[2] * xi**2
    
    C = quad_interp(xi, yi)

    print "C =      ", C
    print "C_true = ", C_true
    
    # Test that all elements have small error:
    assert np.allclose(C, C_true), \
        "Incorrect result, C = %s, Expected: C = %s" % (C, C_true) 
    
    # Create a plot:
    plot_quad(xi, yi)         

        
def test_cubic1():
    """
    Test code, no return value or exception if test runs properly.
    """
    
    C_true = np.array([-2., 0., 3., -1.])
    xi = np.array([0., 1., 2., 3.])
    yi = C_true[0] + C_true[1] * xi + C_true[2] * xi**2 + C_true[3] * xi**3

    C = cubic_interp(xi,yi)
    
    print "C =      ", C
    print "C_true = ", C_true
    
    # Test that all elements have small error:
    assert np.allclose(C, C_true), \
        "Incorrect result, C = %s, Expected: C = %s" % (C, C_true)
        
    # Create a plot:
    plot_cubic(xi, yi)

        
def test_poly1():
    """
    Test code, no return value or exception if test runs properly.
    """
    
    C_true = np.array([-8., 4., 6., -5., 1.])
    xi = np.array([-2., -1, 1., 2., 3])
    
    # Use Horner's rule:
    n = len(xi)
    yi = C_true[n-1]
    for i in range(n-1, 0, -1):
        yi = yi * xi + C_true[i-1]
        
    C = poly_interp(xi, yi)

    print "C =      ", C
    print "C_true = ", C_true
    
    # Test that all elements have small error:
    assert np.allclose(C, C_true), \
        "Incorrect result, C = %s, Expected: C = %s" % (C, C_true)
        
    # Create a plot:
    plot_poly(xi, yi)

              
def test_poly2():
    """
    Test code, no return value or exception if test runs properly.
    """
    
    C_true = np.array([-1., 0., 1., -4., 0., 1.])
    xi = np.array([3., 2., 1., 0., -1., -2.])
    
    # Use Horner's rule:
    n = len(xi)
    yi = C_true[n-1]
    for i in range(n-1, 0, -1):
        yi = yi * xi + C_true[i-1]
        
    C = poly_interp(xi, yi)

    print "C =      ", C
    print "C_true = ", C_true
    
    # Test that all elements have small error:
    assert np.allclose(C, C_true), \
        "Incorrect result, C = %s, Expected: C = %s" % (C, C_true)  
        
    # Create a plot:
    plot_poly(xi, yi)
          
if __name__ == "__main__":

    # "main program"
    print "Running tests..."
    test_quad1()
    test_quad2()
    test_cubic1()
    test_poly1()
    test_poly2()
 
