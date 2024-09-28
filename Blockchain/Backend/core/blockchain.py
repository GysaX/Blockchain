import sys
sys.path.append('/#My Daily Folder/5. Latihan Pemrograman/9-bitcoin')

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import Blockheader
from Blockchain.Backend.util.util import hash256
import time
import json

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        self.chain = []
        self.genesisBlock()

    def genesisBlock(self):
        BlockHeight = 0
        prevBlockHash =  ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"Ariza sent {BlockHeight} BTC to John"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff01f'
        blockheader = Blockheader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockheader.mine()
        self.chain.append(Block(BlockHeight, 1, blockheader.__dict__, 1, Transaction).__dict__)
        print(json.dumps(self.chain, indent=4))

    def mine(self):
        while True:
            lastBlock = self.chain[::-1]
            BlockHeight = lastBlock[0]["Height"] + 1
            prevBlockHash = lastBlock[0]['Blockheader']['blockHash']
            self.addBlock(BlockHeight, prevBlockHash)

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.mine()  # Panggil metode mine() di sini


