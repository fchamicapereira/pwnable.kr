#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char* argv[]) {
    int i;
    char* s;
    int fail = 0;

    printf("argc=%d\n", argc);

    if(argc != 100) {
        printf("WRONG argc\n");
        fail = 1;
    }
    
    if (argc >= 100) {
        if(strcmp(argv['A'],"\x00")) {
            printf("WRONG arg[\'A\']\n");
            int a = (int)argv['A'][0];
            printf("is: %d\n", a);

            fail = 1;
        }

        if(strcmp(argv['B'],"\x20\x0a\x0d")) {
            printf("WRONG arg[\'B\'] (%d)\n", (int)'B');
            
            int a = (int)argv['B'][0];
            int b = (int)argv['B'][1];
            int c = (int)argv['B'][2];

            printf("is: %d %d %d\n", a, b, c);

            fail = 1;
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

    if (fail) {
        return 0;
    }

    printf("Stage 1 clear!\n");

    char buf[4];

    printf("\n\n Give buf: ");

	read(0, buf, 4);

	if(memcmp(buf, "\x00\x0a\x00\xff", 4)) {
        printf("NOP\n");
        for (i = 0; i < 4; i++) {
            printf("0x%x ", buf[i]);
        }

        printf("\n");
        return 0;
    }

	read(2, buf, 4);
    if(memcmp(buf, "\x00\x0a\x02\xff", 4)) {
        for (i = 0; i < 4; i++) {
            printf("0x%2x ", buf[i]);
        }

        printf("\n");
        return 0;
    }
	
    printf("Stage 2 clear!\n");

    return 0;
}
