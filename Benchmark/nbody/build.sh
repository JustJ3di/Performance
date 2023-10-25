rm -f *.o
rm -f nbodySim
clang++ -c -o main.o main.cpp 
clang++ -c -o nbody.o nbody.cpp 
clang++ -o nbodySim nbody.o main.o