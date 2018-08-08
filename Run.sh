#!/bin/bash

# Googletest for C++ function
cd ./cpp/Tests
chmod +x ./runTests.sh
./runTests.sh
cd ../..

#Link C++ to Python
# g++ -std=c++14 -c -fPIC -fopenmp ./cpp/_main.cpp -o ./cpp/CPP.o #For Euler
# g++ -shared -Wl,-soname,./cpp/CPP.so -o ./cpp/CPP.so ./cpp/CPP.o #For Euler
g++ -std=c++14 -c -fPIC ./cpp/_main.cpp -o ./cpp/CPP.o
g++ -shared -Wl,-install_name,./cpp/CPP.so -o ./cpp/CPP.so ./cpp/CPP.o

#Unittesting of R, C++ and Python in Python
python3 Unittest.py

#Runtime of wrapped calls
python3 Runtime.py

#Logging for handling input data
#python ./py/py.py --datadir ./data --outdir ./data
