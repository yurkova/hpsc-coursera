OBJECTS = functions.o newton.o test_quadratic.o
MODULES = functions.mod newton.mod

FFLAGS = -g

.PHONY: test_quadratic clean 

test_quadratic: test_quadratic.exe
	./test_quadratic.exe

test_quadratic.exe: $(MODULES) $(OBJECTS)
	gfortran $(FFLAGS) $(OBJECTS) -o test_quadratic.exe

%.o : %.f90
	gfortran $(FFLAGS) -c  $< 

%.mod: %.f90
	gfortran $(FFLAGS) -c $<

clean:
	rm -f *.o *.exe *.mod

