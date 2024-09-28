from Blockchain.Backend.util.util import hash256
class Blockheader:
    def __init__(self, version, prevBlockHash, merkleRoot, timestamp, bits):
        self.version = version
        self.prevBlockHash = prevBlockHash
        self.merkleRoot  = merkleRoot
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = 0
        self.blockHash = None

    def mine(self):
        while True:
            block_data = f"{self.version}{self.prevBlockHash}{self.merkleRoot}{self.timestamp}{self.nonce}".encode()
            hash_result = hash256(block_data).hex()
            # Sesuaikan dengan target kesulitan
            if hash_result.startswith('0000'):  # Misalnya, cari hash yang dimulai dengan 4 nol
                self.blockHash = hash_result
                print(f"Hash found: {hash_result} with nonce: {self.nonce}")
                break
            self.nonce += 1

