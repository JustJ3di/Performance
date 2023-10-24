CC=clang++

CFLAGS=-I.
DEPS = nbody.h

all: nbody.o main.o 
	$(CC) -o nbodySim nbody.o main.o

nbody.o: nbody.cpp $(DEPS)
	$(CC) -c nbody.cpp $(CFLAGS)
	
main.o: 
	$(CC) -c main.cpp $(CFLAGS)

	
clean:
	rm  -f *.o
	rm -f ./nbodySim
