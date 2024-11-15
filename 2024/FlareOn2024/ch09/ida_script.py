addr_count = 0

def call_process(addr):
    call_insn = DecodeInstruction(addr)
    ret_addr = call_insn.ip + call_insn.size

    pop_insn = DecodeInstruction(call_insn.ops[0].addr)
    patch_qword(pop_insn.ops[0].addr, ret_addr)

    mov_byte_insn = DecodeInstruction(pop_insn.ip + 0xe)
    tmp = get_bytes(mov_byte_insn.ops[1].addr, 1)
    tmp = struct.unpack("<B", tmp)[0]
    tmp = tmp << 8
    
    lea_insn = DecodeInstruction(mov_byte_insn.ip + mov_byte_insn.size)
    patch_byte = (lea_insn.ops[1].addr + tmp) & 0xffffffff
    
    mov_insn = DecodeInstruction(lea_insn.ip + lea_insn.size)
    patch_dword(mov_insn.ops[0].addr, patch_byte)

    create_insn(mov_insn.ops[0].addr)
    created_insn = DecodeInstruction(mov_insn.ops[0].addr)
    if created_insn.itype != 0x56:
        temp_addr = created_insn.ip + created_insn.size
        next_insn = 0
        while(1):
            create_insn(temp_addr)
            next_insn = DecodeInstruction(temp_addr)
            if next_insn.itype == 0x5c:
                break
            else:
                temp_addr = next_insn.ip + next_insn.size
        next_insn = next_insn.ops[1].addr + ret_addr
        return next_insn

    return 0

def main_process(start_addr):
    addr = start_addr
    count = 0
    while(1):
        create_insn(addr)
        first_insn = DecodeInstruction(addr)
        if first_insn.itype == 0x10:
            print("insn: 0x%x" % first_insn.ip)
            addr = call_process(first_insn.ip)
            if addr == 0:
                print("\tjmp insn here")
                break

            count += 1
        else:
            addr += first_insn.size
        if count == 20:
            print("out scope")
            break

def get_instruction(addr):
    call_insn = DecodeInstruction(addr)
    inside_call = call_insn.ops[0].addr
    instr_size = 0
    data = b""
    while 1:
        instruction = DecodeInstruction(inside_call)
        if instruction.itype == 0x5c and instruction.ops[1].addr < 10:
            instr_size = instruction.ops[1].addr + 5
            break
        inside_call += instruction.size

    inside_call = call_insn.ops[0].addr
    while 1:
        instruction = DecodeInstruction(inside_call)
        if instruction.itype == 0x86 and instruction.ops[0].reg == 0:
            data = get_bytes(instruction.ip + instruction.size, instr_size)
            break
        inside_call += instruction.size
    return data

def patch_call_insn(addr, data):
    for i in range(len(data)):
        patch_byte(addr + i, data[i])

def patch_jmp(addr, next_addr):
    patch = b"\xe9"
    calculate = next_addr - (addr + 5) 
    print(calculate)
    byte_calc = struct.pack("<i", calculate)
    patch += byte_calc
    for i in range(len(patch)):
        patch_byte(addr + i, patch[i])

def patch_call(start_addr, addr_arr):
    global addr_count

    addr = start_addr
    count = 0
    while(1):
        create_insn(addr)
        first_insn = DecodeInstruction(addr)
        if first_insn.itype == 0x10:
            addr = call_process(first_insn.ip)
            if addr == 0:
                print("patch jmp here: 0x%x" % first_insn.ip)
                print(addr_count)
                patch_jmp(first_insn.ip, addr_arr[addr_count])
                addr_count += 1
                return 
            print(hex(first_insn.ip))
            data = get_instruction(first_insn.ip)
            patch_call_insn(first_insn.ip, data)
            count += 1
        else:
            addr += first_insn.size
        if count == 20:
            print("out scope")
            break
    

skip = 0
addr_arr = []
with open("9/unwind_and_handler/round_17_handler", "r") as file:
    for i in file:
        addr = int(i.strip(), 16)
        main_process(addr)
        if skip == 0:
            skip = 1
            continue
        else:
            addr_arr.append(int(i.strip(), 16))

with open("9/unwind_and_handler/round_17_handler", "r") as file:
    for i in file:
        addr = int(i.strip(), 16)
        patch_call(addr, addr_arr)
