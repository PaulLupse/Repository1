#ifndef LAB3_CSVREADER_H
#define LAB3_CSVREADER_H

#include <string>
#include <vector>

using namespace std;

#include "Student.h"

// clasa care faciliteaza citirea din fisiere csv
class CSVReader {
public:
    CSVReader();
    CSVReader(const CSVReader& other);
    ~CSVReader();

    // constructor ce initializeaza numele fisierului
    explicit CSVReader(const string& _filename):filename(_filename){};

    // seteaza numele fisierului ce urmeaza sa fie citit
    void set_file(const string& _filename);

    // returneaza numele fisierului curent
    string get_current_file(){return filename;};

    // citeste fisierul setat si returneaza datele sub forma de vector de studenti
    [[nodiscard]] vector<Student> citeste() const;

private:
    // metoda folosita de functia read() pentru prelucrarea unei linii din fisier, returneaza un obiect de tip student
    static Student prelucreaza_linie(char* line);
    string filename;
};

#endif //LAB3_CSVREADER_H