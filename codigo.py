import binascii
print("oii")
print("tudo bem?")


print("sim e vc")

print("tudo bem tambem")


x=input("digite algo")
binascii.hexlify(bytes(x,"utf-8"))
for c in x:
    print("".join(hex(ord(c))[2:]))
