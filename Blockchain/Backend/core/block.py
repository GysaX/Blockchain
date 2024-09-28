class Block:
    """
    Block is a storage container that stores transactions
    """
    def __init__(self, Height, Blocksize, Blockheader, TxCount, Txs):
        self.Height = Height
        self.Blocksize = Blocksize
        self.Blockheader  = Blockheader
        self.TxCount = TxCount
        self.Txs = Txs

