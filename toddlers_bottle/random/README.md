The  rand()  function  returns a pseudo-random integer in the range 0 to RAND_MAX inclusive

Signature:
```
int rand(void);
```

RAND_MAX = 2147483647

- using rand without seed always gives out the same number (0x6b8b4567)

```
0x6b8b4567 ^ 0xdeadbeef = 0xb526fb88 <=> 0x6b8b4567 ^ 0xb526fb88 = 0xdeadbeef
0xb526fb88 = 3039230856
```

- give 3039230856 in input