def solve(fvals, x0, debug = False):
    """
    Return the approximation to the root evaluated and the number of 
    iterations taken.
    """
    tol = 1e-14
    maxiter = 20
    
    if debug:
        print "Initial guess: x = %22.15e" % x0
        
    x = x0;
    for i in range(maxiter):
        f, fp = fvals(x)
        if abs(f) < tol:
            break
        x = x - f / fp
        
        if debug:
            print "After %i iterations, x = %22.15e" % (i + 1, x)
            
        if i == maxiter - 1:
            if abs(f) > tol:
                print "*** WARNING: Not enough iterations to evaluate x "\
                "with the tolerance specified."                
    return x, i 

def fvals_sqrt(x):
    """
    Return f(x) and f'(x) for applying Newton to find a square root.
    """
    f = x**2 - 4.
    fp = 2.*x
    return f, fp

def test1(debug_solve=False):
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    for x0 in [1., 2., 100.]:
        print " "  # blank line
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"
