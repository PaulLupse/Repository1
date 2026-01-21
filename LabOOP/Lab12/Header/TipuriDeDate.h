//
// Created by Paul on 17-Dec-25.
//

#ifndef LAB4_TIPURIDEDATE_H
#define LAB4_TIPURIDEDATE_H

#include <iostream>
using namespace std;

class Int{

    int v;

public:

    Int(const int &v):v(v){}

    void afiseaza(){cout<<v;}

    static bool compare(Int* a, Int* b) { return a->v > b->v; };

    friend ostream& operator<<(ostream & out_stream, Int& integer) { out_stream << integer.v << "\n"; return out_stream; };
    friend ostream& operator<<(ostream & out_stream, Int* integer) { out_stream << integer->v << "\n"; return out_stream; };
};



class Float{

    float v;

public:

    Float(const float &v):v(v){}

    void afiseaza(){cout<<v;}

    static bool compare(Float* a, Float* b) { return a->v > b->v; };

    friend ostream& operator<<(ostream & out_stream, Float& floating) { out_stream << floating.v << "\n"; return out_stream; };
    friend ostream& operator<<(ostream & out_stream, Float* floating) { out_stream << floating->v << "\n"; return out_stream; };

};

#endif //LAB4_TIPURIDEDATE_H