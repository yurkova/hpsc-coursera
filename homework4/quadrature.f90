module quadrature

contains

real(kind=8) function trapezoid(f, a, b, n)

    ! Estimate the integral of f(x) from a to b using the
    ! Trapezoid Rule with n points.

	implicit none
	real(kind=8), intent(in) :: a, b
	real(kind=8), external :: f
	integer, intent(in) :: n

	real(kind=8) :: xi, h
	integer :: i

	h = (b - a) / (n - 1.d0)
	trapezoid = 0.d0
	xi = a

	do i = 2, n - 1
		xi = xi + h
		trapezoid = trapezoid + f(xi) * h 
	enddo

	trapezoid = trapezoid + 0.5d0 * (f(a) + f(b)) * h

end function trapezoid


subroutine err_table(f, a, b, nvals, integr_true)
	implicit none
	real(kind=8), external :: f
	real(kind=8), intent(in) :: a, b, integr_true
	integer, dimension(:), intent(in) :: nvals

	real(kind=8) :: last_error, error, ratio, integr_trap
	integer :: i

	last_error = 0.d0 

	print *, "    n         trapezoid            error       ratio"

	do i = 1, size(nvals)
        integr_trap = trapezoid(f, a, b, nvals(i))
        error = abs(integr_trap - integr_true)
        ratio = last_error / error
        last_error = error

	    print 11, nvals(i), integr_trap, error, ratio
11      format(i8, es22.14, es13.3, es13.3)
	enddo

end subroutine err_table

end module quadrature



