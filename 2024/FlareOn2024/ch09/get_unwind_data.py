import string

registry = {
    0 : "rax",
    1 : "rcx",
    2 : "rdx",
    3 : "rbx",
    4 : "rsp",
    5 : "rbp",
    6 : "rsi",
    7 : "rdi",
    8 : "r8",
    9 : "r9",
    10 : "r10",
    11 : "r11",
    12 : "r12",
    13 : "r13",
    14 : "r14",
    15 : "r15",
}


def parse_unwind(start_addr, unwin_code_len):
    unwind_start_ea = start_addr
    tmp = unwin_code_len * 2
    end_addr = start_addr + tmp
    while(unwind_start_ea <= end_addr):
        unwind_code_data = get_bytes(unwind_start_ea, 2)
        offset_prolog = unwind_code_data[0]
        unwind_op_code = unwind_code_data[1] & 0xf
        unwind_op_info = unwind_code_data[1] >> 4 & 0xf
        if unwind_op_code == 1:
            if unwind_op_info == 1:
                unwind_start_ea += 2
                print("UWOP_ALLOC_LARGE - OpInfo: %d" % unwind_op_info)
                frame_offset_1 = int.from_bytes(get_bytes(unwind_start_ea, 2), "little")
                unwind_start_ea += 2
                frame_offset_2 = int.from_bytes(get_bytes(unwind_start_ea, 2), "little")
                frame_off = (frame_offset_2 << 16) + frame_offset_1
                print("  Context.RSP += %d" % frame_off)

            elif unwind_op_info == 0:
                print("UWOP_ALLOC_LARGE - OpInfo: %d" % unwind_op_info)
                unwind_start_ea += 2
                frame_offset_1 = int.from_bytes(get_bytes(unwind_start_ea, 2), "little")
                frame_off = frame_offset_1 * 8
                print("  Context.RSP += 0x%x" % frame_off)

        elif unwind_op_code == 10:
            print("UWOP_PUSH_MACHFRAME")
            print("  Context.RIP = [Context.RSP]")
            print("  Context.RSP = [Context.RSP + 0x18]")

        elif unwind_op_code == 0:
            print("UWOP_PUSH_NONVOL")
            print("  Context.%s = [Context.RSP]" % (registry[unwind_op_info].upper()))

        elif unwind_op_code == 3:
            temp = get_bytes(start_addr - 1, 1)[0]
            frame_reg = temp & 0xf
            frame_offset = (temp >> 4 & 0xf)
            print("UWOP_SET_FPREG - %s" % registry[frame_reg])
            print("  Context.RSP = %s" % registry[frame_reg])
            print("  Context.RSP -= %d" % (frame_offset * 16))

        elif unwind_op_code == 2:
            print("UWOP_ALLOC_SMALL - OpInfo: %d" % unwind_op_info)
            print("  Context.RSP += 0x%x" % ((unwind_op_info * 8) + 8))

        unwind_start_ea += 2

    if unwin_code_len %2 != 0:
        end_addr = end_addr + 2
    except_handler = int.from_bytes(get_bytes(end_addr, 4), "little")
    print("NO MORE UNWIND CODE")
    print("  Handler: 0x%x" % except_handler)


def get_unwind(start_addr):
    ver_n_flag = get_bytes(start_addr, 1)
    size_of_prolog = get_bytes(start_addr + 1, 1)
    count_unwind_code = get_bytes(start_addr + 2,1)
    count_unwind_code = int.from_bytes(count_unwind_code, "little")
    if count_unwind_code == 0:
        handler = get_bytes(start_addr + 4, 4)
        exceptiona_ddr = int.from_bytes(handler, "little")
        print("NO UNWIND_CODE")
        print("  Handler: 0x%x" % exceptiona_ddr)
    else:
        parse_unwind(start_addr + 4, count_unwind_code)

with open("9/unwind_and_handler/round_17_unwind","r") as file:
    unwind_count = 1
    for i in file:
        startEA = int(i.strip(), 16)
        print("====== UNWIND %d - 0x%x ======" % (unwind_count, startEA))
        get_unwind(startEA)
        unwind_count += 1
        print("")
