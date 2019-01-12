#include <stdio.h>

int main(int argc, char* argv[]) {
    char* p = argv[1];
    int i;
    int* ip = (int*)p;

    printf("p = %s\n", p);

    for(i = 0; i < 5; i++) {
        printf("\ni    = %d\n", i);
        printf("p[i] = %c\n", p[i]);
        printf("ip[i] = %d\n", ip[i]);
    }
}