
# Disassemble

```
(fcn) sym.do_brainfuck 149
|   sym.do_brainfuck (int arg_8h);
|           ; var char intruction_char @ ebp-0xc
|           ; arg int arg_8h @ ebp+0x8
|           0x080485dc      push ebp
|           0x080485dd      mov ebp, esp
|           0x080485df      push ebx
|           0x080485e0      sub esp, 0x24 ; '$'
|           0x080485e3      mov eax, dword [arg_8h] ; [0x8:4]=-1 ; 8
|           0x080485e6      mov byte [intruction_char], al
|           0x080485e9      movsx eax, byte [intruction_char]
|           0x080485ed      sub eax, 0x2b ; '+'
|           0x080485f0      cmp eax, 0x30 ; '0' ; 48
|       ,=< 0x080485f3      ja 0x804866b
|       |   0x080485f5      mov eax, dword [eax*4 + 0x8048848] ; [0x8048848:4]=0x804861c
|       |   0x080485fc      jmp eax ; switch table (49 cases) at 0x8048848
|       |   0x080485fe      mov eax, dword [obj.p] ; [0x804a080:4]=0 ; case '>'
|       |   0x08048603      add eax, 1
|       |   0x08048606      mov dword [obj.p], eax ; [0x804a080:4]=0
|      ,==< 0x0804860b      jmp 0x804866b
|      ||   0x0804860d      mov eax, dword [obj.p] ; [0x804a080:4]=0 ; case '<'
|      ||   0x08048612      sub eax, 1
|      ||   0x08048615      mov dword [obj.p], eax ; [0x804a080:4]=0
|     ,===< 0x0804861a      jmp 0x804866b
|     |||   0x0804861c      mov eax, dword [obj.p] ; [0x804a080:4]=0 ; case '+'
|     |||   0x08048621      movzx edx, byte [eax]
|     |||   0x08048624      add edx, 1
|     |||   0x08048627      mov byte [eax], dl
|    ,====< 0x08048629      jmp 0x804866b
|    ||||   0x0804862b      mov eax, dword [obj.p] ; [0x804a080:4]=0 ; case '-'
|    ||||   0x08048630      movzx edx, byte [eax]
|    ||||   0x08048633      sub edx, 1
|    ||||   0x08048636      mov byte [eax], dl
|   ,=====< 0x08048638      jmp 0x804866b
|   |||||   0x0804863a      mov eax, dword [obj.p] ; [0x804a080:4]=0 ; case '.'
|   |||||   0x0804863f      movzx eax, byte [eax]
|   |||||   0x08048642      movsx eax, al
|   |||||   0x08048645      mov dword [esp], eax ; int c
|   |||||   0x08048648      call sym.imp.putchar ; int putchar(int c)
|  ,======< 0x0804864d      jmp 0x804866b
|  ||||||   0x0804864f      mov ebx, dword [obj.p] ; [0x804a080:4]=0 ; case ','
|  ||||||   0x08048655      call sym.imp.getchar ; int getchar(void)
|  ||||||   0x0804865a      mov byte [ebx], al
| ,=======< 0x0804865c      jmp 0x804866b
| |||||||   0x0804865e      mov dword [esp], str.and___not_supported. ; [0x8048830:4]=0x6e61205b ; "[ and ] not supported." ; const char *s ; [
| |||||||   0x08048665      call sym.imp.puts ; int puts(const char *s)
| |||||||   0x0804866a      nop
| ```````-> 0x0804866b      add esp, 0x24 ; '$'
|           0x0804866e      pop ebx
|           0x0804866f      pop ebp
\           0x08048670      ret
```

# binary info

## Headers

```
$ readelf -S bf
There are 30 section headers, starting at offset 0x116c:

