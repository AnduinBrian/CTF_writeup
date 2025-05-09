import crcmod

polynomial = 0x2f
initial_value = 0xff

crc = crcmod.mkCrcFun(
    poly=0x100 + polynomial,
    initCrc=initial_value,
    rev=False,
)

for i in range(0, 255):
    payload = b"\x00\x03\x00"
    data = payload + i.to_bytes(1, 'little')
    checksum = crc(data) ^ 0xff
    if checksum == 0x74:
        secret = i

print("Found secret: %d" % secret)

payload = b"\x0f\x03\x00" + secret.to_bytes(1, 'little')
checksum = crc(payload) ^ 0xff
print("FLAG: CTF{%2X}" % checksum)

