program intersection
	use newton, only: solve
	use functions, only: f, fprime
	
	real(kind=8) :: x, x0
	real(kind=8) :: x0vals(4)
	integer :: i, iters
	logical :: debug

	debug = .false.
	x0vals = (/-2.d0, -1.5d0, -1.d0, 1.3d0/)

	do i = 1,size(x0vals)
		x0 = x0vals(i)
		call solve(f, fprime, x0, x, iters, debug)
		print 121, x0vals(i), x, iters
121		format('With initial guess x0 = ' es22.15 &
			' solve returns x = ' es22.15 ' after ' i3 ' iterations')
		enddo

end program intersection

