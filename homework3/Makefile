# $UWHPSC/codes/fortran/newton/Makefile

OBJECTS = functions.o newton.o test1.o
OBJECTS_INTERSECTION = functions.o newton.o intersection.o
MODULES = functions.mod newton.mod

FFLAGS = -g

.PHONY: test1 clean 

intersections: intersection.exe
	./intersection.exe

intersection.exe: $(MODULES) $(OBJECTS_INTERSECTION)
	gfortran $(FFLAGS) $(OBJECTS_INTERSECTION) -o intersection.exe

test1: test1.exe
	./test1.exe

test1.exe: $(MODULES) $(OBJECTS)
	gfortran $(FFLAGS) $(OBJECTS) -o test1.exe

%.o : %.f90
	gfortran $(FFLAGS) -c  $< 

%.mod: %.f90
	gfortran $(FFLAGS) -c $<

clean:
	rm -f *.o *.exe *.mod

