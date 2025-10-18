#include "CSVReader.h"
#include "Student.h"
#include <cstring>
#include <fstream>

CSVReader::CSVReader():filename(string("")) {}
CSVReader::CSVReader(const CSVReader &other) {}
CSVReader::~CSVReader()=default;

void CSVReader::set_file(const string& _filename) {
    filename = _filename;
}

vector<Student> CSVReader::citeste() const {

    // daca vreo eroare este intalnita in privinta deschiderii fisierului,
    // sau a operarii cu acestuia, este returnat un vector de studenti gol
    vector<Student> studenti;

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
                    studenti.push_back(prelucreaza_linie(buffer));
                }catch (...) { // daca este detectata vreo eroare, linia de text respectiva este ignorata
                    cerr<<"Eroare la prelucrarea liniei " << line_index<<" in fisierul: " << filename <<"\n";
                }
                line_index++;
            }
            return studenti;
        }
        catch(...) {
            cerr<<"\nEroare la citirea fisierului: " << filename <<'\n';
        }
    }

    return studenti;
}

// descompune fiecare linie in fisierul csv si returneaza datele sub forma de obiect student
Student CSVReader::prelucreaza_linie(char* line) {
    try {

        char* nume_complet = strtok(line, ",");
        char* specializare = strtok(nullptr, ",");
        int an = stoi(strtok(nullptr, ","));
        float medie = strtof(strtok(nullptr, ","), nullptr);
        return {nume_complet, specializare, an, medie};
    }
    catch (invalid_argument& exception) {
        cerr<<"\nEroare de conversie la prelucrarea liniei de text. Motiv: " << exception.what()<<"\n";
        throw;
    }
}