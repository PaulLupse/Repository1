#cmmdc

a = int(input())
b = int(input())
cpa = a
cpb = b

while a is not b:
    if a < b:
        b -= a
    else: a -= b
print(f"CMMDC: {a:.0f}")

#cmmmc

cmmmc = (cpa*cpb/a)
print(f"CMMMC: {cmmmc:.0f}")