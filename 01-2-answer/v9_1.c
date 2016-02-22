#include <u.h>

char read() {
    asm(LI, 0);
    asm(BIN);
}

write(char x) {
    asm(LBL, 8);
    asm(LI, 1);
    asm(BOUT);
}

char x = -1, g;
main()
{
    g = 0;
    while(1) {
        if (g == 0) {
            g = 1;
        }
        x = read();
        if (x != -1) {
            g = 0;
            write(x);
            write('\n');
            asm(HALT);
        }
    }
    asm(HALT);
}
