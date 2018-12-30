## key1
- R3 <= pc = 0x00008cdc
- return 0x00008cdc

## key2
- R6 <= pc + 1 = 0x00008cfc + 1 = 0x00008cfd
- R3 <= pc + 4 = 0x00008d08
- return 0x00008d08

## key3
- R3 <= lr = 0x00008d80
- return 0x00008d80

## main
- from key1
  - R0 <= 0x00008cdc
  - R4 <= 0x00008cdc
- from key2
  - R0 <= 
  - R3 <= 
  - R4 <= 0x00008cdc
  - R4 <= R3 + R4 = 
