a = int(input()).split()
b = int(input()).split()
cpa = a
cpb = b

#cmmdc

while a * b != 0:
    if a < b:
        b = b % a
    else: a = a % b
print(f"CMMDC: {a + b:.0f}")

#cmmmc

cmmmc = (cpa*cpb/(a+ b))
print(f"CMMMC: {cmmmc:.0f}")