#include <stdio.h>
#include <stdlib.h>

int max(int a, int b){return a > b ? a : b;}
int min(int a, int b){return a < b ? a : b;}

int minim_vector(int v[100], int n)
{
    int Min = v[0];
    for(int i = 0; i < n; i ++)
        Min = min(Min, v[i]);
    return Min;
}

int pos_maxim_vector(int v[100], int n)
{
    int Max = v[0], pos_max = 0;
    for(int i = 0; i < n; i ++)
        if(Max < v[i])
        {
            Max = v[i];
            pos_max = i;
        }

    return pos_max;
}

double media_aritmetica(int v[100], int n)
{
    double s = 0;
    for(int  i = 0; i < n; i ++)
        s += v[i];
    return s/n;
}

int mmc_media_aritmetica(int v[100], int n, double media_aritmetica)
{
    int cnt = 0;
    for(int i = 0; i < n; i ++)
        if(v[i] > media_aritmetica)
            cnt ++;
    return cnt;
}

int main()
{
    int n;
    int v[100] = {0};
    scanf("%d", &n);
    for(int i = 0; i < n; i ++)
    {
        int nr;
        scanf("%d", &nr);
        v[i] = nr;
    }

    printf("min = %d\npoz_max = %d\nma = %.2lf\ngt_ma = %d", minim_vector(v, n), pos_maxim_vector(v, n), media_aritmetica(v, n), mmc_media_aritmetica(v, n, media_aritmetica(v, n)));

    return 0;
}
