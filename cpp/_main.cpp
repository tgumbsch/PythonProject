#include "cumsum.h"

extern "C" {
    //Cummulative sum of array arr to vector v
    void CUMSUM(std::vector<double>* v, double *arr, int length){
        // It is possible to change the testing function here, K-S test or Mann-Whitney, for instance
        std::vector<double> seq(arr, arr + length);
        cumsum(seq,v);
    }

    // Helper fucntions to build the vector containing the time series
    std::vector<double>* new_vector(){
        return new std::vector<double>;
    }
    void delete_vector(std::vector<double>* v){
        // std::cout << "destructor called in C++ for " << v << std::endl;
        delete v;
    }
    int vector_size(std::vector<double>* v){
        return v->size();
    }
    double vector_get(std::vector<double>* v, int i){
        return v->at(i);
    }
    void vector_push_back(std::vector<double>* v, double i){
        v->push_back(i);
    }
}



