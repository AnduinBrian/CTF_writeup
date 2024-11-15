from sage.all import *
from sage.all import EllipticCurve, Zmod, factor, Factorization
from scapy.all import rdpcap, Raw
from Crypto.Cipher import ChaCha20
import hashlib
import base64

q = 0xc90102faa48f18b5eac1f76bb40a1b9fb0d841712bbe3e5576a7a56976c2baeca47809765283aa078583e1e65172a3fd
a = 0xa079db08ea2470350c182487b50f7707dd46a58a1d160ff79297dcc9bfad6cfc96a81c4a97564118a40331fe0fc1327f
b = 0x9f939c02a7bd7fc263a4cce416f4c575f28d0c1315c4f0c282fca6709a5f9f7f9c251c9eede9eb1baa31602167fa5380

x = 0x087b5fe3ae6dcfb0e074b40f6208c8f6de4f4f0679d6933796d3b9bd659704fb85452f041fff14cf0e9aa7e45544f9d8
y = 0x127425c1d330ed537663e87459eaa1b1b53edfe305f6a79b184b3180033aab190eb9aa003e02e9dbf6d593c5e3b08182

E = EllipticCurve(GF(q), [a, b])

G = E(x, y)

client_P = E(0x195b46a760ed5a425dadcab37945867056d3e1a50124fffab78651193cea7758d4d590bed4f5f62d4a291270f1dcf499, 0x357731edebf0745d081033a668b58aaa51fa0b4fc02cd64c7e8668a016f0ec1317fcac24d8ec9f3e75167077561e2a15)

n = G.order()

all_factors = factor(n)
print(f"factor(n) = {all_factors}")

h = Factorization(all_factors[:-1]).value()
print(f"smooth part: {h}")

Gi = G * (n//h)
Pi = client_P * (n//h)
part_key = discrete_log(Pi, Gi, operation="+")
print(f"part key: {part_key}")

print("Trying to recover full key...")

k = part_key
count = 1
while True:
    if k * G == client_P:
        break
    k += h
    count += 1
print(f"Full key: {k}")

server_P = E(27688886377906486650974531457404629460190402224453915053124314392088359043897605198852944594715826578852025617899270,20559737347380095279889465811846526151405412593746438076456912255094261907312918087801679069004409625818172174526443)

shared_sec = k * server_P
hash_512 = hashlib.sha512(int(shared_sec[0]).to_bytes(48, 'big')).digest()
key = hash_512[:32]
iv = hash_512[32:40]

pcap = rdpcap("capture.pcapng")
raw = b""

for pkt in pcap:
    if Raw in pkt:
        raw += pkt[Raw].load

raw = raw[48 * 4:]

print(f"Chacha20 key: {key} - IV: {iv}")
cipher = ChaCha20.new(key=key, nonce=iv)
test = cipher.decrypt(raw[:6])

if test == b"verify":
    cipher.seek(0)
    lines = cipher.decrypt(raw).decode().strip("\x00").split("\x00")
    for line in lines:
        print(line)

