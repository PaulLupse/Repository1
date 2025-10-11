#ifndef LAB2_READER_H
#define LAB2_READER_H

#include <fstream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

#include "Student.h"

class CSVReader {
public:
    CSVReader();
    CSVReader(const CSVReader& other);
    ~CSVReader();

    CSVReader(string& _filename):filename(_filename){};

    void set_file(string& _filename);
    string get_current_file(){return filename;};
    vector<Student> read_file();

private:
    string filename;
};

#endif