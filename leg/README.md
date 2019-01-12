## key1
- R3 <= pc = 0x00008ce4
- return 0x00008ce4

- 

## key2
- R3 <= pc + 4 = 0x00008d08 + 4 = 0x00008d0c
- return 0x00008d0c

## key3
- R3 <= lr = 0x00008d80
- return 0x00008d80

## main
0x00008ce4 + 0x00008d0c + 0x00008d80 = 0x0001a770 (108400)
