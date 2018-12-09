#include <stdio.h>
#include <string.h>

void debug(char* s) {
    
}

int main(int argc, char* argv[]) {
    int i;
    char* s;
    printf("argc=%d\n", argc);

    if(argc != 100) {
        printf("WRONG argc\n");
    }
    
    if (argc >= 100) {
        if(strcmp(argv['A'],"\x00")) {
            printf("WRONG arg[\'A\']\n");
            int a = (int)argv['A'][0];
            printf("is: %d\n", a);
        }

        if(strcmp(argv['B'],"\x20\x0a\x0d")) {
            printf("WRONG arg[\'B\'] (%d)\n", (int)'B');
            
            int a = (int)argv['B'][0];
            int b = (int)argv['B'][1];
            int c = (int)argv['B'][2];

            printf("is: %d %d %d\n", a, b, c);

        }
    }

    for (i = 0; i < argc; i++) {
        s = argv[i];

        printf("argv[%d]=", i);
        
        while (*s != 0x0) {
            printf("0x%2x ", *s);
            s += 1;
        }

        printf(" (%s)\n", argv[i]);
    }

    return 0;
}
