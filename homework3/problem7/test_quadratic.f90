program test_quadratic

	use functions, only: f_quadratic, fprime_quadratic, eps
	use newton, only: solve, tol

	real(kind=8) :: x, x0, xstar, fx
	real(kind=8) :: eps_values(3), tol_values(3)
	integer :: i, j, iters
	logical :: debug

	debug = .false.

	x0 = 4.d0
	print 110, x0
110 format("Starting with initial guess ", es22.15,/)

	eps_values = (/1.d-04, 1.d-08, 1.d-12/)
	tol_values = (/1.d-05, 1.d-10, 1.d-14/)

	print 111
111	format('    epsilon        tol    iters          x                 ' &
'f(x)        x-xstar')

	do i=1,size(eps_values)
		eps = eps_values(i)
		xstar = 1.d0 + eps**(0.25d0)

		do j=1,size(tol_values)
			tol = tol_values(j)
			call solve(f_quadratic, fprime_quadratic, x0, x, iters, debug)
			fx = f_quadratic(x)			

			print 112, eps, tol, iters, x, fx, x-xstar
112	format(2es13.3, i4, es24.15, 2es13.3)

			enddo
		print *, ' '
		enddo

end program test_quadratic
