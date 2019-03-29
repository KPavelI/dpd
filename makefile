objects = dpd.F90

   FC = mpif90	
   FFLAGS = 
   LDFLAGS = -O2 -ffree-line-length-512 # -xCORE-AVX2 #-heap-arrays
   #LDFLAGS = -O0 -g -CB -traceback
   TARGET = dpd

default: $(objects) 
	$(FC) $(LDFLAGS) -o $(TARGET) $(objects)
   $(objects) :

clean: 
	rm -f $(TARGET) *.o
