#include <stdio.h>
#include <stdlib.h>

struct nr_mare{ //structura reprezentad un numar mare, cu maxim 10000 de cifre si lungime l
    int val[10000];
    int l;
};

struct nr_mare max(struct nr_mare nr1, struct nr_mare nr2)
{
    if(nr1.l > nr2.l)
        return nr1;
    else if(nr1.l < nr2.l)
        return nr2;
    for(int i = nr1.l - 1; i >= 0; i--)
    {
        if(nr1.val[i] > nr2.val[i])
            return nr1;
        else if(nr1.val[i] < nr2.val[i])
            return nr2;
    }
    return nr1;
};

struct nr_mare min(struct nr_mare nr1, struct nr_mare nr2)
{
    if(nr1.l < nr2.l)
        return nr1;
    else if(nr1.l > nr2.l)
        return nr2;
    for(int i = nr1.l - 1; i >= 0; i--)
    {
        if(nr1.val[i] < nr2.val[i])
            return nr1;
        else if(nr1.val[i] > nr2.val[i])
            return nr2;
    }
    return nr1;
};

void print_nr_mare(struct nr_mare nr)
{
    for(int i = 0; i < nr.l; i ++)
        printf("%d", nr.val[nr.l - i - 1]);
}

struct nr_mare adunare(struct nr_mare nr1, struct nr_mare nr2)
{
    struct nr_mare nr = {{0}, 0};
    if(nr1.l < nr2.l)
    {
        struct nr_mare aux;
        aux = nr1;
        nr1 = nr2;
        nr2 = aux;
    }

    int carry = 0;
    for(int i = 0; i < nr2.l; i ++)
    {
        nr.val[i] = (nr1.val[i] + nr2.val[i] + carry) % 10;
        carry = (nr1.val[i] + nr2.val[i]) / 10;
        nr.l ++;
    }
    for(int i = nr2.l; i < nr1.l; i ++)
    {
        nr.val[i] = (nr1.val[i] + carry) % 10;
        carry = (nr1.val[i] + carry) / 10;
        nr.l ++;
    }
    if(carry)
    {
        nr.val[nr.l] = carry;
        nr.l ++;
    }

    return nr;
}

void cauta_imprumut(struct nr_mare *nr, int pos)
{
    if((nr -> val)[pos])
       (nr -> val)[pos] -= 1;
    else
    {
        pos ++;
        cauta_imprumut(nr, pos);
        pos --;
        (nr -> val)[pos] = 9;
    }
}

struct nr_mare scadere(struct nr_mare nr1, struct nr_mare nr2)
{
    struct nr_mare nra = max(nr1, nr2);
    struct nr_mare nrb = min(nr1, nr2);

    nr1 = nra;
    nr2 = nrb;

    for(int i = 0; i < nr2.l; i ++)
    {
        if(nr1.val[i] >= nr2.val[i])
            nr1.val[i] -= nr2.val[i];
        else
        {
            cauta_imprumut(&nr1, i + 1);
            nr1.val[i] = nr1.val[i] + 10 - nr2.val[i];
        }
    }
    int i = nr1.l - 1;
    while(nr1.val[i] == 0 && i > 0)
    {
        nr1.l --;
        i --;
    }
    return nr1;
}

struct nr_mare inmultire(struct nr_mare nr1, int nr2)
{
    int carry = 0;
    for(int i = 0; i < nr1.l; i ++)
    {
        nr1.val[i] = (nr1.val[i] * nr2) % 10;
        nr1.val[i] += carry;
        carry = (nr1.val[i] * nr2) / 10;
    }
    return nr1;
}

int main()
{
    struct nr_mare a = {{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1}, 126};
    struct nr_mare b = {{9}, 1};
    struct nr_mare nr = adunare(a, b);

    print_nr_mare(adunare(b, a)); printf("\n");
    print_nr_mare(scadere(b, a)); printf("\n");
    print_nr_mare(inmultire(a, 9));
    return 0;
}
