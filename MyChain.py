# 每个区块链都包含时间、自己的哈希值、上一区块的哈希值、难度、随机值、交易数据
# 每个区块的哈希值=计算（一系列的值+上一区块的哈希值）

# 验证区块方法
# POW 工作量证明
import time
import hashlib
import json

class Block():
    def __init__(self,msg,previous_hash):
        self.time_stamp = time.asctime(time.localtime(time.time()))
        self.previous_hash = previous_hash
        self.msg = msg
        self.nonce = 1
        self.hash = self.get_hash()

    def get_hash(self):   # 计算哈希值
        data = self.time_stamp + self.msg + self.previous_hash + str(self.nonce)
        hash256 = hashlib.sha256()
        hash256.update(data.encode('gb2312'))
        return hash256.hexdigest()

    def mine(self,diffculty):
        target = ''
        for each_num in range(0,diffculty):
            target = target + '0'
        while(int(self.hash[0:diffculty] != target)):
            self.nonce = self.nonce+1
            self.hash = self.get_hash()
        print('Mined a new block')


class MyChain():
    # 初始化
    def __init__(self,diffculty):
        self.list = []
        self.diffculty = diffculty

# 添加区块
    def add_block(self,block):
        block.mine(self.diffculty)
        self.list.append(block)
# 打印所有区块
    def show(self):
        json_res = json.dumps(self.list,default=self.block_dict)
        print(json_res)
    def block_dict(self,block):
        return block.__dict__
        # 验证哈希值
    def isChainValid(self):
         for i in range(1,len(self.list)):
             current_block = self.list[i]
             previous_block = self.list[i-1]
             if (current_block.hash != current_block.get_hash()):
                 print('Current Block is not equal')
                 return False
             if (current_block.previous_hash != previous_block.hash):
                 print('Previous hash is not correct')
                 return False
             print('All the blocks are correct')
             return  True

c = MyChain(1)
c.add_block(Block('first','0'))
c.add_block(Block('second',c.list[len(c.list)-1].hash))
c.show()
c.isChainValid()

blockchain_list = []
genesis_block = Block('0','hello block!')  # 创世区块
print(genesis_block.hash)
second_block = Block(genesis_block.hash,'second message!')
print(second_block.hash)
blockchain_list.append(genesis_block)
blockchain_list.append(second_block)
json_blockchain = json.dumps([obj.__dict__ for obj in blockchain_list])
print(json_blockchain)

