from numpy import *

def fvals(x):
	"""
	Returns f(x)=g1(x)-g2(x) and f'(x)
	"""
	f = g1(x) - g2(x)
	fp = cos(pi * x) - pi * x * sin(pi * x) + 1.2 * x
	return f, fp

def g1(x):
	return x * cos(pi * x)

def g2(x):
	return 1. - 0.6 * x**2

def plot_functions(x0):
	"""
	Plot g1(x), g2(x) and intersection points
	"""
	from matplotlib import pyplot as plt
	x = linspace(-5, 5, 1000)
	y1 = g1(x)
	y2 = g2(x)
	y0 = g1(x0)
	plt.figure(1)
	plt.clf()
	line1, = plt.plot(x, y1, 'b-')
	line2, = plt.plot(x, y2, 'r-')
	plt.legend((line1, line2), ('g1(x)', 'g2(x)'))
	plt.plot(x0, y0, 'ko')
	plt.savefig('intersections.png')



def test1(debug_solve = False):
	"""
	Test Newton method
	"""
	from newton import solve
	init_points = [-2., -1.5, -1., 1.3]
	evaluated_points = list()
	for x0 in init_points:
		print " "
		x, iters = solve(fvals, x0, debug = debug_solve)
		evaluated_points.append(x)
		print "With initial guess x0 = %22.15e" \
			"solve returns x = %22.15e after %i iterations" % (x0, x, iters)
	plot_functions(array(evaluated_points))