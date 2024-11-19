import asyncio
from asyncio import *
async def fire():
    n = 5
    while n:
        n-=1
        print("ROCKET FIRED!", end = '\r')
        await asyncio.sleep(1)

async def fire2():
    while True:
        print("ROCKET FIRED!", end = '')
        await asyncio.sleep(2)

print("ROCKET FIRED!")
run(fire())
print("a", end = '')