import struct
import sys

def check_sum(bytes_arr):
    checksum = 0
    for i in bytes_arr[:-1]:
        checksum ^= i
    
    return checksum

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Give me packet !!")
        exit(0)
    else:
        packet_hex = bytearray.fromhex(sys.argv[1])
        print("\n[+] Packet bytes:\n")
        for i in packet_hex:
            print("| %02X " % i, end="")
        print("|\n")

        ret = check_sum(packet_hex)
        if ret == packet_hex[-1]:
            print("[+] Parsed data:")

            sync = int.from_bytes(packet_hex[:2], byteorder='big')
            print("  [-] SYNC: 0x%x" % sync)
            
            keyfob_id = packet_hex[2:6]
            keyfob_id = struct.unpack(">I", keyfob_id)[0]
            print("  [-] UID: 0x%x" % keyfob_id)

            button = packet_hex[6] >> 4 & 0xf
            print("  [-] Button: 0x%x" % button)

            counter = packet_hex[6] & 0xf
            counter = counter << 6
            counter += packet_hex[7] >> 2
            print("  [-] Counter: 0x%x" % counter)

            secret = int.from_bytes(packet_hex[8:12], byteorder='big')
            secret = secret >> 2
            secret += (packet_hex[7] & 0x3) << 30            
            print("  [-] keystream: 0x%x" % secret)

            print("  [-] Checksum bytes: 0x%x" % packet_hex[-1])

            print("[!] Flag part 1: CTF{%x}" % keyfob_id)
            print("\n[+] Part 2")

            iv = counter << 4 
            iv += button
            print("  [-] IV: 0x%08x" %iv)

            inver_ks = secret ^ 0xffffffff
            print("  [-] secret: 0x%08x" % inver_ks)
        else:
            print("[?] Wrong checksum: should be %2X - but got %2X" % (packet_hex[-1], ret))
        
        