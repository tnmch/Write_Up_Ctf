#we dont know about the update of values :(
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#ifdef __APPLE__
#include <OpenCL/opencl.h>
#else
#include <CL/cl.h>
#endif
 
#define MAX_SOURCE_SIZE (0x100000)

typedef unsigned long __uint64;
__uint64 modpow(__uint64 a, __uint64 b) {
//Source : https://github.com/pantaloons/RSA/blob/master/single.c
 __uint64 res = 1;
 while(b > 0) {
  if(b & 1) {
   res = (res * a);
  }
  b = b >> 1;
  a = (a * a);
 }
 return res;
}

int main()
{
    unsigned long long var_8 = 0;
    unsigned long long i;
    unsigned long long v4, v3, v2, v1, v5;
for ( i = 0LL; i <= 1193046; ++i )
  {
    v4 = i / 41LL;
    v3 = modpow(3LL, v4);
    v2 = v3 + v5;
    v1 = v2 * i;
    v5 = v1 % 1836457930599072000LL;
  }
    printf("hackfest{%04llx%04llx%04llx%04llx%04llx}\n", v5, v1, v2, v3, v4);

    return 0;
}

