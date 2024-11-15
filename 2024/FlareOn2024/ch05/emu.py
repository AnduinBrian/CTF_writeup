from unicorn import *
from unicorn.x86_const import *
from capstone import *
from capstone.x86 import *

mu = Uc(UC_ARCH_X86, UC_MODE_64)
mu.mem_map(0, 0x1000)
mu.mem_map(0x5000, 0x10000)

mu.mem_write(0, open("shellcode", "rb").read())

mu.reg_write(UC_X86_REG_RBP, 0x7500)
mu.reg_write(UC_X86_REG_RSP, 0x7000)


encrypted = 0x7500 - 0x1148
key = 0x7500 - 0x1278
iv = 0x7500 - 0x1258

mu.mem_write(key, b'\x8d\xec\x91\x12\xeb\x76\x0e\xda\x7c\x7d\x87\xa4\x43\x27\x1c\x35\xd9\xe0\xcb\x87\x89\x93\xb4\xd9\x04\xae\xf9\x34\xfa\x21\x66\xd7')
mu.mem_write(iv, b'\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11\x11')
mu.mem_write(encrypted, b'\xA9\xF6\x34\x08\x42\x2A\x9E\x1C\x0C\x03\xA8\x08\x94\x70\xBB\x8D\xAA\xDC\x6D\x7B\x24\xFF\x7F\x24\x7C\xDA\x83\x9E\x92\xF7\x07\x1D')

mu.emu_start(0x00000 + 0xe7f, 0x00000 + 0xecf)

print(mu.mem_read(encrypted, 0x80))
