#include <stdio.h>

int main(void) {
	// your code goes here
	int n=0,x=0,i,value=0;
	scanf("%d",&n);
	int arr[n];
	for (i=0;i<n;i++)
	{
	    scanf("%d",&arr[i]);
	}
	scanf("%d",&x);
	for(i=0;i<n;i++)
	{
	    if(arr[i]=x)
	    {
	    value++;
	}
	}
	if(value<=1)
	{
	    printf("YES");
	}
	else
	{
	    printf("NO");
	}
	return 0;
}

