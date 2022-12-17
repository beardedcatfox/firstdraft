from bit.crypto import ECPrivateKey
import random

from bit.format import (
    bytes_to_wif,
    public_key_to_address)

from bit.utils import hex_to_bytes
#############################################################################################################

a1 = open('1ma.txt', 'r', encoding='utf8')
dd = dict()
ab = open('hack.txt', 'w', encoding='utf8')

for qa in a1:
    dd[qa.strip()] = 'yes, bitch'

sss = 1
while True:
    sh = ['b', '0', 'a', 'd', '8', '6', 'f', '7', '1', 'e', '3', '2', '4', 'c', '9', '5']
    b = random.choices(sh, k=(64))
    #a = '000000000000000000000000000000000000000000000000' + ''.join(b)
    ae = ''.join(b)
    bw = hex_to_bytes(ae)
    wif = bytes_to_wif(bw)
    hw = public_key_to_address(ECPrivateKey(bw).public_key.format())            #сжатый!
    sss += 1
    print(sss)

    if str(hw) in dd:
        print(hw, ae, wif, file=ab)
        print(hw, ae, wif)
        break
