import struct
import hexdump

def u32(v):
    return struct.unpack("<I", v)[0]

class c4tb_file_info_t():
    def __init__(self):
        pass

def read_c4tb(file):
    f = open(file, "rb")
    data = f.read()
    f.close()
    
    c4tb_file_info = c4tb_file_info_t()
    
    encrypt_content_size = u32(data[4:8])
    vm_ops_offset = u32(data[8:12])
    vm_ops_size = u32(data[12:16])
    
    c4tb_file_info.encrypt_content_size = encrypt_content_size
    c4tb_file_info.vm_ops_offset = vm_ops_offset
    c4tb_file_info.vm_ops_size = vm_ops_size
    c4tb_file_info.vm_ops = data[vm_ops_offset:vm_ops_offset + vm_ops_size]
    c4tb_file_info.encrypted_content = data[16:16 + encrypt_content_size]
    
    return c4tb_file_info

def print_c4tb_info(c4tb_file_info):
    print("c4tb_file_info.encrypt_content_size = 0x%X" % c4tb_file_info.encrypt_content_size)
    print("c4tb_file_info.vm_ops_offset = 0x%X" % c4tb_file_info.vm_ops_offset)
    print("c4tb_file_info.vm_ops_size = 0x%X" % c4tb_file_info.vm_ops_size)
    print("================================== VM OPS =====================================")
    hexdump.hexdump(c4tb_file_info.vm_ops)

def add_key_to_file_info(c4tb_file_info):
    vm_ops = list(c4tb_file_info.vm_ops)
    vm_ops[5] = 0x00
    vm_ops[4] = 0x11
    vm_ops[12] = 0x22
    vm_ops[11] = 0x33
    vm_ops[19] = 0x44
    vm_ops[18] = 0x55
    vm_ops[26] = 0x66
    vm_ops[25] = 0x77
    vm_ops[33] = 0x88
    vm_ops[32] = 0x99
    vm_ops[40] = 0xAA
    vm_ops[39] = 0xBB
    vm_ops[47] = 0xCC
    vm_ops[46] = 0xDD
    vm_ops[54] = 0xEE
    vm_ops[53] = 0xFF
    c4tb_file_info.vm_ops = bytes(vm_ops)
    return c4tb_file_info
    

def vm_disassemble(vm_ops):
    print("")
    print("================================== VM OPS FOR DISASSEMBLE =====================================")
    hexdump.hexdump(vm_ops)
    print("================================== VM DISASSEMBLE =====================================")
    ptr = 0
    while True:
        if vm_ops[ptr] == 1:
            print("0x%X: PUSH 0x%X" % (ptr, (vm_ops[ptr + 1] << 8) + vm_ops[ptr + 2]))
            ptr += 1
            ptr += 2
        elif vm_ops[ptr] == 5:
            print("0x%X: GET_MEM" % (ptr))
            ptr += 1
        elif vm_ops[ptr] == 6:
            print("0x%X: STORE_MEM" % (ptr))
            ptr += 1
        elif vm_ops[ptr] == 9:
            print("0x%X: ADD" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 13:
            print("0x%X: MUL" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 14:
            print("0x%X: JMP 0x%x" % (ptr, (vm_ops[ptr + 1] << 8) + vm_ops[ptr + 2]))
            ptr += 3
        elif vm_ops[ptr] == 16:
            addr = (vm_ops[ptr + 1] << 8) + vm_ops[ptr + 2]
            print("0x%X: JMP_NOT 0x%X" % (ptr, addr))
            ptr += 3
        elif vm_ops[ptr] == 17:
            print("0x%X: IS_EQUAL" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 18:
            # *(v7 - 1) < (unsigned __int64)*v7
            print("0x%X: IS_LOWER" % ptr) #???????????????????????????
            ptr += 1
        elif vm_ops[ptr] == 20:
            # *(v7 - 1) > (unsigned __int64)*v7;
            print("0x%X: IS_GREATER" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 25:
            print("0x%X: HLT" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 24:
            print("0x%X: OUT" % ptr)
            ptr += 1
            break
        elif vm_ops[ptr] == 27:
            print("0x%X: OR" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 28:
            print("0x%X: AND" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 30:
            print("0x%X: SHL" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 31:
            print("0x%X: SHR" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 36:
            print("0x%X: ROL8" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 37:
            print("0x%X: ROR8" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 29:
            print("0x%X: MOD" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 26:
            print("0x%X: XOR" % ptr)
            ptr += 1
        elif vm_ops[ptr] == 33:
            print("0x%X: ROR32" % ptr)
            ptr += 1

        else:
            print("0x%X: Unknown ops %d" % (ptr, vm_ops[ptr]))
            break

if __name__ == "__main__":
    c4tb_file_info = read_c4tb("disk/catmeme3.jpg.c4tb")
    print_c4tb_info(c4tb_file_info)
    c4tb_file_info = add_key_to_file_info(c4tb_file_info)
    vm_disassemble(c4tb_file_info.vm_ops)
