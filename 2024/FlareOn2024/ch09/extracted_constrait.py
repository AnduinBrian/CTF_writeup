
input = b"this_is_test_string_for_challeng"

def check1(data):
    result = data[4] * 0xef7a8c
    result = result + 0x9d865d8d
    result = result - (data[24] * 0x45b53c)
    result = result + 0x18baee57
    result = result - (data[0] * 0xe4cf8b)
    result = result + 0xffffffff6ec04422
    result = result - (data[8] * 0xf5c990)
    result = result + 0x6bfaa656
    result = result ^ (data[20] * 0x733178)
    result = result ^ 0x61e3db3b
    result = result ^ (data[16] * 0x9a17b8)
    result = result + 0xFFFFFFFF35D7FB4F
    result = result ^ (data[12] * 0x773850)
    result = result ^ 0x5a6f68be
    result = result ^ (data[28] * 0xe21d3d)
    result = result ^ 0x5c911d23
    result = result + 0x7e9b8587
    result &= 0xFFFFFFFFFFFFFFFF
    return result  #must be zero

def check2(data):
    result = 0
    return result

print(hex(check2(input)))