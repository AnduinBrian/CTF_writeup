from Crypto.Cipher import ChaCha20

with open("coredump", "rb") as file:
    data = file.read()

    shell_ptr = data.find(b"\x0f\xb0\x35\x4e")
    print(f"[*] Located shellcode: {hex(shell_ptr)}")
    shellcode = data[shell_ptr:shell_ptr + 0xF96]

    buff = data.find(b"\x48\x7a\x40\xc5")
    print(f"[*] Found ptr: {hex(buff)}")
    key = data[buff + 4: buff + 4 + 32]
    iv = data[buff + 4 + 32: buff + 4 + 32 + 12]
    print(f"[*] Key: {key}")
    print(f"[*] IV: {iv}")

    cipher = ChaCha20.new(key=key, nonce=iv)
    dec = cipher.decrypt(shellcode)
    
    with open("shellcode", "wb") as file:
        file.write(dec)
    
    print("[*] shellcode extracted !!")