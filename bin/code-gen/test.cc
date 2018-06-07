#include <stdio.h>
#include "test.h"

extern "C" int DLLEXPORT hello(char* name)
{
  printf("Hello\n");
}


