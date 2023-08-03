#include<stdio.h>(c  program)
void toBinary(int N)
{
    // your code here
    int s[32],i=0,a=0;
    while(N>=1)
    {
      s[i]=(N%2);
      N=N/2;
      i++;
      a=i;
    }  
    for(int j=a-1;j>=0;j--)
    {
        printf("%d",s[j]);
    }
    }
