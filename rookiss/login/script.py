from pwn import *

context.clear(arch='i386', log_level='critical')

max_enc_len = 16
max_len = 12
wanted = 'f87cd601aa7fedca99018a8be88eda34'

# find md5
secret = ''
encode = ''
md5 = ''
secret_bytes = [0, 0, 0]
"""
while True:
    secret = struct.pack('<III', secret_bytes[0], secret_bytes[1], secret_bytes[2])

    # encode = b64e(secret)
    encode = secret
    md5 = md5sumhex(encode)

    if md5 == wanted:
        print 'FOUND', secret, encode, md5
        break

    secret_bytes[0] = (secret_bytes[0] + 1) % 0xffffffff

    if secret_bytes[0] & 0xffffff == 0x0:
        print 'secret', hex(secret_bytes[0]), hex(secret_bytes[1]), hex(secret_bytes[2])
    if secret_bytes[0] == 0x00000000:
        secret_bytes[1] = (secret_bytes[1] + 1 ) % 0xffffffff

        if secret_bytes[1] == 0x00000000:
            secret_bytes[2] = (secret_bytes[2] + 1 ) % 0xffffffff

            if secret_bytes[2] == 0x00000000:
                break
"""

def inc(values, index, max_length, max_value):
    carry = values[index] == (max_value - 1)
    values[index] = (values[index] + 1) % max_value
    if carry and index < max_length - 1:
        return inc(values, index + 1, max_length, max_value)
    if not carry and values[index] == 0:
        print 'len++'
    return values

def buildEncode(values, base64_table):
    chars = ''
    for v in values:
        if v != -1:
            chars += base64_table[v]
    return chars

secret = ''
base64_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
max_value = len(base64_table)
max_length = 12
values = [-1] * max_length
size = 0
while True:
    inc(values, 0, max_length, max_value)
    encode = buildEncode(values, base64_table)
    md5 = md5sumhex(encode)

    if md5 == wanted:
        print 'FOUND', secret, encode, md5
        break

    

p = process('./login')
p.recvuntil(': ')

if len(encode) > max_enc_len:
    print '[ERROR] Exceeded max input length ({0} len={1})'.format(encode, len(encode))
else:
    print 'sending {0} (len {1}) md5 {2}'.format(encode, len(encode), md5)

p.sendline(encode)
print p.recvline()

p.close()

