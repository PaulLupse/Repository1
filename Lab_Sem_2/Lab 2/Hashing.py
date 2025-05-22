import numpy as np
np.seterr(over='ignore')

MOD = 2**32 - 1

constante_sha256 = ('428a2f98', '71374491', 'b5c0fbcf', 'e9b5dba5', '3956c25b', '59f111f1', '923f82a4', 'ab1c5ed5',
'd807aa98', '12835b01', '243185be', '550c7dc3', '72be5d74', '80deb1fe', '9bdc06a7', 'c19bf174',
'e49b69c1', 'efbe4786', '0fc19dc6', '240ca1cc', '2de92c6f', '4a7484aa', '5cb0a9dc', '76f988da',
'983e5152', 'a831c66d', 'b00327c8', 'bf597fc7', 'c6e00bf3', 'd5a79147', '06ca6351', '14292967',
'27b70a85', '2e1b2138', '4d2c6dfc', '53380d13', '650a7354', '766a0abb', '81c2c92e', '92722c85',
'a2bfe8a1', 'a81a664b', 'c24b8b70', 'c76c51a3', 'd192e819', 'd6990624', 'f40e3585', '106aa070',
'19a4c116', '1e376c08', '2748774c', '34b0bcb5', '391c0cb3', '4ed8aa4a', '5b9cca4f', '682e6ff3',
'748f82ee', '78a5636f', '84c87814', '8cc70208', '90befffa', 'a4506ceb', 'bef9a3f7', 'c67178f2',
                    )

def __st_rot(numar, nr_pos):
    bin_numar = bin(numar)[2::]
    bin_numar = '0' * (32 - len(bin_numar)) + bin_numar
    bin_numar = bin_numar[nr_pos::] + bin_numar[:nr_pos:]
    return np.uint32(int(bin_numar, 2))

def __dr_rot(numar, nr_pos):
    bin_numar = bin(numar)[2::]
    bin_numar = '0' * (32 - len(bin_numar)) + bin_numar
    bin_numar = bin_numar[-nr_pos::] + bin_numar[:-nr_pos:]
    return np.uint32(int(bin_numar, 2))

def _string_bin(string):

    string_bin = ''
    for caracter in string:
        caracter_binar = bin(ord(caracter))[2::]
        # padding
        caracter_binar = '0' * (8 - len(caracter_binar)) + caracter_binar
        string_bin += caracter_binar

    return string_bin