Section Headers:
  [Nr] Name              Type            Addr     Off    Size   ES Flg Lk Inf Al
  [ 0]                   NULL            00000000 000000 000000 00      0   0  0
  [ 1] .interp           PROGBITS        08048154 000154 000013 00   A  0   0  1
  [ 2] .note.ABI-tag     NOTE            08048168 000168 000020 00   A  0   0  4
  [ 3] .note.gnu.build-i NOTE            08048188 000188 000024 00   A  0   0  4
  [ 4] .gnu.hash         GNU_HASH        080481ac 0001ac 00002c 04   A  5   0  4
  [ 5] .dynsym           DYNSYM          080481d8 0001d8 0000e0 10   A  6   1  4
  [ 6] .dynstr           STRTAB          080482b8 0002b8 00009e 00   A  0   0  1
  [ 7] .gnu.version      VERSYM          08048356 000356 00001c 02   A  5   0  2
  [ 8] .gnu.version_r    VERNEED         08048374 000374 000030 00   A  6   1  4
  [ 9] .rel.dyn          REL             080483a4 0003a4 000018 08   A  5   0  4
  [10] .rel.plt          REL             080483bc 0003bc 000050 08   A  5  12  4
  [11] .init             PROGBITS        0804840c 00040c 000023 00  AX  0   0  4
  [12] .plt              PROGBITS        08048430 000430 0000b0 04  AX  0   0 16
  [13] .text             PROGBITS        080484e0 0004e0 000334 00  AX  0   0 16
  [14] .fini             PROGBITS        08048814 000814 000014 00  AX  0   0  4
  [15] .rodata           PROGBITS        08048828 000828 000138 00   A  0   0  4
  [16] .eh_frame_hdr     PROGBITS        08048960 000960 000034 00   A  0   0  4
  [17] .eh_frame         PROGBITS        08048994 000994 0000d8 00   A  0   0  4
  [18] .init_array       INIT_ARRAY      08049f08 000f08 000004 00  WA  0   0  4
  [19] .fini_array       FINI_ARRAY      08049f0c 000f0c 000004 00  WA  0   0  4
  [20] .jcr              PROGBITS        08049f10 000f10 000004 00  WA  0   0  4
  [21] .dynamic          DYNAMIC         08049f14 000f14 0000e8 08  WA  6   0  4
  [22] .got              PROGBITS        08049ffc 000ffc 000004 04  WA  0   0  4
  [23] .got.plt          PROGBITS        0804a000 001000 000034 04  WA  0   0  4
  [24] .data             PROGBITS        0804a034 001034 000008 00  WA  0   0  4
  [25] .bss              NOBITS          0804a040 00103c 000460 00  WA  0   0 32
  [26] .comment          PROGBITS        00000000 00103c 00002a 01  MS  0   0  1
  [27] .shstrtab         STRTAB          00000000 001066 000106 00      0   0  1
  [28] .symtab           SYMTAB          00000000 00161c 0004f0 10     29  47  4
  [29] .strtab           STRTAB          00000000 001b0c 000315 00      0   0  1
```

## Relocations

```
$ readelf -r bf

Relocation section '.rel.dyn' at offset 0x3a4 contains 3 entries:
 Offset     Info    Type            Sym.Value  Sym. Name
08049ffc  00000506 R_386_GLOB_DAT    00000000   __gmon_start__
0804a040  00000d05 R_386_COPY        0804a040   stdin@GLIBC_2.0
0804a060  00000b05 R_386_COPY        0804a060   stdout@GLIBC_2.0

Relocation section '.rel.plt' at offset 0x3bc contains 10 entries:
 Offset     Info    Type            Sym.Value  Sym. Name
0804a00c  00000107 R_386_JUMP_SLOT   00000000   getchar@GLIBC_2.0
0804a010  00000207 R_386_JUMP_SLOT   00000000   fgets@GLIBC_2.0
0804a014  00000307 R_386_JUMP_SLOT   00000000   __stack_chk_fail@GLIBC_2.4
0804a018  00000407 R_386_JUMP_SLOT   00000000   puts@GLIBC_2.0
0804a01c  00000507 R_386_JUMP_SLOT   00000000   __gmon_start__
0804a020  00000607 R_386_JUMP_SLOT   00000000   strlen@GLIBC_2.0
0804a024  00000707 R_386_JUMP_SLOT   00000000   __libc_start_main@GLIBC_2.0
0804a028  00000807 R_386_JUMP_SLOT   00000000   setvbuf@GLIBC_2.0
0804a02c  00000907 R_386_JUMP_SLOT   00000000   memset@GLIBC_2.0
0804a030  00000a07 R_386_JUMP_SLOT   00000000   putchar@GLIBC_2.0
```

# Execution examples

```
$ ./bf
[out] welcome to brainfuck testing system!!
[out] type some brainfuck instructions except [ ]
[in]  ,.,.,.,.,.
[in]  hello
[out] hello
```

```
$ ./bf
[out] welcome to brainfuck testing system!!
[out] type some brainfuck instructions except [ ]
[in]  ,-.
[in]  b
[out] a
```

```
$ ./bf
[out] welcome to brainfuck testing system!!
[out] type some brainfuck instructions except [ ]
[in]  ,+++.
[in]  a
[out] d
```

# Reverse engineered

- max number of instruction = 512
- instructions:
    - `,` read char from stdin and stores in *p
    - `.` outputs *p to stdout
    - `<` subtract 1 to p
    - `>` add 1 to p
    - `+` add 1 to *p
    - `-` subtract 1 to *p

Plan:

- overwrite putchar@got -> _start
- overwrite fgets@got -> system
- overwrite memset@got -> gets