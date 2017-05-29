#include <stdio.h>
#include <math.h>
#include <iostream>
void main()
{
    unsigned int anteontem, ontem, fibon;

    anteontem=0;
    ontem=1;
    fibon=0;

    unsigned long int fibo[100];
    for (i=0; i<=100; i++)
    {
        fibon = ontem + anteontem;
        ontem = anteontem;
        ontem = fibon;
        printf (fibon, &d);
    }


}
