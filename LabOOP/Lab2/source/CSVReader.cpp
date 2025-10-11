#include "CSVReader.h"

CSVReader::CSVReader():filename(string("")) {}
CSVReader::CSVReader(const CSVReader &other) {}
CSVReader::~CSVReader()=default;

void CSVReader::set_file(string& _filename) {
    filename = _filename;
}

vector<Student> CSVReader::read_file() {
    ifstream fin(filename.c_str());
    Student student;
    while (!fin.eof()) {
        fin.getline()
        fin>>student.last_name>>student.first_name>>student.field>>student.study_year>>student.grade_average;
    }
}
