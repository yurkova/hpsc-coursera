program test2
	use quadrature, only: err_table
	use omp_lib
	
	implicit none
	integer :: nvals(12), i

	real(kind=8) :: a, b, k, integr_true

	!$ call omp_set_num_threads(2)

	do i = 1, 12
		nvals(i) = 5 * 2**(i - 1)
	enddo

	a = 0.d0
	b = 2.d0
	k = 1.d3

	integr_true = (b - a) + (b**4 -a**4) / 4.d0 - (1.d0 / k) * &
		(cos(k * b) - cos (k * a))
	print 10, integr_true
10  format("True integral value: ", es22.14)

	call err_table(f, a, b, nvals, integr_true)

contains

real(kind=8) function f(x)
	implicit none
	real(kind=8), intent(in) :: x

    f = x**3 + sin(k * x) + 1.d0
end function f

end program test2
