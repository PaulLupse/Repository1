#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

class VectorCompact {
private:
    struct Element {
        int valoare = 0;
        int linie = 0;
        int coloana = 0;
    };
    vector<Element> date;
public:
    VectorCompact(string nume_fisier);
    void afiseaza();
};

// constructor ce citeste fisierul cu numele pasat
VectorCompact::VectorCompact(string nume_fisier) {
    ifstream fin(nume_fisier);
    int n, m;
    fin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int element_matrice;
            fin >> element_matrice;
            if (element_matrice) {
                date.push_back({element_matrice, i, j});
            }
        }
    }
}

void VectorCompact::afiseaza() {
    for (Element element : date ) {
        cout << "Element: " << element.valoare << " | Linie: " << element.linie << " | Coloana: " << element.coloana << endl;
    }
}



int main() {
    VectorCompact v("lab1.in");
    v.afiseaza();
}