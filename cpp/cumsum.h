#include <iostream>
#include <vector>

void cumsum(std::vector<double> seq,std::vector<double> &cseq){
    double sum = 0;
    for(int i =0; i< seq.size(); i++){
        sum += seq[i];
        cseq[i] = sum;
    }
}


/* For Euler

#include <omp.h>

void cumsum(std::vector<double> seq,std::vector<double> &cseq){
    double sum = 0;
    #pragma omp parallel for reduction(+:sum)
    for(int i =0; i< seq.size(); i++){
        sum += seq[i];
        cseq[i] = sum;
    }
}

*/



