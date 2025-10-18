#include "CSVReader.h"
#include "Student.h"
#include "Sorter.h"
#include <vector>
#include <iostream>

// functie generica ce serveste la afisarea unui vector din STL
template <typename _type>
ostream& operator<<(ostream& os, vector<_type>& v) {
    for (auto iterator = v.begin(); iterator != v.end(); ++iterator) {
        cout << *iterator <<endl;
    }
    return os;
}

int main() {

    vector<Student> students = CSVReader("studenti.csv").read();
    sort_vector(students, (int)students.size(), Student::compare_medie);
    cout << students;

    return 0;
}