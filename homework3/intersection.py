from numpy import *

def fvals(x):
	"""
	Returns f(x)=g1(x)-g2(x) and f'(x) for g1(x)=x*cos(pi*x) and
	g2(x)=1-0.6*x**2
	"""
	f = x * cos(pi * x) - (1. - 0.6 * x**2)
	fp = cos(pi * x) - pi * x * sin(pi * x) + 1.2 * x
	return f, fp

def test1(debug_solve = False):
	"""
	Test Newton method
	"""
	from newton import solve
	for x0 in [-2., -1.5, -1., 1.3]:
		print " "
		x, iters = solve(fvals, x0, debug = debug_solve)
		print "With initial guess x0 = %22.15e" \
			"solve returns x = %22.15e after %i iterations" % (x0, x, iters)