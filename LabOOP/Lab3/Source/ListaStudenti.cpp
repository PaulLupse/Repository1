# include "ListaStudenti.h"

ListaStudenti::ListaStudenti(const ListaStudenti & other):varf(other.varf), baza(other.baza), nrNoduri(other.nrNoduri) {

};

void ListaStudenti::adauga(Student * student) {
    if (varf == nullptr) {
        varf = new Nod(student);
        prev = varf;
    }
}

ostream& operator<<(ostream& out_stream, const ListaStudenti::Nod& nod) {
    out_stream << nod.date << "\n";
    return out_stream;
}