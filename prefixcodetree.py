from bitstring import BitArray

class PrefixCodeTree:
    """
    docstring
    """
    def __init__(self):
        self.Trie = {}
        pass
    
    def listToString(self,s):
        # initialize an empty string 
        str1 = "" 
        # return string   
        for i in s:
            str1 = str1 + str(i)
        return str1 

    def insert(self,codeword, symbol):
        self.Trie[symbol] = self.listToString(codeword)
    
    def decode(self, encodedData, datalen):
        a = BitArray(bytes=encodedData,length=datalen)
        b = a.bin
        res = ""
        while b:
            for k in self.Trie:
                if(b.startswith(self.Trie[k])):
                    res += k
                    b = b[len(self.Trie[k]):]
        return res


codebook = {
'x1': [0],
'x2': [1,0,0],
'x3': [1,0,1],
'x4': [1,1]
}

codeTree = PrefixCodeTree()

for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

message = codeTree.decode(b'\xd2\x9f\x20', 21)
print(message)