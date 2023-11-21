#include <stdio.h>
#include <strings.h>

int main()
{
  char s[100000];
  scanf("%s", s);

  int count = strlen(s);

  printf("%d\n", count);
}
