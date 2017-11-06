#!/bin/bash

g++ -std=c++14 -c -fPIC ./cpp/_main.cpp -o ./cpp/CPP.o
g++ -shared -Wl,-install_name,./cpp/CPP.so -o ./cpp/CPP.so ./cpp/CPP.o
python Unittest.py #unittesting
python Runtime.py #runtime
python ./py/py.py #logging for handeling data
