#include <iostream>
using namespace std;

class A {
public:
    int ceva;
};

class B : public A {
public:
    char altceva;
};

union Uniune {
    A a;
    B b;
};

int main() {

    B b;
    b.ceva = 10;
    b.altceva = 'b';

    cout<<sizeof(b)<<endl;

    Uniune u;
    u.b = b;

    cout<<sizeof(u)<<endl;
    cout<<sizeof(u.a)<<endl;
    cout<<sizeof(u.b)<<endl;

    // ar trebui sa putem accesa si folosind aritmetica pointerilor

}