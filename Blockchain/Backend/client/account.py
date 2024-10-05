import sys
sys.path.append('/#My Daily Folder/5. Latihan Pemrograman/9-bitcoin')
from Blockchain.Backend.core.EllepticCurve.EllepticCurve import Sha256Point
import secrets
from Blockchain.Backend.util.util import hash160, hash256

class account:
    def createKeys(self, prefix='garuda'):
        Gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
        Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8

        G = Sha256Point(Gx, Gy)

        # Menggunakan secrets.token_bytes untuk menghasilkan 32 byte (256-bit) private key
        privateKey = secrets.token_bytes(32)  # 32 bytes = 256 bits
        privateKeyHex = privateKey.hex()  # Mengubahnya menjadi format hexadecimal
        
        # Menggabungkan awalan "garuda" dengan private key hexadecimal
        customPrivateKey = f"{prefix}{privateKeyHex}"
        
        # Menggunakan privateKey yang sudah dalam byte untuk mendapatkan public key
        privateKey_int = int.from_bytes(privateKey, 'big')  # Ubah dari bytes ke integer
        unCompressedPublicKey = privateKey_int * G
        Xpoint = unCompressedPublicKey.x
        Ypoint = unCompressedPublicKey.y

        if Ypoint.num % 2 == 0:
            compressKey = b'\x02' + Xpoint.num.to_bytes(32, 'big')
        else:
            compressKey = b'\x03' + Xpoint.num.to_bytes(32, 'big')

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

        # Menampilkan private key custom dengan awalan 'garuda'
        print(f"Private Key : {customPrivateKey}")
        print(f"Public Key  : {PublicAddres}")

if __name__ =='__main__':
    acct = account()
    acct.createKeys()
