#!/bin/bash

# Googletest for C++ function
cd ./cpp/Tests
chmod +x ./runTests.sh
./runTests.sh
cd ../..

#Link C++ to Python, for some OS try line 12 instead of 13 if 12 gives an error
g++ -std=c++14 -c -fPIC ./cpp/_main.cpp -o ./cpp/CPP.o
g++ -shared -Wl,-install_name,./cpp/CPP.so -o ./cpp/CPP.so ./cpp/CPP.o
# g++ -shared -Wl,-soname,./cpp/CPP.so -o ./cpp/CPP.so ./cpp/CPP.o

#Unittesting of R, C++ and Python in Python
python Unittest.py

#Runtime of wrapped calls
python Runtime.py

#Logging for handling input data
python ./py/py.py --datadir ./data --outdir ./data
