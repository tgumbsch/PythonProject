#include"../cumsum.h"




#include<gtest/gtest.h>

TEST(cumsum, zerohandle){
    std::vector<double> seq = {};
    std::vector<double> v = {};
    cumsum(seq, &v);
    EXPECT_EQ(seq,v);
}

TEST(cumsum, example){
    std::vector<double> seq = {1,2,3,4};
    std::vector<double> sol = {1,3,6,10};
    std::vector<double> v = {};
    cumsum(seq, &v);
    EXPECT_EQ(sol,v);
}

#include <random>

TEST(cumsum, stdrandom){
    std::mt19937 gen(0);
    std::normal_distribution<double> norm(0,1.);
    std::vector<double> seq;
    for(int k = 0; k<1000000;k++){
        double append = norm(gen);
        seq.push_back(append);
    }
    std::vector<double> sol(seq.size());
    std::partial_sum(seq.begin(), seq.end(), sol.begin());
    std::vector<double> v = {};
    cumsum(seq, &v);
    EXPECT_EQ(sol,v);
}




