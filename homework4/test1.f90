program test1
	use quadrature, only: err_table
	
	implicit none
	integer :: nvals(7)

	real(kind=8) :: a, b, integr_true

	nvals = (/5, 10, 20, 40, 80, 160, 320/)

	a = 0.d0
	b = 2.d0
	integr_true = (b - a) + (b**4 -a**4) / 4.d0
	print 10, integr_true
10  format("True integral value: ", es22.14)

	call err_table(f, a, b, nvals, integr_true)

contains

real(kind=8) function f(x)
	implicit none
	real(kind=8), intent(in) :: x

	f = x ** 3 + 1.d0
end function f

end program test1