def sha_1(mesaj):

    bin_mesaj = _string_bin(mesaj)

    lung_bin_mesaj = len(bin_mesaj)

    # padding la mesaj

    bin_mesaj += '1'
    nr_zerouri = 512 * ((lung_bin_mesaj + 1 - 448) // 512 + 1) - (lung_bin_mesaj + 1 - 448)
    bin_mesaj += '0' * nr_zerouri
    nr_zerouri_lungime_mesaj = 64 - len(bin(lung_bin_mesaj)[2::])
    bin_mesaj += '0' * nr_zerouri_lungime_mesaj + bin(lung_bin_mesaj)[2::]

    # se imparte scrierea binara a mesajului in 'bloc'-uri de cate 512 biti

    lung_bin_mesaj = len(bin_mesaj)
    lista_blocuri = []
    for i in range(0, lung_bin_mesaj, 512):
        lista_blocuri.append(bin_mesaj[i:min(i + 512, lung_bin_mesaj)])
        i += 512

    # compresia
    global h1, h2, h3, h4, h5 # constantele initiale
    h1 = np.uint32(1732584193)
    h2 = np.uint32(4023233417)
    h3 = np.uint32(2562383102)
    h4 = np.uint32(271733878)
    h5 = np.uint32(3285377520)

    for bloc in lista_blocuri:
        global A, B, C, D, E
        A = np.uint32(h1)
        B = np.uint32(h2)
        C = np.uint32(h3)
        D = np.uint32(h4)
        E = np.uint32(h5)

        # blocul se imparte in bucati de cate 32 de biti (16 bucati in total), numite 'cuvinte' sau 'dublucuvinte' (doubleword)
        cuvinte = []
        for i in range(0, len(bloc), 32):
            cuvinte.append(int(bloc[i:i + 32:], 2))

        for i in range(16, 80):
            cuvinte.append(np.uint32(__st_rot(np.uint32(np.uint32(cuvinte[i - 3] ^ cuvinte[i - 8]) ^ cuvinte[i - 14]) ^ cuvinte[i - 16], 1)))

        for index, cuvant in enumerate(cuvinte):

            if index < 20:
                k = 1518500249
                f = np.uint32((B & C) | ((~B) & D))
            elif index < 40:
                k = 1859775393
                f = np.uint32(B ^ C ^ D)
            elif index < 60:
                k = 2400959708
                f = np.uint32((B & C) | (B & D) | (C & D))
            else:
                k = 3395469782
                f = np.uint32(B ^ C ^ D)

            temp = np.uint32(__st_rot(A, 5) + f + E + k + cuvant)

            E = D
            D = C
            C = np.uint32(__st_rot(B, 30))
            B = A
            A = temp

        h1 = np.uint32(h1 + A)
        h2 = np.uint32(h2 + B)
        h3 = np.uint32(h3 + C)
        h4 = np.uint32(h4 + D)
        h5 = np.uint32(h5 + E)


    return hex(h1)[2::] + hex(h2)[2::] + hex(h3)[2::] + hex(h4)[2::] + hex(h5)[2::]

def __ch(x, y, z):
    return (x & y) ^ (~x & z)

def __maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

def __sigma_0(x):
    return __dr_rot(x, 2) ^ __dr_rot(x, 13) ^ __dr_rot(x, 22)

def __sigma_1(x):
    return __dr_rot(x, 6) ^ __dr_rot(x, 11) ^ __dr_rot(x, 25)

def __lsigma_0(x):
    return __dr_rot(x, 7) ^ __dr_rot(x, 18) ^ (x >> 3)

def __lsigma_1(x):
    return __dr_rot(x, 17) ^ __dr_rot(x, 19) ^ (x >> 10)

def __sum_mod(numere, MOD):

    if len(numere) > 2:
        return (__sum_mod(numere[:-1:], MOD) + numere[-1]) % MOD
    return (numere[0] + numere[1]) % MOD

def sha_256(mesaj):

    k = [int(constanta, 16) for constanta in constante_sha256]

    bin_mesaj = ''

    bin_mesaj = _string_bin(mesaj)

    lung_bin_mesaj = len(bin_mesaj)

    # padding la mesaj

    bin_mesaj += '1'
    nr_zerouri = 512 * ((lung_bin_mesaj + 1 - 448) // 512 + 1) - (lung_bin_mesaj + 1 - 448)
    bin_mesaj += '0' * nr_zerouri
    nr_zerouri_lungime_mesaj = 64 - len(bin(lung_bin_mesaj)[2::])
    bin_mesaj += '0' * nr_zerouri_lungime_mesaj + bin(lung_bin_mesaj)[2::]

    # se imparte scrierea binara a mesajului in 'bloc'-uri de cate 512 biti

    lung_bin_mesaj = len(bin_mesaj)
    lista_blocuri = []
    for i in range(0, lung_bin_mesaj, 512):
        lista_blocuri.append(bin_mesaj[i:min(i + 512, lung_bin_mesaj)])
        i += 512


    # compresia
    global h1, h2, h3, h4, h5, h6, h7, h8 # constantele initiale
    h1 = 1779033703
    h2 = 3144134277
    h3 = 1013904242
    h4 = 2773480762
    h5 = 1359893119
    h6 = 2600822924
    h7 = 528734635
    h8 = 1541459225

    # se aceseaza fiecare bloc
    for bloc in lista_blocuri:
        global A, B, C, D, E, F, G, H
        A = h1
        B = h2
        C = h3
        D = h4
        E = h5
        F = h6
        G = h7
        H = h8

        # blocul se imparte in bucati de cate 32 de biti (16 bucati in total), numite 'cuvinte' sau 'dublucuvinte' (doubleword)
        cuvinte = []
        for i in range(0, len(bloc), 32):
            cuvinte.append((int(bloc[i:i + 32:], 2)))

        # se mai construiesc 64 de cuvinte
        for i in range(16, 64):
            cuvinte.append((__sum_mod((__lsigma_1(cuvinte[i-2]), cuvinte[i-7], __lsigma_0(cuvinte[i-15]), cuvinte[i-16],), MOD)))

        #print('init: ', hex(A), hex(B), hex(C), hex(D), hex(E), hex(F), hex(G), hex(H))

        for i in range(0, 64):
            temp1 = (__sum_mod((H, __sigma_1(E), __ch(E, F, G), k[i], cuvinte[i]), MOD))
            temp2 = (__sum_mod((__sigma_0(A), __maj(A, B, C)), MOD))
            H = G
            G = F
            F = E
            E = (__sum_mod((D, temp1), MOD))
            D = C
            C = B
            B = A
            A = (__sum_mod((temp1, temp2), MOD))

            #print(i, hex(A), hex(B), hex(C), hex(D), hex(E), hex(F), hex(G), hex(H))

        h1 = (__sum_mod((h1, A), MOD))
        h2 = (__sum_mod((h2, B), MOD))
        h3 = (__sum_mod((h3, C), MOD))
        h4 = (__sum_mod((h4, D), MOD))
        h5 = (__sum_mod((h5, E), MOD))
        h6 = (__sum_mod((h6, F), MOD))
        h7 = (__sum_mod((h7, G), MOD))
        h8 = (__sum_mod((h8, H), MOD))

    return hex(h1)[2::] + hex(h2)[2::] + hex(h3)[2::] + hex(h4)[2::] + hex(h5)[2::] + hex(h6)[2::] + hex(h7)[2::] + hex(h8)[2::]

if __name__ == '__main__':
    print(sha_256('a'))
    #print(sha_256('La soare roata se mareste, la umbra numai carnea creste, si somn e carnea, se dezumfla, dar frig si umbra iar o umfla. La soare roata se mareste, la umbra numai carnea creste, si somn e carnea, se dezumfla, dar frig si umbra iar o umfla. La soare roata se mareste, la umbra numai carnea creste, si somn e carnea, se dezumfla, dar frig si umbra iar o umfla. La soare roata se mareste, la umbra numai carnea creste, si somn e carnea, se dezumfla, dar frig si umbra iar o umfla. La soare roata se mareste, la umbra numai carnea creste, si somn e carnea, se dezumfla, dar frig si umbra iar o umfla. La soare roata se mareste, la umbra numai carnea creste, si somn e carnea, se dezumfla, dar frig si umbra iar o umfla.'))