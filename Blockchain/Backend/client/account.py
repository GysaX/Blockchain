import sys
sys.path.append('/#My Daily Folder/5. Latihan Pemrograman/9-bitcoin')
from Blockchain.Backend.core.EllepticCurve.EllepticCurve import Sha256Point
import secrets
from Blockchain.Backend.util.util import hash160, hash256

class account:
    def createKeys(self):
        Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

        G = Sha256Point(Gx, Gy)

        privateKey = secrets.randbits(256)
        unCompressedPyblicKey = privateKey * G
        Xpoint = unCompressedPyblicKey.x
        Ypoint = unCompressedPyblicKey.y

        if Ypoint.num % 2 == 0:
            compressKey = b'\0x2' + Xpoint.num.to_bytes(32, 'big')
        else:
            compressKey = b'\0x3' + Xpoint.num.to_bytes(32, 'big')

        hash160_var = hash160(compressKey)
        """Prefix for Mainnet"""
        main_prefix = b'\x00'

        newAddr = main_prefix + hash160_var

        """Checksum"""
        checksum = hash256(newAddr)[:4]

        newAddr = newAddr + checksum
        BASE_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

        count = 0

        for c in newAddr:
            if c == 0:
                count += 1
            else:
                break

        num = int.from_bytes(newAddr, 'big')
        prefix = '1' * count

        result = ''

        while num > 0:
            num, mod = divmod(num, 58)
            result = BASE_ALPHABET[mod] + result

        PublicAddres = prefix + result

        print(f"Private Key {privateKey}")
        print(f"Public Key  {PublicAddres}")

if __name__ =='__main__':
    acct = account()
    acct.createKeys()
