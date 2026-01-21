#include <bits/stdc++.h>

using namespace std;

ifstream fin("roy-floyd.in");
ofstream fout("roy-floyd.out");

int ad[105][105], n, m;

void AfisMat()
{
    for(int i = 1; i <= n; i ++)
    {
        for(int j = 1; j <= n; j ++)
            cout << ad[i][j] << " ";
        cout << '\n';
    }

}

void RF()
{
    for(int k = 1; k <= n; k ++)
        for(int i = 1; i <= n; i ++)
            for(int j = 1; j <= n; j ++)
                if(ad[i][j] > ad[i][k] + ad[k][j])
                    ad[i][j] = ad[i][k] + ad[k][j];
}

int main()
{
    int x, y, p;
    fin >> n >> m;
    for(int i = 1; i <= m; i++){fin >> x >> y >> p; ad[x][y] = p; }
    for(int i = 1; i <= n; i ++)
    {
        for(int j = 1; j <= n; j ++)
            if(ad[i][j] == 0) ad[i][j] = 1000000000;
        ad[i][i] = 0;
    }
    //AfisMat();
    RF();
    for(int i = 1; i <= n; i ++)
    {
        for(int j = 1; j <= n; j ++)
            if(ad[i][j] == 1000000000) ad[i][j] = -1;
        ad[i][i] = 0;
    }
    AfisMat();

    return 0;
}