#include <stdio.h>
using namespace std;		
		
int main() {		
  int a=0,b=0,c=0;

  printf("Enter the First Number: ");
  scanf("%d",&a);
  printf("Enter the Second Number: ");
  scanf("%d",&b);
  printf("Enter the Third Number: ");
  scanf("%d",&c);

  float avg = (a+b+c)/3.0F;
	printf("Average: %f",avg);
	
  return 0;	
}		