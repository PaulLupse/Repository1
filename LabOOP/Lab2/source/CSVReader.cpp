#include "CSVReader.h"
#include <cstring>
#include <fstream>

CSVReader::CSVReader():filename(string("")) {}
CSVReader::CSVReader(const CSVReader &other) {}
CSVReader::~CSVReader()=default;

void CSVReader::set_file(const string& _filename) {
    filename = _filename;
}

vector<Student> CSVReader::read() const {

    // daca vreo eroare este intalnita in privinta deschiderii fisierului,
    // sau a operarii cu acestuia, este returnat un vector de studenti gol
    vector<Student> students;

    ifstream fin;
    fin.open(filename);
    // daca fisierul nu e deschis, atunci a aparut o eroare la deschiderea acestuia
    if (!fin.is_open()) {
        cerr<<"Eroare la deschiderea fisierului cu numele: " << filename << endl;
    }
    else {
        try{

            int line_index = 0;
            while (!fin.eof()) {
                char buffer[105];
                fin.getline(buffer, 100);
                try {
                    students.push_back(parse_line(buffer));
                }catch (...) { // daca este detectata vreo eroare, linia de text respectiva este ignorata
                    cerr<<"Eroare la prelucrarea liniei " << line_index<<" in fisierul: " << filename <<"\n";
                }
                line_index++;
            }
            return students;
        }
        catch(...) {
            cerr<<"\nEroare la citirea fisierului: " << filename <<'\n';
        }
    }

    return students;
}

// descompune fiecare linie in fisierul csv si returneaza datele sub forma de obiect student
Student CSVReader::parse_line(char* line) {
    try {

        Student new_student;
        char* field = strtok(line, ",");
        new_student.nume_de_familie = field;
        field = strtok(nullptr, ",");
        new_student.prenume = field;
        field = strtok(nullptr, ",");
        new_student.specializare = field;
        field = strtok(nullptr, ",");
        new_student.an = stoi(field);
        field = strtok(nullptr, ",");
        new_student.medie = strtof(field, nullptr);
        return new_student;
    }
    catch (invalid_argument& exception) {
        cerr<<"\nEroare de conversie la prelucrarea liniei de text. Motiv: " << exception.what()<<"\n";
        throw;
    }
}