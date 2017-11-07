#include <iostream>
#include <vector>

void cumsum(std::vector<double> seq,std::vector<double>* v){
    double sum = 0;
    for(int i =0; i< seq.size(); i++){
        sum += seq[i];
        v->push_back(sum); //expensive operation
    }
}


