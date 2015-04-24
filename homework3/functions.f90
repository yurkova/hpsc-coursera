module functions
	real(kind=8) :: pi
	save

contains

real(kind=8) function f_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x

    f_sqrt = x**2 - 4.d0

end function f_sqrt


real(kind=8) function fprime_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x
    
    fprime_sqrt = 2.d0 * x

end function fprime_sqrt


real(kind=8) function f(x)
	implicit none
	real(kind=8), intent(in) :: x

	f = x * cos(pi * x) - (1.d0 - 0.6d0 * x**2)

end function f


real(kind=8) function fprime(x)
	implicit none
	real(kind=8), intent(in) :: x

	fprime = cos(pi * x) - pi * x * sin(pi * x) + 1.2d0 * x

end function fprime

end module functions
