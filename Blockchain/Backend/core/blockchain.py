import sys
sys.path.append('/#My Daily Folder/5. Latihan Pemrograman/9-bitcoin')

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import Blockheader
from Blockchain.Backend.util.util import hash256
from Blockchain.Backend.core.database.database import BlockchainDB
import time

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        self.genesisBlock()

    def write_on_disk(self, block):
        blockchainDB = BlockchainDB()
        blockchainDB.write(block)

    def fetch_last_block(self):
        blockchainDB = BlockchainDB()
        return blockchainDB.lastBlock()

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
        self.write_on_disk([Block(BlockHeight, 1, blockheader.__dict__, 1, Transaction).__dict__])

    def mine(self):
        while True:
            lastBlock = self.fetch_last_block()
            BlockHeight = lastBlock["Height"] + 1
            prevBlockHash = lastBlock['Blockheader']['blockHash']
            self.addBlock(BlockHeight, prevBlockHash)

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.mine()  # Panggil metode mine() di sini


